FROM python:3.8.13

RUN mkdir /backend

COPY requirements.txt /backend

WORKDIR /backend

RUN /usr/local/bin/python -m pip install --upgrade pip && /usr/local/bin/python -m pip install -r requirements.txt

COPY . /backend/

EXPOSE 5000

CMD ["python", "main.py"]