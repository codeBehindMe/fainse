from typing import List, Optional

from src.model.client import Client
from src.model.invoice import _


class ClientController:
    def __init__(self, backend: Optional[str] = None) -> None:
        pass

    def get_clients(self) -> List[Client]:
        raise NotImplementedError()

    def new_client(self, **kwargs):
        raise NotImplementedError()
