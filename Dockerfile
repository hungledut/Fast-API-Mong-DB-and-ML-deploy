FROM python:3.11

ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . ./

CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "7979"]