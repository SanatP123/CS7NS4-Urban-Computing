import requests
import csv

# URL of the CSV file

def fetch_s3_data():
    url = ""
    try:
        
        response = requests.get(url)

        
        if response.status_code == 200:
            
            csv_data = response.text

        
            reader = csv.reader(csv_data.splitlines())

            #first 20 entries
            for i, row in enumerate(reader):
                
                print(row)
                if i == 19:  # Limit to the first 20 entries
                    break

        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

fetch_s3_data()
