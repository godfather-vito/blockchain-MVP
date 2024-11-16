import hashlib

class Block:
    def __init__(self, index, previous_hash, timestamp, data):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = hash()

    def hash(self):
        hasher = hashlib.sha256()
        hasher.update(str(self.index)+
                      str(self.timestamp)+
                      str(self.data)+
                      str(self.previous_hash).encode('UTF-8'))
        return hasher.hexdigest()
    



# ブロックの中に入れるものってなんだっけ
# ブロックのindex, previous_hash, timestamp, data