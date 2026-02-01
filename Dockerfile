FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py app.py
COPY best_lead_conversion_model.pkl best_lead_conversion_model.pkl

EXPOSE 7860

CMD ["python", "app.py"]
