# Blockchain-in-Real-Estate
A Python-based blockchain for secure real estate management. It records property transactions, verifies ownership history with cryptographic hashes, and ensures transparency and tamper-proof records for property management.

## 🚀 Features
- Add property transactions with **seller, buyer, and price**  
- Mine blocks using **Proof of Work** with SHA-256 hashing  
- View the **entire blockchain** in JSON format  
- **Validate blockchain** integrity for security  
- Command-line **interactive menu**

## 🛠️ Tech Stack
- **Python 3**  
- **Hashlib** for cryptographic hashing  
- **JSON** for data representation

## ⚡ How It Works
1. **Transactions** are added to a pending list with property details.  
2. **Blocks** are mined using a Proof-of-Work algorithm to secure transactions.  
3. Each block stores:
   - Index and timestamp  
   - List of confirmed transactions  
   - Previous block's hash  
   - Current block’s hash and nonce  

4. **Blockchain Validation** checks the integrity of each block and the chain.  

## 📥 Installation & Usage
1. **Clone the repository:**
```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

2. **Run the program:**
```bash
python real_estate_blockchain.py
```

