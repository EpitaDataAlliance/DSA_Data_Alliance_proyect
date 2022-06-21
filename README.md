# Mobile Price Prediction App built with Streamlit, Grafana, FastAPI, Airflow, and Docker


### Follow the Commands below to Run the Project

`git clone https://github.com/EpitaDataAlliance/DSA_Data_Alliance_proyect.git`

`cd DSA_Data_Alliance_proyect`

`docker-compose up airflow-init`

`docker-compose up --build`


### URLs of the Applications

- Streamlit -> http://0.0.0.0:8501
- Airflow   -> http://0.0.0.0:8080 -> default user:pass -> airflow:airflow
- Grafana   -> http://0.0.0.0:3000 -> default user:pass -> admin:admin123
- FastAPI   -> http://0.0.0.0:5000


### Demo Version 

A running version of the project can be found at http://35.78.183.136:<app_port> 
except the Airflow part since the AWS EC2 instance does not have enough resources to run
