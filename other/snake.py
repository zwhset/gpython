# -*- coding: utf-8 -*-
"""
    package.module
    ~~~~~~~~~~~~~~

    网上找的区块链的实现：

    首先将定义块将是什么样子。在区块链中，每个块都存储一个时间戳和一个索引。在SnakeCoin中，需要把两者都存储起来。为了确保整个区块链的完整性，每个块都有一个自动识别散列。与比特币一样，每个块的散列将是块索引、时间戳、数据和前块哈希的加密哈希。数据可以是你想要的任何东西。

    :copyright: (c) YEAR by zwhset.
    :license: GOMEOPS, see LICENSE_FILE for more details.
"""

import hashlib

from datetime import datetime


class Block:
    def __init__(self):
        pass

    def hash_block(self, index, timestamp, data, previous_hash):
        '''hash生成方法'''
        sha = hashlib.sha256()
        s = "{0}{1}{2}{3}".format(index, timestamp, data, previous_hash)
        sha.update(s.encode("utf8"))
        return sha.hexdigest()

    def next_block(self, last_block):
        '''下一个hash'''
        index = last_block.index + 1
        timestamp = datetime.now()
        data = "you data."
        pre_hash = last_block.hash
        return self.hash_block(index, timestamp, data, pre_hash)

    def init_block(self):
        '''源hash'''
        self.index = 0
        self.timestamp = datetime.now()
        self.data = "Genesis Block"
        self.previous_hash = "go"
        self.hash = self.hash_block(self.index, self.timestamp, self.data, self.previous_hash)
        return self.hash


if __name__ == '__main__':
    b = Block()
    s_hash = b.init_block()

    print("souce hash:\t", s_hash)
    for i in range(30):
        print("[{i}# hash]:\t".format(i=i), b.next_block(b))