web: sh setup.sh && /app/.heroku/python/bin/python -m pip install -r requirements.txt && streamlit run main.py
# worker: /app/.heroku/python/bin/python -m pip install --upgrade pip && /app/.heroku/python/bin/python -m pip install -r requirements.txt && cd backend && uvicorn main:app --host=0.0.0.0 --port=$PORT
worker: /app/.heroku/python/bin/python -m pip install --upgrade pip && /app/.heroku/python/bin/python -m pip install -r requirements.txt && cd backend && /app/.heroku/python/bin/python main.py
