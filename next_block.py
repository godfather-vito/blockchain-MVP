from block import Block
import datetime


def gen_next_block(last_block):
    current_index = last_block.index + 1
    current_timestamp = datetime.datetime.now()
    current_data = 'Oh yeah! This is ' + str(current_index)
    previous_hash = last_block.hash
    return Block(current_index, current_timestamp, current_data, previous_hash)