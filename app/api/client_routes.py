from fastapi import APIRouter, Depends, HTTPException, Body
from sqlmodel import Session
from app.api.dependencies import get_client_service
from app.models.client import Client
from app.services.client_service import ClientService
from typing import List

router = APIRouter()

@router.get("/clients", response_model=List[Client])
def list_clients(client_service: ClientService = Depends(get_client_service)):
    return client_service.get_all_clients()

@router.post("/clients", response_model=Client)
def add_client(name: str, national_id: str, client_service: ClientService = Depends(get_client_service)):
    try:
        created_client = client_service.add_client(name=name, national_id=national_id)
        return created_client
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
