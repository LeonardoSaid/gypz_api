# GYPZ API - Backend

![2020-09-22-11-13-gypz-dom herokuapp com](https://user-images.githubusercontent.com/32913906/93893999-a4fc2900-fcc4-11ea-83d9-3b6ce68346f3.png)

- GYPZ Tech Challenge: [https://github.com/gypzlab/tech_challenge](https://github.com/gypzlab/tech_challenge)
- Preview/Demo: [http://gypz-api.herokuapp.com/](http://gypz-api.herokuapp.com/)
- Repositório do Frontend: [https://github.com/LeonardoSaid/gypz_dom](https://github.com/LeonardoSaid/gypz_dom)

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/fe1bbe5d90d96762c4c3)

## Requisitos

- Python 3.6
- Django
- Django REST Framework

A lista completa de requisitos está disponível em `requirements.txt`

## Instalação

Recomendado criar um ambiente virtual antes

```bash
git clone https://github.com/LeonardoSaid/gypz_api.git
cd gypz_api
pip install django djangorestframework djangorestframework-jwt django-cors-headers
```

Para iniciar a aplicação:

```bash
python manage.py migrate
python manage.py runserver
```

## Docker

### Dockerfile

Se quiser usar o Dockerfile presente no root do projeto basta montar a imagem e executar:

```bash
# executando gypz_api em modo detached na porta 8000
docker build -t gypz_api .
docker run -dp 8000:8000 gypz_api
```

### Docker-compose

Para utilizar o `docker-compose.yml` providenciado, coloque o arquivo junto com as pastas dos projetos `gypz_api` e `gypz_dom` e execute:

```bash
# com docker-compose.yml, /gypz_dom/ e /gypz_api/ no mesmo diretório
docker-compose up -d --build
```

## Licença
[MIT](https://choosealicense.com/licenses/mit/)
