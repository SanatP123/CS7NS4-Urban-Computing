import csv
from flask import Flask, render_template
from Task1_upload_own_data import main
#from Fetch_S3_data import fetch_s3_data

app = Flask(__name__)

app.static_folder = 'static'

def load_bike_data_from_csv():
    
    bike_data = []
    with open('UC_4/dublinbikes.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            
            station = {
                'name': row['name'],
                'latitude': float(row['latitude']),
                'longitude': float(row['longitude']),
                'available_bikes': int(row['available_bikes'])
            }
            bike_data.append(station)
    return bike_data

@app.route('/')
def index():
    # Call the main function
    main()
    bike_data = load_bike_data_from_csv()

    #bike_data = fetch_s3_data()

    
    return render_template('index.html', bike_data = bike_data)  

@app.route('/analysis')
def display_analysis():
    

    
    graph1_path = 'figures/1.png'
    graph2_path = 'figures/2.png'
    graph3_path = 'figures/3.png'
    graph4_path = 'figures/4.png'
    graph5_path = 'figures/5.png'
    graph6_path = 'figures/6.png'

    return render_template('analysis.html', graph1_path=graph1_path, graph2_path=graph2_path, graph3_path=graph3_path, graph4_path=graph4_path,graph5_path=graph5_path,graph6_path=graph6_path )
if __name__ == '__main__':
    app.run(debug=True) 