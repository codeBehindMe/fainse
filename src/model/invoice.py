from dataclasses import dataclass
from typing import List, Optional

from src.model.client import Client


@dataclass
class BankDetails:
    accountName: str
    accountNumber: int
    bsb: str


@dataclass
class LineItem:
    itemNumber: int
    itemDescription: str
    unitPrice: float
    quantity: float
    total: float


@dataclass
class Invoice:
    clientId: int
    clientName: str
    issuedTo: Client
    issuedDate: str
    lineItems: List[LineItem]
    total: float
    gstRate: str
    gst: float
    amountDue: float
    invoiceDue: str
    bankDetails: BankDetails
    recieved: bool
    paymentRecievedDate: Optional[str] = None
    invoiceId: Optional[str] = None
    invoiceNumber: Optional[int] = None
