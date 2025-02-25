import os
from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel
import httpx
import uvicorn
from typing import Optional, List, Dict, Any
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI
app = FastAPI(
    title="Ollama API",
    description="A FastAPI server that connects to Ollama for LLM inference",
    version="1.0.0"
)

# Environment variables
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

# Models
class GenerationRequest(BaseModel):
    prompt: str
    model: str
    system: Optional[str] = None
    template: Optional[str] = None
    context: Optional[List[int]] = None
    options: Optional[Dict[str, Any]] = None
    stream: Optional[bool] = False
    raw: Optional[bool] = False

class ChatMessage(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    model: str
    messages: List[ChatMessage]
    stream: Optional[bool] = False
    options: Optional[Dict[str, Any]] = None

# Routes
@app.get("/")
async def root():
    return {"message": "Ollama API Gateway is running"}

@app.get("/models")
async def list_models():
    """List all available models in Ollama"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{OLLAMA_BASE_URL}/api/tags")
            if response.status_code != 200:
                raise HTTPException(status_code=response.status_code, detail=f"Error from Ollama: {response.text}")
            return response.json()
    except Exception as e:
        logger.error(f"Error listing models: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to connect to Ollama: {str(e)}")

@app.post("/generate")
async def generate(request: GenerationRequest):
    """Generate text using a specified model"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{OLLAMA_BASE_URL}/api/generate",
                json=request.dict(exclude_none=True)
            )
            if response.status_code != 200:
                raise HTTPException(status_code=response.status_code, detail=f"Error from Ollama: {response.text}")
            return response.json()
    except Exception as e:
        logger.error(f"Error generating text: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to connect to Ollama: {str(e)}")

@app.post("/chat")
async def chat(request: ChatRequest):
    """Chat with a specified model"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{OLLAMA_BASE_URL}/api/chat",
                json=request.dict(exclude_none=True)
            )
            if response.status_code != 200:
                raise HTTPException(status_code=response.status_code, detail=f"Error from Ollama: {response.text}")
            return response.json()
    except Exception as e:
        logger.error(f"Error in chat: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to connect to Ollama: {str(e)}")

@app.get("/health")
async def health_check():
    """Check if Ollama is running"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{OLLAMA_BASE_URL}")
            return {"status": "healthy" if response.status_code == 200 else "unhealthy"}
    except Exception as e:
        logger.error(f"Health check failed: {str(e)}")
        return {"status": "unhealthy", "error": str(e)}

if __name__ == "__main__":
    port = int(os.getenv("PORT", "8000"))
    host = os.getenv("HOST", "0.0.0.0")
    uvicorn.run("main:app", host=host, port=port, reload=True)