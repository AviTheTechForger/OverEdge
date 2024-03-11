# A py script to add a random entry the best_player.csv

import csv
import random

with open('/opt/airflow/s3/raw_data/best_player.csv', 'a+', newline='\n') as f:
    writer = csv.writer(f, delimiter=',', quotechar="'", quoting=csv.QUOTE_MINIMAL)
    writer.writerow([random.choice(["Virat Kohli", "Rohit Sharma"])])

print('Name Inserted')