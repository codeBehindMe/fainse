import pymongo
import pytest

from src.backend.mdb import MongoDBBackend
from src.model.client import Client

_MONGO_TEST_CONN = {
    "host": "localhost",
    "port": 27017,
    "username": "root",
    "password": "root",
}

_MONGO_TEST_DB_NAME = "TEST_FAINSE"


@pytest.fixture(scope="class")
def setup_database() -> pymongo.MongoClient:
    """
    Drops the database and creates it again so that it's clean each time
    """
    mongo_client = pymongo.MongoClient(**_MONGO_TEST_CONN)
    if _MONGO_TEST_DB_NAME in mongo_client.list_database_names():
        mongo_client.drop_database(_MONGO_TEST_DB_NAME)
    yield mongo_client
    mongo_client.close()


@pytest.mark.usefixtures("setup_database")
class TestMongoDBBackend:
    @pytest.mark.order(1)
    def test_instantiate_database(self):
        mdb = MongoDBBackend(**_MONGO_TEST_CONN, app_database_name=_MONGO_TEST_DB_NAME)

    def test_create_client_format_one(self, setup_database: pymongo.MongoClient):
        mdb = MongoDBBackend(**_MONGO_TEST_CONN, app_database_name=_MONGO_TEST_DB_NAME)
        c = Client(
            clientId=None,
            clientName="testClient",
            contactName="testContact",
            emailAddress="testAddress",
            addressStr="testAddress",
        )

        res_client = mdb.new_client(c)
        db_res = setup_database[_MONGO_TEST_DB_NAME].clients.find_one(
            {"clientId": res_client.clientId}
        )
        assert db_res["clientName"] == res_client.clientName
