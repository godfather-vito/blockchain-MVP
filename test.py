# ジェネシスブロックを作ってブロックチェーンを作成する
    # とりあえずブロックっていうのはデータスキームのインスタンスなので、リストに格納するのでいいのかなと。改竄もしたくないので、
# ブロック情報を出力
# 指定回数ループ
    # 新しいブロックをブロックチェーンに繋げる
    # 新しいブロック情報を出力

from genesis_block import gen_genesis_block
from next_block import gen_next_block


blockchain = [gen_genesis_block()]

previous_block = blockchain[0]

required_number_blocks = int(input("How many blocks do u want?:"))



