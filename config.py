import os
import boto3
from dotenv import load_dotenv

load_dotenv()
# AWS S3 credentials and bucket name
S3_BUCKET = "poc-data-kadaster"
s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))

KEY_PREFIX = 'io/export/'  # Folder path without 's3://'
KEY_PREFIX1 = 'io/Results/' # Folder path without 's3://'

# Configuration Constants
BASE_DIR = KEY_PREFIX
# output=r'D:\DATA\OUTPUT_DATA_EXTRACTION'
output=KEY_PREFIX1
# IN_DIR = os.path.join(BASE_DIR, 'Json Files')
OUT_DIR_LINE_MASK = os.path.join(output, 'Line')
OUT_DIR_TEXT_BOX = os.path.join(output, 'Manual')
OUT_DIR_TEXT_BOX2 = os.path.join(output, 'Detected')
OUT_DIR_OCR = os.path.join(output, 'ocr_output')
