# mongodb backend
import datetime
from copy import deepcopy
from dataclasses import asdict
from typing import Any, Dict, List

import pymongo
from pymongo import MongoClient
from pymongo.collection import Collection

from src.backend.backend import Backend
from src.model.client import Client
from src.model.invoice import Invoice

APP_DATABASE_NAME = "fainse"


class MongoDBBackend(Backend):
    def __init__(
        self, host, port, username, password, app_database_name=APP_DATABASE_NAME
    ) -> None:
        super().__init__()
        self.host = host
        self.port = port
        self.mongo_client = MongoClient(
            host=host, port=port, username=username, password=password
        )
        self.db = self.mongo_client[app_database_name]
        self.clients_collection = self.db.clients
        self.invoices_collection = self.db.invoices

    def __del__(self):
        self.mongo_client.close()

    @staticmethod
    def _get_max_value_of_field(collection: Collection, field_name: str) -> Any:
        res = collection.find_one(sort=[(field_name, pymongo.DESCENDING)])
        if res is None:
            return 0
        else:
            return res[field_name]

    @classmethod
    def _auto_increment_field(cls, collection: Collection, field_name: str) -> int:
        last_id = cls._get_max_value_of_field(collection, field_name)
        return last_id + 1

    def get_clients(self) -> List[str]:
        clients = self.db.clients
        for client in clients.find():
            yield client.clientName

    def new_client(self, client: Client) -> Client:
        clients_collection = self.db.clients

        _client = deepcopy(client)
        _client.clientNumber = self._auto_increment_field(
            clients_collection, "clientNumber"
        )
        clients_collection.insert_one(asdict(_client))
        return _client

    def get_invoice_by_id(self):
        raise NotImplementedError()

    def update_invoice(self, invoice: Invoice):
        # Need to appropriately handle this
        if invoice.invoiceId is None:
            raise ValueError("cannot update invoice with empty invoiceId")
        _res: Dict = self.invoices_collection.find_one({"invoiceId": invoice.invoiceId})

        if _res is None:
            raise ValueError(
                f"could not find any invoices for invoiceId: {invoice.invoiceId}"
            )

        for k, v in asdict(invoice).items():
            _res[k] = v

        # FIXME: Change with update_one.
        self.invoices_collection.delete_one({"invoiceId": invoice.invoiceId})
        self.invoices_collection.insert_one(_res)

    def new_invoice(self, invoice: Invoice):
        invoices_collection = self.db.invoices

        _invoice = deepcopy(invoice)

        # We have to increment the invoice number for each invoice per client.
        _res = invoices_collection.find_one(
            {"clientId": _invoice.clientId},
            sort=[("invoiceNumber", pymongo.DESCENDING)],
        )
        if _res is None:
            _invoice.invoiceNumber = 1
        else:
            _invoice.invoiceNumber = _res["invoiceNumber"] + 1
