FROM python:3.12-slim


WORKDIR /application


COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000 

CMD ["gunicorn","dailypay.wsgi:application","--bind","0.0.0.0:8000"]
