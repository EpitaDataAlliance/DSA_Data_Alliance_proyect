FROM python:3.8.13

RUN mkdir /streamlit

COPY requirements.txt /streamlit

WORKDIR /streamlit

RUN /usr/local/bin/python -m pip install --upgrade pip && /usr/local/bin/python -m pip install -r requirements.txt

COPY . /streamlit

ENV ON_DOCKER Yes

EXPOSE 8501

CMD ["streamlit", "run", "main.py"]