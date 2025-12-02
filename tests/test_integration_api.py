from fastapi.testclient import TestClient

from app.main import app
from app.database import Base, engine


Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

client = TestClient(app)


def test_calculate_endpoint_creates_record_and_returns_result():
    payload = {"operand1": 2, "operand2": 3, "operation": "+"}
    response = client.post("/api/calculate", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["result"] == 5
    assert data["operation"] == "+"


def test_history_returns_recent_calculations():
    
    payload = {"operand1": 1, "operand2": 1, "operation": "+"}
    client.post("/api/calculate", json=payload)

    response = client.get("/api/history?limit=10")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1
    assert "result" in data[0]


def test_report_returns_metrics():
    
    client.post("/api/calculate", json={"operand1": 2, "operand2": 2, "operation": "*"})
    client.post("/api/calculate", json={"operand1": 10, "operand2": 2, "operation": "/"})

    response = client.get("/api/report")
    assert response.status_code == 200
    data = response.json()
    assert data["total_calculations"] >= 2
    assert "sum_results" in data
    assert "average_result" in data
    assert isinstance(data["operation_counts"], dict)
