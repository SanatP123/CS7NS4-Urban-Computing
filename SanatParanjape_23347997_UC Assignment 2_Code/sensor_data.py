# To Run this code:
# 1. Install Python 3 in your system
# 2. Import Necessary Libraries (requests and csv)
# 3. In the terminal write the following command "python3 sensor_data.py"





#import requests and csv to request API data and csv to store the data
import requests
import csv

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


csv_filename = "dublinbikes_1000_entries.csv"


with open(csv_filename, mode='w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=column_names)

    writer.writeheader()
    for entry in all:
        writer.writerow(entry)


