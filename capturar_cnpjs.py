
import requests
import pandas as pd
import time
import os

ARQUIVO_CNPJS = "C:/Users/thiagorotundo/Documents/sistemas/vscode jhsf/automacoes/cnpjs.csv"
ARQUIVO_SAIDA = "C:/Users/thiagorotundo/Documents/sistemas/vscode jhsf/automacoes/dados_cnpjs_invertexto.xlsx"
TOKEN = "23046|uxuPMkgRr98WAuBZ80x20cn4fPPI2Huv"

# Lê os CNPJs 
df_cnpjs = pd.read_csv(ARQUIVO_CNPJS, header=None, names=['CNPJ'])

# Se já existir arquivo de saída, carrega para continuar
if os.path.exists(ARQUIVO_SAIDA):
    df_saida = pd.read_excel(ARQUIVO_SAIDA)
    dados_coletados = df_saida.to_dict(orient="records")
    cnpjs_existentes = set(df_saida['CNPJ'].astype(str))
else:
    dados_coletados = []
    cnpjs_existentes = set()

for index, row in df_cnpjs.iterrows():
    cnpj = str(row['CNPJ']).strip()
    cnpj = cnpj.zfill(14)  # Corrige zeros à esquerda

    if cnpj in cnpjs_existentes:
        print(f"⏩ Ignorando {cnpj}, já consultado.")
        continue

    print(f"Consultando CNPJ: {cnpj}")
    url = f"https://api.invertexto.com/v1/cnpj/{cnpj}?token={TOKEN}"

    try:
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            data = response.json()
            if "razao_social" in data:
                endereco = data.get("endereco", {})
                situacao = data.get("situacao", {})
                registro = {
                    "CNPJ": cnpj,
                    "Razão Social": data.get("razao_social"),
                    "Nome Fantasia": data.get("nome_fantasia"),
                    "CEP": endereco.get("cep"),
                    "Endereço": endereco.get("logradouro"),
                    "Número": endereco.get("numero"),
                    "Complemento": endereco.get("complemento"),
                    "Bairro": endereco.get("bairro"),
                    "Cidade": endereco.get("municipio"),
                    "UF": endereco.get("uf"),
                    "Situação": situacao.get("nome")
                }
                dados_coletados.append(registro)

                # Remove cnpjs duplicados e salva
                df_saida = pd.DataFrame(dados_coletados).drop_duplicates(subset=['CNPJ'])
                df_saida.to_excel(ARQUIVO_SAIDA, index=False)
                print(f"✅ Dados salvos para {cnpj}")
            else:
                print(f"⚠ Erro na consulta do CNPJ {cnpj}: {data}")
        elif response.status_code == 429:
            print("⚠ Limite atingido! Aguardando 60 segundos antes de continuar...") #api tem limite de 10 consultas por minuto
            time.sleep(60)
            continue
        else:
            print(f"❌ Erro HTTP ao consultar {cnpj}: {response.status_code}")
    except Exception as e:
        print(f"❌ Erro inesperado para {cnpj}: {e}")

    # Pausa para evitar bloqueio da api
    time.sleep(6)

print(f"✅ Processo concluído! Arquivo final: {ARQUIVO_SAIDA}")