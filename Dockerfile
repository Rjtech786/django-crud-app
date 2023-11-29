FROM python3

WORKDIR data

RUN pip install django==4.2.7

COPY . .

RUN python manage.py migrate

EXPOSE 8000

CMD [python,manage.py,runserver,0.0.0.08000]
