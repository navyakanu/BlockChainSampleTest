import json
from src.Block import Block


class BlockChain:
    def __init__(self):
        self.chain = [self.__create_genesis_block()]

    def __create_genesis_block(self):
        return Block(0, '201889867', 'Genesis', "0")

    def get_latest_block(self):
        return self.chain[len(self.chain)-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.get_hash()
        self.chain.append(new_block)

    def convert_to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=False, indent=4)


CHAIN = BlockChain()
CHAIN.add_block(Block(1, '20180604', 'FirstBlock'))
CHAIN.add_block(Block(2, '20180704', 'SecondBlock'))

print(CHAIN.convert_to_json())
