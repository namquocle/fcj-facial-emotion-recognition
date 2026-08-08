import os
import boto3
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def test_connections():
    region = os.environ.get('AWS_REGION', 'ap-southeast-1')
    print("Checking environment variables...")
    print(f"AWS_REGION: {region}")
    print(f"S3_BUCKET_NAME: {os.environ.get('S3_BUCKET_NAME')}")
    print(f"DYNAMODB_TABLE_NAME: {os.environ.get('DYNAMODB_TABLE_NAME')}")
    print(f"AWS_ACCESS_KEY_ID: {os.environ.get('AWS_ACCESS_KEY_ID', '')[:8]}... (length: {len(os.environ.get('AWS_ACCESS_KEY_ID', ''))})")
    
    # 1. Test S3
    try:
        s3 = boto3.client('s3', region_name=region)
        bucket = os.environ.get('S3_BUCKET_NAME')
        print(f"\n1. Testing S3 connection to bucket '{bucket}'...")
        s3.head_bucket(Bucket=bucket)
        print("   S3 Bucket connection successful! [OK]")
    except Exception as e:
        print(f"   S3 Error: {e} [FAILED]")

    # 2. Test DynamoDB
    try:
        ddb = boto3.client('dynamodb', region_name=region)
        table = os.environ.get('DYNAMODB_TABLE_NAME', 'FaceEmotionLogs')
        print(f"\n2. Testing DynamoDB connection to table '{table}'...")
        ddb.describe_table(TableName=table)
        print("   DynamoDB Table connection successful! [OK]")
    except Exception as e:
        print(f"   DynamoDB Error: {e} [FAILED]")

    # 3. Test Rekognition
    try:
        rek = boto3.client('rekognition', region_name=region)
        print("\n3. Testing Amazon Rekognition service availability...")
        rek.list_collections(MaxResults=1)
        print("   Rekognition Service connection successful! [OK]")
    except Exception as e:
        print(f"   Rekognition Error: {e} [FAILED]")

if __name__ == "__main__":
    test_connections()
