from collections import Counter
from typing import List

from sqlalchemy.orm import Session

from . import models, schemas

VALID_OPERATIONS = {"+", "-", "*", "/", "^"}  


def perform_calculation(operand1: float, operand2: float, operation: str) -> float:
    """Pure calculation logic (unit-test this)."""
    if operation not in VALID_OPERATIONS:
        raise ValueError("Unsupported operation")

    if operation == "+":
        return operand1 + operand2
    if operation == "-":
        return operand1 - operand2
    if operation == "*":
        return operand1 * operand2
    if operation == "/":
        if operand2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return operand1 / operand2
    if operation == "^":
        return operand1 ** operand2

    
    raise ValueError("Invalid operation")


def create_calculation(db: Session, calc_in: schemas.CalculationCreate) -> models.Calculation:
    """Perform calc, persist to DB, return ORM object."""
    result = perform_calculation(calc_in.operand1, calc_in.operand2, calc_in.operation)

    db_obj = models.Calculation(
        operand1=calc_in.operand1,
        operand2=calc_in.operand2,
        operation=calc_in.operation,
        result=result,
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_calculation_history(db: Session, limit: int = 20) -> List[models.Calculation]:
    """Return latest calculations."""
    return (
        db.query(models.Calculation)
        .order_by(models.Calculation.created_at.desc())
        .limit(limit)
        .all()
    )


def get_report_metrics(db: Session) -> schemas.ReportMetrics:
    """Aggregate stats from all calculations."""
    rows: List[models.Calculation] = db.query(models.Calculation).all()
    total = len(rows)

    if total == 0:
        return schemas.ReportMetrics(
            total_calculations=0,
            average_result=None,
            sum_results=0.0,
            operation_counts={},
        )

    sum_results = sum(row.result for row in rows)
    avg = sum_results / total

    op_counts = Counter(row.operation for row in rows)

    return schemas.ReportMetrics(
        total_calculations=total,
        average_result=avg,
        sum_results=sum_results,
        operation_counts=dict(op_counts),
    )
