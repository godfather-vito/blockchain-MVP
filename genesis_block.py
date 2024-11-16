from block import Block
import datetime

def gen_genesis_block(self):
    return Block(0, '0',
                 datetime.datetime.now(),
                 {'message':'genesis_block',
                 'PoW': 9,}, 
                 )#PoWは9で割った時の剰余が1以上の時blocknumberをインクリメントすることにしてあるので。最小の数の9を採用。



