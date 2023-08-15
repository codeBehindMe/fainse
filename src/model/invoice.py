from dataclasses import dataclass
from datetime import _Date, datetime
from typing import Optional


@dataclass
class IssuedTo:
    contactName: Optional[str]
    businessName: str
    emailAddress: str
    addressStr: Optional[str]


@dataclass
class BankDetails:
    accountName: str
    accountNumber: int
    bsb: str


@dataclass
class Invoice:
    clientName: str
    invoiceId: str
    issuedTo: IssuedTo
    issuedDate: _Date
    total: float
    gstRate: str
    gst: float
    amountDue: float
    invoiceDue: _Date
    bankDetails: BankDetails
