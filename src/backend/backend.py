from abc import ABC, abstractmethod
from typing import List

from src.model.client import Client
from src.model.invoice import Invoice


class Backend(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def get_clients(self) -> List[str]:
        raise NotImplementedError()

    @abstractmethod
    def new_client(self, client: Client) -> Client:
        raise NotImplementedError()

    @abstractmethod
    def get_invoice_by_id(self, invoiceId: str) -> Invoice:
        raise NotImplementedError()

    @abstractmethod
    def update_invoice(self, invoice: Invoice):
        raise NotImplementedError()

    @abstractmethod
    def new_invoice(self, invoice: Invoice):
        raise NotImplementedError()
