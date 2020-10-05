FROM python:3.6

#python output is set straight to the terminal
ENV PYTHONUNBUFFERED 1

RUN mkdir /gypz_api
WORKDIR /gypz_api
COPY requirements.txt /gypz_api/
EXPOSE 8000
RUN pip install -r requirements.txt
COPY . /gypz_api/
CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000