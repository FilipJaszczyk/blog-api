FROM python:3.9-buster

WORKDIR /opt/app

ENV PYTHONDONTWRITEBYTECODE=1 \
 PYTHONUNBUFFERED=1

COPY /src . \
    Pipfile . \
    Pipfile.lock ./

RUN pip install pipenv \
 && pipenv install --system --deploy --ignore-pipfile

EXPOSE 8080

CMD [ "gunicorn", "-c", "config/gunicorn.conf.py" ]
