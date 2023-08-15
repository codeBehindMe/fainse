from dataclasses import dataclass
from typing import Optional


@dataclass
class Client:
    clientId: int
    clientName: str
    contactName: str
    emailAddress: str
    addressStr: Optional[str]
