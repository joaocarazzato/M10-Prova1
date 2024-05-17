# M10-Prova1
Repositório responsável por armazenar a parte prática da primeira prova do Módulo 1 de Engenharia da Computação. Feito por **João Pedro Gonçalves Carazzato**

## Como executar?

Primeiro, precisamos clonar nosso projeto com o seguinte comando:

```
git clone https://github.com/joaocarazzato/M10-Prova1.git
```

Após isso, considerando que já possuímos o [Docker](https://www.docker.com) instalado, podemos executar a nossa aplicação com o seguinte comando dentro da pasta **src**:
```
docker compose up
```

Após isso, a nossa aplicação e nosso banco de dados já vão estar rodando e pronto para utilização!

**Para acessar nossa aplicação usamos o endereço local:**
[http://localhost:5000](http://localhost:5000)

A fim de testar as rotas que temos, podemos utilizar a **Collection do [Insomnia](https://insomnia.rest)** que pode ser encontrada dentro da pasta **docs** e [importada](https://docs.insomnia.rest/insomnia/import-export-data) para seu aplicativo.

## Pastas e arquivos
Aqui segue uma segmentação para conhecimento da atual divisão de pastas/arquivos:
```
- README.md
- .gitignore
- docs
    - Insomnia_2024-05-17.yaml 
    # Export do insomnia contendo todas as rotas testadas com exemplos

-src
    - database 
    # Modelos para nosso banco de dados poder ser utilizado de forma simples e rápida
        - database.py # Cria a conexão assíncrona
        - models.py # Definição da tabela da DB que vamos usar

    - db.sql # Definição da tabela em SQL para o PostgreSQL utilizar
    - docker-compose.yml # Compose contendo o container do Postgres e da API
    - Dockerfile # Dockerfile responsável pela criação da imagem da API
    - main.py # Todo o código da API pode ser localizado aqui em FastAPI
    - requirements.txt # Requerimentos para execução do código da API
```