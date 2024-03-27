# -*- coding: UTF-8 -*- #
"""
@filename:test_calculation.py
@author:wdh
@time:2024-01-15
"""

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_calculate():
    response = client.post("/calculate", json={"value": 5})
    assert response.status_code == 200
    assert response.json() == {"result": 25}