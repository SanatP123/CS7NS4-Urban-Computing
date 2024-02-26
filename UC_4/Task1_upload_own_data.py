


#import requests and csv to request API data and csv to store the data
import requests
import csv
import boto3

# Configure your AWS credentials


def upload_own_data():
    aws_access_key_id = ''
    aws_secret_access_key = ''
    aws_region = ''
        
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=aws_region)


    url = "https://data.smartdublin.ie/dublinbikes-api/last_snapshot/"

    no_of_entries = 1000

    #list to save the entries retrieved
    all = []

    cnt = 0

    #100 entries will be retrieved at a time
    page_size = 100

    total_pages = (no_of_entries + page_size - 1) // page_size

    column_names = []

    for i in range(total_pages):
        parameters = {
            "page": i + 1,
            "page_size": page_size
        }
        # GET Request to the url with parameters
        response = requests.get(url, params=parameters)
        # Succesful if the response is 201
        if response.status_code == 201:
            data = response.json()

            if not column_names and data:
                column_names = data[0].keys()

            all.extend(data)
            cnt += len(data)

            if cnt >= no_of_entries:
                break
        # Failed to retrieve data if code isn't 201 For exapmle: 500 - Internal server error    
        else:
            print(f"Failed to retrieve data for page {i + 1}. Status code: {response.status_code}")


    csv_filename = "UC_4/dublinbikes.csv"


    with open(csv_filename, mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=column_names)

        writer.writeheader()
        for entry in all:
            writer.writerow(entry)

    s3_bucket_name = ''
    s3_object_key = 'Real-time code/dublin_bikes.csv'

    s3.upload_file(csv_filename, s3_bucket_name, s3_object_key) 

def main():
    upload_own_data()

if __name__ == "__main__":
    main()


