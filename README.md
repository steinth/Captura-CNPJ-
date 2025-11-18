**Consulta de CNPJs – Automação com Python**

Automação em Python para consulta e extração de informações de CNPJs utilizando a API do Invertexto.
O script realiza consultas em massa a partir de um arquivo CSV, processa cada CNPJ, extrai dados relevantes e salva tudo em um arquivo Excel.
Além disso, gera um arquivo de log registrando cada etapa da execução.


Funcionalidades

Leitura automática de CNPJs de um arquivo .csv

Consulta individual de cada CNPJ na API do Invertexto

Normalização dos dados, incluindo zeros à esquerda

Exportação dos resultados para um arquivo .xlsx

Tratamento automático para limite de requisição (HTTP 429)

Continuidade automática: se o Excel existir, o script retoma de onde parou

Ignora CNPJs duplicados já consultados
