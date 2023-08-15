from typing import Optional, List


from src.model.invoice import _
from src.model.client import Client


class ClientController:
    def __init__(self, backend: Optional[str] = None) -> None:
        pass

    def get_clients(self) -> List[Client]:
        raise NotImplementedError()

    def new_client(self, **kwargs):
        raise NotImplementedError()
