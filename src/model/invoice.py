from dataclasses import dataclass
from datetime import _Date 
from typing import Optional

from src.model.client import Client


@dataclass
class BankDetails:
    accountName: str
    accountNumber: int
    bsb: str


@dataclass
class Invoice:
    clientName: str
    invoiceId: str
    issuedTo: Client
    issuedDate: _Date
    total: float
    gstRate: str
    gst: float
    amountDue: float
    invoiceDue: _Date
    bankDetails: BankDetails
    recieved: bool
    paymentRecievedDate: Optional[_Date]
