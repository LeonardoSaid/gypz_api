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

## License
[MIT](https://choosealicense.com/licenses/mit/)
