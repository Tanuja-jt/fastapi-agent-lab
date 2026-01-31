from fastapi import FastAPI, HTTPException
from schemas import CalculationRequest, CalculationResponse

app = FastAPI(title="Calculator Agent")

@app.post("/calculate", response_model=CalculationResponse)
def calculate(data: CalculationRequest):

    if data.operation == "add":
        result = data.a + data.b

    elif data.operation == "subtract":
        result = data.a - data.b

    elif data.operation == "multiply":
        result = data.a * data.b

    elif data.operation == "divide":
        if data.b == 0:
            raise HTTPException(
                status_code=400,
                detail="Division by zero is not allowed"
            )
        result = data.a / data.b

    else:
        raise HTTPException(
            status_code=400,
            detail="Invalid operation"
        )

    return {"result": result}
