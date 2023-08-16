from abc import ABC, abstractmethod
from typing import List


class Backend(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def get_clients(self) -> List[str]:
        raise NotImplementedError()

    @abstractmethod
    def new_client(self):
        raise NotImplementedError()

    @abstractmethod
    def get_invoice(self):
        raise NotImplementedError()

    @abstractmethod
    def update_invoice(self):
        raise NotImplementedError()

    @abstractmethod
    def generate_new_invoice(self):
        raise NotImplementedError()
