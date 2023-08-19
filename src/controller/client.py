from typing import List, Optional

from src.model.client import Client
from src.backend.backend import Backend
import src.utils.misc as misc_utils


class ClientController:
    def __init__(self, backend: Backend) -> None:
        self.backend = backend

    @staticmethod
    def _generate_client_id() -> str:
        return misc_utils.hex_id_time_ms()

    def get_clients(self) -> List[Client]:
        raise NotImplementedError()

    def new_client(
        self,
        clientName: str,
        contactName: str,
        emailAddress: str,
        address: Optional[str] = None,
    ):
        client = Client(
            clientId=self._generate_client_id(),
            clientName=clientName,
            contactName=contactName,
            emailAddress=emailAddress,
            addressStr=address
        )

        self.backend.new_client(client=client)
