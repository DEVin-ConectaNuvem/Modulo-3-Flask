# Flask-API

### Pré-requisitos

- Ter o Python, Poetry, Postgres instalado na sua máquina.
- Criar um projeto de OAuth2 no Google Cloud Platform para utilizar todas as funcionalidades
- No postgres, criar as databases conforme o nome do seu NAME_DB + o prefixo do ambiente
### Configurações
- Executar o comando: poetry config --local virtualenvs.in-project true
- Executar o comando: poetry install para instalar as dependências.
- Criar um arquivo .env baseado no arquivo .env_example e colocar os campos necessários.

### Executar a aplicação

- Para executar a aplicação, utilize o comando: poetry run flask run