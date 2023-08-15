# mongodb backend
from src.backend.backend import Backend

class MongoDBBackend(Backend):
    
    def __init__(self) -> None:
        super().__init__()

    def get_clients(self):
        return super().get_clients()

    def new_client(self):
        return super().new_client()