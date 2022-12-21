FROM python:latest

LABEL Maintainer="alvesgf16"

WORKDIR /app

COPY . .

CMD ["python", "./sample/atm.py"]