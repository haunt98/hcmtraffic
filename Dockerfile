FROM python:3

RUN pip install requests

WORKDIR /usr/src/app

COPY main.py .

CMD ["python", "main.py"]
