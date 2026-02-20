from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2  # For PostgreSQL

app = FastAPI()
class SensorData(BaseModel):
    timestamp: str
    vibration: float
    temp: float
    # Add more fields

conn = psycopg2.connect("dbname=postgres user=postgres password=yourpass")

@app.post("/ingest")
def ingest(data: SensorData):
    cur = conn.cursor()
    cur.execute("INSERT INTO sensors (timestamp, vibration, temp) VALUES (%s, %s, %s)", (data.timestamp, data.vibration, data.temp))
    conn.commit()
    return {"status": "ingested"}