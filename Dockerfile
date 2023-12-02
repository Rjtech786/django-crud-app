FROM python:3

WORKDIR . .

RUN pip install django==4.2.7

COPY . .

RUN python install -r requirements.txt

RUN python manage.py migrate

EXPOSE 8000 

CMD [python,manage.py,runserver,0.0.0.0:8000]
