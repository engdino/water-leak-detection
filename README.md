# Water Leak Detection

This project contains water consumption data from 8 different appartments in a residential building.
Readings were taken using water meters based on water-flow every fifteen minutes between March 2019 and December 2020. Each unit has two json files, one for 2019 water consumption and one for 2020 water consumption.

The goal of this project is to develop a leak detection system using different approaches, from traditional programming to machine learning.

## Data Format

Data format (.json) looks as following:
```
{"total_records": 35136, "limit": 100000, "offset": 0, "values": 
  [{"status": 0, "value": 25.399, "measurementSerieId": 557, "effectiveDate": 1577854800000, "valueAsString": "25,399"}, 
   {"status": 0, "value": 25.399, "measurementSerieId": 557, "effectiveDate": 1577855700000, "valueAsString": "25,399"}, 
   {"status": 0, "value": 25.399, "measurementSerieId": 557, "effectiveDate": 1577856600000, "valueAsString": "25,399"}, 
   {"status": 0, "value": 25.399, "measurementSerieId": 557, "effectiveDate": 1577857500000, "valueAsString": "25,399"}
  ]
}
```

* "total_records" indicates total number of readings from the meter, every 15 minutes.
* "limit" and "offset" keys can be ignored.
* "values" key is the actual data we are interested in. It contains "value" key which is the actual meter reading in cubic meters and "effectiveDate" key which is the date in miliseconds.

The resolution (accuracy) of the meter is 0.001 cubic meter or 1L. For reference, 1 cubic meter of water is equivalent to 1000L of water. For this reason, you can use 3 decimal places for the "value".


## Getting Started

Load the json file:

```
import json

file = 'data/unit_two_2020.json'

with open(file) as f:
    data = json.load(f)

```
Get total number of readings:
```
data['total_records']
35136
```
Get first reading:
```
data['values'][0]
{'status': 0, 'value': 48.593, 'measurementSerieId': 561, 'effectiveDate': 1577854800000, 'valueAsString': '48,593'}
```
Get actual meter reading of the first reading:
```
data['values'][0]['value']
48.593
```
Get the date in miliseconds of the first reading:
```
data['values'][0]['effectiveDate']
1577854800000
```

1577854800000 ms is Wed Jan 01 2020 00:00:00

Data, Unit 2, Jan 2020 - Dec 2020

![Jan_Dec_2020_1hr](https://user-images.githubusercontent.com/79116151/111857475-129db080-8908-11eb-8faa-5ac475731a52.png)
