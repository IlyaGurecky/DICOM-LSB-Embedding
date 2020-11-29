import pydicom
import matplotlib.pyplot as plt
import project.constants as const
from project.my_lsb import lsb_embed
from project.message_utils import encode_message_to_bits
from project.utils import calculate_max_message_length, validate_image_and_message_size

# ------------------- INITIALIZE PARAMS AND ENCODE MESSAGE-------------------

MESSAGE = 'Test Message'
FILENAME = 'test'
PATH = '../resources/{0}'.format(FILENAME)

messageBitArray = encode_message_to_bits(MESSAGE)
messageBitLength = len(messageBitArray)

print('\nMessage bits:')
print(messageBitArray, '\n')

print('Message bits length:')
print(messageBitLength, '\n')

# ------------------------------ WORK WITH DICOM ----------------------------

dicom = pydicom.dcmread(PATH)

print('DICOM pixels:')
print(dicom.pixel_array, dicom.pixel_array.shape, '\n')

print('DICOM pixels quantity:')
pixels_quantity = dicom.pixel_array.shape[0] * dicom.pixel_array.shape[1]
print(pixels_quantity)

print('\nMax message length in symbols:')
en, ru = calculate_max_message_length(pixels_quantity, const.BITS_PER_PIXEL)
print('EN: {0}, RU: {1}'.format(en, ru))

plt.imshow(dicom.pixel_array, cmap='gray')
plt.show()

validate_image_and_message_size(pixels_quantity, const.BITS_PER_PIXEL, messageBitLength)

new_pixels = lsb_embed(dicom.pixel_array, messageBitArray, const.BITS_PER_PIXEL)

dicom.PixelData = new_pixels.tobytes()
dicom.Rows, dicom.Columns = new_pixels.shape

plt.imshow(new_pixels, cmap='gray')
plt.show()

tag_block = dicom.private_block(const.DICOM_TAG_BLOCK, const.DICOM_TAG_NAME, create=True)
tag_block.add_new(const.DICOM_TAG_ID, 'LO', str(messageBitLength))

dicom.save_as(const.RESULT_PATH)
