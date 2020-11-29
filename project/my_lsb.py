import numpy as np
from numpy import ndarray


def lsb_embed(pixels_array: ndarray, message_bits, bits_per_pixel=1):
    message_iterator = iter(message_bits)
    row_num, col_num = pixels_array.shape
    try:
        for row in range(row_num):
            for col in range(col_num):
                for i in range(bits_per_pixel):
                    bit = next(message_iterator)
                    pixel = pixels_array[row][col]
                    pixels_array[row][col] = insert_message_bit_to_pixel(pixel, bit, i)
        return pixels_array
    except StopIteration:
        return pixels_array


def insert_message_bit_to_pixel(pixel, bit, position):
    bits_list = list(np.binary_repr(pixel, width=16))
    bits_list[-1 - position] = int(bit)
    bits_string = "".join(str(x) for x in bits_list)
    new_pixel = int(bits_string, 2)
    return new_pixel


def lsb_extract(pixels_array, message_length: int, bits_per_pixel=1):
    bits = list()
    row_num, col_num = pixels_array.shape
    bits_counter = 0
    try:
        for row in range(row_num):
            for col in range(col_num):
                for i in range(bits_per_pixel):
                    if bits_counter >= message_length:
                        raise StopIteration()
                    bits.append(retrieve_bits_from_pixel(pixels_array[row][col], i))
                    bits_counter += 1
        return "".join(str(x) for x in bits)
    except StopIteration:
        return "".join(str(x) for x in bits)


def retrieve_bits_from_pixel(pixel, position):
    bits = np.binary_repr(pixel, width=16)
    bits_list = list(bits)
    return str(bits_list[-1 - position])
