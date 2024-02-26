import requests
import boto3


aws_access_key_id = ''
aws_secret_access_key = ''
aws_region = ''

s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=aws_region)


download_url = ""

save_path = "downloaded_dataset.csv"

# Send an HTTP GET request to download the file
response = requests.get(download_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    with open(save_path, "wb") as f:
        f.write(response.content)
    print(f"Dataset downloaded and saved as {save_path}")
else:
    print(f"Failed to download the dataset. Status code: {response.status_code}")

s3_bucket_name = ''
s3_object_key = ''

s3.upload_file(save_path, s3_bucket_name, s3_object_key)
