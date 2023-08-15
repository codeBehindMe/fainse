# google cloud datastore backend


class GCDatastoreBackend:
    def __init__(self) -> None:
        pass

    def get_clients(self):
        raise NotImplementedError()

    def new_client(self):
        raise NotImplementedError()

    def get_invoice(self):
        raise NotImplementedError()

    def update_invoice(self):
        raise NotImplementedError()

    def generate_invoice(self):
        raise NotImplementedError()
