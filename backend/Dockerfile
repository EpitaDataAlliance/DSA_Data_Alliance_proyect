FROM python:3.8.13

WORKDIR /app

RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip3 install -r ../requirements.txt

COPY . .

EXPOSE 8080

CMD ["python", "main.py"]
