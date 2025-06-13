FROM python:3.9-slim

WORKDIR /app

COPY src/requirements.txt .
RUN pip install -r requirements.txt

COPY ../data ./data
COPY src/*.py .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.address", "0.0.0.0"]
