# -*- coding: UTF-8 -*- #
"""
@filename:calculation.py
@author:wdh
@time:2024-01-15
"""


from fastapi import APIRouter
from ...schemas import CalculationInput, CalculationResult,Person
from ...utils import calculator
from .opt_demo import init_table
router = APIRouter()

@router.post("/calculate", response_model=CalculationResult)
async def perform_calculation(input: CalculationInput) -> CalculationResult:
    result = calculator.complex_calculation(input.value)
    return CalculationResult(result=result)

@router.get("/get_info", response_model=Person)
async def perform_calculation() -> Person:
    # result = calculator.complex_calculation()
    p_info = {
        "id":123,
        "username": "Foo",
        "age": 20
    }
    return p_info

@router.get("/get_test")
async def perform_calculation() -> Person:
    # result = calculator.complex_calculation()
    p_info = {
        "id":123,
        "username": "Foo",
        "age": 20
    }
    return Person(**p_info)



@router.get("/create_test")
async def perform_calculation() :
    # result = calculator.complex_calculation()
    print(123)
    return 123



