
import json
import datetime
import matplotlib.pyplot as plt


file = 'data/unit_two_2020.json'

def read(file):
    with open(file) as f:
        data = json.load(f)
    return data

def extract_data(data, offset=1):

    num_data = data['total_records']
    value_list = []
    date_list = []

    for i in range (0, num_data, offset):
        value_list.append(data['values'][i]['value'])
        miliseconds = data['values'][i]['effectiveDate']
        date_list.append(datetime.datetime.fromtimestamp(miliseconds/1000.0))

    return value_list, date_list

data = read(file)
values, dates = extract_data(data)

plt.plot(dates, values)
plt.show()
