# DICOM LSB Embedding

This tool designed for embedding some text to **DICOM** files using **LSB** method with configurable multiplexing

## Short Manual

1. Check and set your config some config parameters to [constants.py](https://github.com/IlyaGurecky/DICOM-LSB-Embedding/blob/main/project/constants.py)
    - BITS_PER_PIXEL - how many message bits will be embedded in the least significant bits of each pixel
    - RESULT_FILE - some template for new DICOM file name
    - DICOM_TAG_BLOCK - DICOM tag group name
    - DICOM_TAG_ID - tag id
    - DICOM_TAG_NAME - tag creator name

2. Set your message to MESSAGE var and your DICOM file name in /recources/ folder

3. Run [main_embed.py](https://github.com/IlyaGurecky/DICOM-LSB-Embedding/blob/main/project/main_embed.py)

4. Get new DICOM container name from /results/ folder

5. Set this name to CONTAINER_NAME var in [main_extract.py](https://github.com/IlyaGurecky/DICOM-LSB-Embedding/blob/main/project/main_extract.py) and run this .py file