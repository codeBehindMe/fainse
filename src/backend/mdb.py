# mongodb backend
from dataclasses import asdict
from typing import Any, List
from copy import deepcopy

import pymongo
from pymongo import MongoClient
from pymongo.collection import Collection

from src.backend.backend import Backend
from src.model.client import Client

APP_DATABASE_NAME = "fainse"


class MongoDBBackend(Backend):
    def __init__(self, host, port, username, password) -> None:
        super().__init__()
        self.host = host
        self.port = port
        self.mongo_client = MongoClient(
            host=host, port=port, username=username, password=password
        )
        self.db = self.mongo_client[APP_DATABASE_NAME]

    @staticmethod
    def _get_max_value_of_field(collection: Collection, field_name: str) -> Any:
        res = collection.find_one(sort=[(field_name, pymongo.DESCENDING)])
        if res is None:
            return 1
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

    def new_client(self, client: Client):
        clients_collection = self.db.clients

        _client = deepcopy(client)
        _client.clientId = self._auto_increment_field(clients_collection,"clientId")
        clients_collection.insert_one(asdict(_client))

    def get_invoice(self):
        return super().get_invoice()

    def update_invoice(self):
        return super().update_invoice()

    def generate_new_invoice(self):
        return super().generate_new_invoice()
