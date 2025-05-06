from fastapi import FastAPI
from src.webserver.constants import *
from pydantic import BaseModel
import logging
import os
from dotenv import load_dotenv
from src.backend.backend import generate_itinerary

# Load environment variables from .env file
load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class RequestPayload(BaseModel):
    model: str
    prompt: str
    images: list[str]
    session_id: str

# Initialize the FastAPI app
app = FastAPI(
    title="LLM inference API",
    description="API for LLM inference",
    version="0.1",
)

@app.get("/")
def read_root():
    """ Root endpoint to check if the server is running."""
    return {"version": os.getenv("WEB_SERVER_VERSION")}

@app.post("/api/generate")
def generate_response(request: RequestPayload):
    """Generate a response from the LLM model."""
    logging.info(f"Received request: {request}")    
    response = generate_itinerary()
    return {"response": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.webserver.server:app", host="0.0.0.0", port=8000, reload=False)