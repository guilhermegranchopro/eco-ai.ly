from polars import DataFrame
from fastapi import FastAPI

# Create FastAPI app
app = FastAPI()

# Define a "Hello, World!" endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, Pedro!"}

