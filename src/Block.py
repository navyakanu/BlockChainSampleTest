import hashlib


class Block:

    def __init__(self, index, time_stamp, data, previous_hash=None):
        self.index = index
        self.time_stamp = time_stamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.get_hash()

    def get_hash(self):
        hash_value = hashlib.sha256(str([self.index,
                                         self.data,
                                         self.time_stamp,
                                         self.previous_hash]).encode('utf-8'))
        return hash_value.hexdigest()

# value1 = Block(1,'201978567','ABC','')
# value2 = Block(2,'201967908','BCD',value1.hash)
