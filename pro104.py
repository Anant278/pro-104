import csv
from collections import Counter

#Get all data of the csv file
with open("pro-104.csv", newline="") as x:
    reader = csv.reader(x)
    file_data = list(reader)
file_data.pop(0)
new_data = []
for i in range(len(file_data)):
    num = file_data[i][1]
    new_data.append(float(num))
n = len(new_data)
new_data.sort()
data = Counter(new_data)

#Mean
def mean():
    sum = 0
    for k in new_data:
        sum += k
    Mean = sum/n
    print(Mean)

#Median
def median():
    if n%2 == 0:
        median1 = float(new_data[n//2])
        median2 = float(new_data[n//2-1])
        Median = (median1 + median2)/2
    else:
        Median = new_data[n//2]
        print(n)
        print(Median)

#Mode
def mode():
    modeDataRange = {
        "50-60": 0,
        "60-70": 0,
        "70-80": 0
    }
    for weight,occurence in data.items():
        if 50 < float(weight) < 60:
            modeDataRange["50-60"] += occurence
        elif 60 < float(weight) < 70:
            modeDataRange["60-70"] += occurence
        else:
            modeDataRange["70-80"] += occurence
    modeRange, modeOccurence = 0,0
    for range,occurence in modeDataRange.items():
        if occurence > modeOccurence:
            modeRange, modeOccurence = [int(range.split("-")[0]), int(range.split("-")[1])],occurence
    mode = float((modeRange[0] + modeRange[1])/2)
    print(mode)

#Calling 
mean()
median()
mode()