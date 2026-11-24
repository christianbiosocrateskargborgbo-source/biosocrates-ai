# BioSocrate AI + QLBD
# Quantum Ledger Blockchain Database
# Built by Christian Bio Socrates Kargbo

import hashlib
import time
import json

class QLBD:
    def __init__(self):
        self.chain = []
        self.create_block("GENESIS - BioSocrate AI Started")

    def create_block(self, data):
        block = {
            "index": len(self.chain) + 1,
            "time": time.time(),
            "data": data,
            "prev_hash": self.chain[-1]["hash"] if self.chain else "0",
        }
        block["hash"] = hashlib.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest()
        self.chain.append(block)
        return block

    def show(self):
        for b in self.chain:
            print(f"Block {b['index']}: {b['data']} | Hash: {b['hash'][:12]}...")

# BioSocrate AI Brain
def biosocrate_ai(question):
    q = question.lower()
    if "who are you" in q:
        return "I am BioSocrate AI + QLBD. Secret AI built by Boss!"
    if "token" in q:
        return "Tokens are LIVE and WORKING. No stress!"
    if "playstore" in q:
        return "Playstore na our Playground. We go showcase apps there!"
    if "qlbd" in q:
        return "QLBD = Quantum Ledger Blockchain Database. Safe, Fast, No thief!"
    return "Boss, I hear you. We go build am together with QLBD!"

# RUN
if __name__ == "__main__":
    db = QLBD()
    db.create_block("User: Tokens Live")
    db.create_block("User: Build Apps for Playstore")
    db.show()
    print("\n--- BioSocrate AI ---")
    print(biosocrate_ai("Who are you?"))
    print(biosocrate_ai("What is QLBD?"))