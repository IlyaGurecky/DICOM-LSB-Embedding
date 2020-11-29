def calculate_max_message_length(pixels_quantity: int, bits_per_pixel: int):
    en = pixels_quantity * bits_per_pixel / 8
    ru = pixels_quantity * bits_per_pixel / 16
    return int(en), int(ru)


def validate_image_and_message_size(pixels_quantity, bits_per_pixel, message_bit_length):
    if pixels_quantity * bits_per_pixel < message_bit_length:
        raise Exception('Message is too big for this image:(')
