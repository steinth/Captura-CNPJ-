from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Carregar planilha
df = pd.read_excel("C:/Users/thiagorotundo/Documents/sistemas/vscode jhsf/automacoes/dados_cnpjs_invertexto.xlsx")

# Iniciar navegador
driver = webdriver.Chrome()
driver.get("https://nfseembudasartes.obaratec.com.br/ords/embu01/f?p=935:65::::65::")

# Loop pelos dados
for _, row in df.iterrows():

    try:
        # Preencher campos
        driver.find_element(By.NAME, "P65_COTR_NUM_CNPJ").clear()
        driver.find_element(By.NAME, "P65_COTR_NUM_CNPJ").send_keys(row["CNPJ"])

        driver.find_element(By.NAME, "P65_COTR_DES_RAZAO_SOCIAL").clear()
        driver.find_element(By.NAME, "P65_COTR_DES_RAZAO_SOCIAL").send_keys(row["Razão Social"])

        driver.find_element(By.NAME, "P65_COTR_DES_ENDERECO").clear()
        driver.find_element(By.NAME, "P65_COTR_DES_ENDERECO").send_keys(row["Endereço"])

        driver.find_element(By.NAME, "P65_COTR_NUM_ENDERECO").clear()
        driver.find_element(By.NAME, "P65_COTR_NUM_ENDERECO").send_keys(str(row["Número"]))

        cep_limpo = str(row["CEP"]).replace(".", "").replace("-", "")
        driver.find_element(By.NAME, "P65_COTR_NUM_CEP").clear()
        driver.find_element(By.NAME, "P65_COTR_NUM_CEP").send_keys(cep_limpo)

        complemento = "" if pd.isna(row["Complemento"]) else str(row["Complemento"])
        driver.find_element(By.NAME, "P65_COTR_DES_COMPLEMENTO").clear()
        driver.find_element(By.NAME, "P65_COTR_DES_COMPLEMENTO").send_keys(complemento)

        driver.find_element(By.NAME, "P65_COTR_DES_BAIRRO").clear()
        driver.find_element(By.NAME, "P65_COTR_DES_BAIRRO").send_keys(row["Bairro"])

        driver.find_element(By.NAME, "P65_COTR_NOM_CIDADE").clear()
        driver.find_element(By.NAME, "P65_COTR_NOM_CIDADE").send_keys(row["Cidade"])

        driver.find_element(By.NAME, "P65_COTR_NOM_UF").clear()
        driver.find_element(By.NAME, "P65_COTR_NOM_UF").send_keys(row["UF"])

        driver.find_element(By.NAME, "P65_COTR_DES_EMAIL").clear()
        driver.find_element(By.NAME, "P65_COTR_DES_EMAIL").send_keys("cadastroprefeitura@jhsf.com.br")

        driver.find_element(By.NAME, "P65_CONFIRMA_EMAIL").clear()
        driver.find_element(By.NAME, "P65_CONFIRMA_EMAIL").send_keys("cadastroprefeitura@jhsf.com.br")

        # Botão
        botao = driver.find_element(By.ID, "B489474186242244765")
        driver.execute_script("arguments[0].scrollIntoView(true);", botao)
        time.sleep(1)
        botao.click()

        time.sleep(2)

        # Verificar se aparece a mensagem de CNPJ já cadastrado
        erro_cnpj = driver.find_elements(
            By.XPATH, "//*[contains(text(), 'Já existe Contribuinte Cadastrado')]"
        )

        if erro_cnpj:
            print(f"CNPJ {row['CNPJ']} CNPJ já cadastrado na prefeitura de Embu das artes")
            continue

        print(f"CNPJ {row['CNPJ']} cadastrado com sucesso.")

    except Exception as e:
        print(f"Erro ao cadastrar {row['CNPJ']}: {e}")
        continue

driver.quit()
