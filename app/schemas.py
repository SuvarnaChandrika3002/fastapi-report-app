from datetime import datetime
from pydantic import BaseModel

class CalculationCreate(BaseModel):
    operand1: float
    operand2: float
    operation: str

class CalculationRead(BaseModel):
    id: int
    operand1: float
    operand2: float
    operation: str
    result: float
    created_at: datetime

    class Config:
        from_attributes = True  

class ReportMetrics(BaseModel):
    total_calculations: int
    average_result: float | None
    sum_results: float
    operation_counts: dict[str, int]
