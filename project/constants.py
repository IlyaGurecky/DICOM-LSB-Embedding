from datetime import datetime

# Max - 16 (Uint16)
BITS_PER_PIXEL = 3
RESULT_FILE = 'EС-{0}||{1}.dcm'.format(datetime.now().strftime('%d.%m.%Y|%H:%M:%S'), BITS_PER_PIXEL)
RESULT_PATH = '../results/{0}'.format(RESULT_FILE)
DICOM_TAG_BLOCK = 0x0041
DICOM_TAG_ID = 0x01
DICOM_TAG_NAME = 'MSG'
