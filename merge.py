import csv
from collections import OrderedDict
import os

cd = os.path.dirname(os.path.abspath(__file__))

old_weather_data = os.path.join(cd,'old_weather_forecast.csv')
new_weather_data = os.path.join(cd,'new_weather_forecast.csv')

filenames = old_weather_data, new_weather_data
data = OrderedDict()
fieldnames = []
for filename in filenames:
    with open(filename, 'r') as fp:
        reader = csv.DictReader(fp)
        fieldnames.extend(reader.fieldnames)
        for row in reader:
            data.setdefault(row['Day'], {}).update(row)
fieldnames = list(OrderedDict.fromkeys(fieldnames))
with open('merged.csv', 'w', newline='') as fp:
    writer = csv.writer(fp)
    writer.writerow(fieldnames)
    for row in data.values():
        writer.writerow([row.get(fields, '') for fields in fieldnames])