
import os
from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from health_app.data import load_users_health_records, save_users_health_records
from health_app.health import Health


DATA_FILE = os.getenv("HEALTH_RECORDS_FILE", "data/health_records.json")

app = FastAPI(title="Health API")


class RecordIn(BaseModel):
    name: str
    weight_kg: float
    height_m: float


class RecordOut(BaseModel):
    name: str
    weight_kg: float
    height_m: float
    bmi: float
    category: str
    ideal_weight: float


def to_record_out(record: Health) -> RecordOut:
    return RecordOut(
        name=record.name,
        weight_kg=record.weight_kg,
        height_m=record.height_m,
        bmi=record.calculate_bmi(),
        category=record.get_bmi_category(),
        ideal_weight=record.get_ideal_weight(),
    )


@app.get("/")
def health_check():
    return {
        "status": "ok",
        "app": "Health API",
    }


@app.get("/records", response_model=List[RecordOut])
def get_records():
    records = load_users_health_records(DATA_FILE)
    return [to_record_out(record) for record in records]


@app.post("/records", response_model=RecordOut, status_code=201)
def create_record(record: RecordIn):
    try:
        health_record = Health(
            name=record.name,
            weight_kg=record.weight_kg,
            height_m=record.height_m,
        )
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))

    records = load_users_health_records(DATA_FILE)
    records.append(health_record)
    save_users_health_records(records, DATA_FILE)

    return to_record_out(health_record)