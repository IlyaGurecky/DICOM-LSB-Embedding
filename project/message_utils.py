import bitarray


def encode_message_to_bits(message):
    ba = bitarray.bitarray()
    ba.frombytes(message.encode('utf-8'))
    return ba


def decode_bits_to_message(bit_array_string):
    return bitarray.bitarray(bit_array_string).tobytes().decode('utf-8')
