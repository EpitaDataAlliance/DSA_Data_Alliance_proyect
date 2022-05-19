web: sh setup.sh && python -m pip install -r requirements.txt && uvicorn main:app --host=0.0.0.0 --port=${PORT:-5000}
worker: python -m pip install -r requirements.txt && cd backend && python3 main.py
