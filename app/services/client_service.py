from app.repository.client_repository import ClientRepository
from app.models.client import Client

class ClientService:
    def __init__(self, client_repository: ClientRepository):
        self.client_repository = client_repository

    def get_all_clients(self) -> list[Client]:
        return self.client_repository.get_all()

    def add_client(self, name: str, national_id: str) -> Client:
        client = Client(name=name, national_id=national_id)
        return self.client_repository.add(client)
