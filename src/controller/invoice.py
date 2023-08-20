import src.utils.misc as misc_utils
from src.backend.backend import Backend
from src.model.invoice import Invoice, LineItem


class InvoiceController:
    def __init__(self, backend: Backend) -> None:
        self.backend = backend

    @staticmethod
    def _generate_invoice_id() -> str:
        return misc_utils.hex_id_time_ms()

    def get_invoices(self, clientId: str) -> [Invoice]:
        raise NotImplementedError()

    def new_invoice(self, invoice: Invoice) -> Invoice:
        self.backend.new_invoice(invoice=invoice)

    def update_invoice(self, invoice: Invoice) -> bool:
        self.backend.update_invoice(invoice)

    def add_line_item(self, invoiceId: str, li: LineItem) -> bool:
        invoice = self.backend.get_invoice_by_id(invoiceId)
        invoice.lineItems.append(li)
        self.update_invoice(invoice)
