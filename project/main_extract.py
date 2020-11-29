import pydicom
import project.constants as const
from project.my_lsb import lsb_extract
from project.message_utils import decode_bits_to_message

CONTAINER_NAME = 'EС-29.11.2020|22:36:12||3.dcm'
CONTAINER_PATH = '../results/{0}'.format(CONTAINER_NAME)

dicom_container = pydicom.dcmread(CONTAINER_PATH)

length_tag = dicom_container.get_private_item(const.DICOM_TAG_BLOCK, const.DICOM_TAG_ID, const.DICOM_TAG_NAME).value

msg_length = int(length_tag)

message_bits = lsb_extract(dicom_container.pixel_array, msg_length, const.BITS_PER_PIXEL)

decoded_message = decode_bits_to_message(message_bits)

print('\nDECODED MESSAGE:')
print(decoded_message)
