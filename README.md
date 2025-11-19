# Automação de Cadastro de Empresas

Este projeto realiza o fluxo completo de captura e cadastro de empresas utilizando Python, Selenium e Pandas.

## Objetivo

Automatizar o processo de cadastro de empresas em sistemas públicos, reduzindo trabalho manual e evitando erros repetitivos.

## Como funciona

1. **Captura dos dados**
   A automação consulta uma API pública de dados cadastrais utilizando CNPJ como entrada, recebendo informações como:

   * Razão Social
   * Endereço
   * CEP
   * Cidade
   * UF
     e outros dados básicos da empresa.

2. **Geração de planilha**
   Os dados retornados são tratados e armazenados automaticamente em uma planilha Excel, que serve como base para a segunda etapa.

3. **Automação de cadastro na Prefeitura**
   Utilizando Selenium, o script acessa o portal da Prefeitura e preenche automaticamente o formulário de solicitação de cadastro para cada empresa da planilha.

   O robô:

   * Abre o navegador
   * Preenche os campos com os dados da planilha
   * Envia o formulário
   * Verifica se o CNPJ já está cadastrado e, se estiver, segue para o próximo registro sem interromper o processo

4. **Execução totalmente automatizada**
   Uma vez iniciado, o fluxo completo roda do início ao fim sem necessidade de intervenção manual.

## Tecnologias utilizadas

* Python
* Selenium WebDriver
* Pandas
* ChromeDriver

## Observações

* Nenhuma informação sensível ou restrita foi incluída no repositório.
* O código e o exemplo de automação são genéricos e podem ser adaptados para qualquer outro portal de cadastro público.

## Objetivo educacional

O projeto foi desenvolvido como exercício prático de:

* Automação de processos repetitivos
* Web scraping
* Manipulação de dados
* Interação com sistemas Web via Selenium

---
