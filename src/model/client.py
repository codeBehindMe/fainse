from dataclasses import dataclass
from typing import Optional


@dataclass
class Client:
    clientId: Optional[int] = None
    clientName: str
    contactName: str
    emailAddress: str
    addressStr: Optional[str] = None
