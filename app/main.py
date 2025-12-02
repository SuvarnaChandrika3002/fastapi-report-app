from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

from . import models, schemas, crud
from .database import engine, SessionLocal, Base


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Calculator with History & Report")


templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/api/calculate", response_model=schemas.CalculationRead)
def calculate(calc_in: schemas.CalculationCreate, db: Session = Depends(get_db)):
    try:
        calc = crud.create_calculation(db, calc_in)
    except ZeroDivisionError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return calc


@app.get("/api/history", response_model=list[schemas.CalculationRead])
def history(limit: int = 20, db: Session = Depends(get_db)):
    return crud.get_calculation_history(db, limit=limit)


@app.get("/api/report", response_model=schemas.ReportMetrics)
def report(db: Session = Depends(get_db)):
    return crud.get_report_metrics(db)
