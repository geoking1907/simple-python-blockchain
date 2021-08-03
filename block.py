import hashlib

class TestBlock:

    def __init__(self, previous_hash, transactions):
        self.previous_hash = previous_hash
        self.transactions = transactions

        self.data = " - ".join(transactions) + " - " + previous_hash
        self.hash = hashlib.sha256(self.data.encode()).hexdigest()
