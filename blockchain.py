import hashlib
import json
import time

class RealEstateBlockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.create_block(previous_hash="0")  # Genesis block

    def create_block(self, previous_hash):
        block = {
            "index": len(self.chain) + 1,
            "timestamp": time.time(),
            "transactions": self.pending_transactions,
            "previous_hash": previous_hash,
            "hash": "",
            "nonce": 0
        }
        block["hash"] = self.proof_of_work(block)
        self.pending_transactions = []
        self.chain.append(block)
        return block

    def add_property_transaction(self, property_id, seller, buyer, price):
        self.pending_transactions.append({
            "property_id": property_id,
            "seller": seller,
            "buyer": buyer,
            "price": price,
            "timestamp": time.time()
        })

    def proof_of_work(self, block, difficulty=3):
        prefix = "0" * difficulty
        while True:
            block_str = json.dumps(block, sort_keys=True).encode()
            hash_val = hashlib.sha256(block_str).hexdigest()
            if hash_val.startswith(prefix):
                return hash_val
            block["nonce"] += 1

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            prev = self.chain[i - 1]
            curr = self.chain[i]
            if curr["previous_hash"] != prev["hash"]:
                return False
            if curr["hash"] != self.hash_block(curr):
                return False
        return True

    @staticmethod
    def hash_block(block):
        block_copy = block.copy()
        block_copy["hash"] = ""
        return hashlib.sha256(json.dumps(block_copy, sort_keys=True).encode()).hexdigest()


# ----------- INTERACTIVE USAGE -----------
if __name__ == "__main__":
    blockchain = RealEstateBlockchain()

    print("\nWelcome to the Real Estate Blockchain System")
    while True:
        print("\nOptions:")
        print("1. Add new property transaction")
        print("2. Mine a new block")
        print("3. View blockchain")
        print("4. Validate blockchain")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            property_id = input("Enter Property ID: ").strip()
            seller = input("Enter Seller Name: ").strip()
            buyer = input("Enter Buyer Name: ").strip()
            price = float(input("Enter Price: ").strip())
            blockchain.add_property_transaction(property_id, seller, buyer, price)
            print("\nTransaction added to pending list.")

        elif choice == "2":
            if blockchain.pending_transactions:
                blockchain.create_block(blockchain.chain[-1]["hash"])
                print("\nBlock mined and added to the chain.")
            else:
                print("\nNo pending transactions to mine.")

        elif choice == "3":
            print("\n--- Blockchain ---")
            print(json.dumps(blockchain.chain, indent=4))

        elif choice == "4":
            print("\nBlockchain valid?" , blockchain.is_chain_valid())

        elif choice == "5":
            print("\nExiting... Goodbye!")
            break

        else:
            print("\nInvalid choice, try again.")
