import csv
from collections import Counter
with open("data2.csv", newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)
    #print(data1)


file_data.pop(0)
newData = []
for i in range(len(file_data)):
    n_num = file_data[i][1]
    newData.append(float(n_num))

#Calculation of mean

n = len(newData)

total = 0
for x in newData:
    total+=x

mean = total/n
print("Mean (Average) is -> " + str(mean))

#Calculation of median
newData.sort()
if n % 2== 0:
    median1 = float(newData[n//2])
    median2 = float(newData[n//2-1])
    median = (median1+median2)/2

else:
     median = newData[n//2]
print("Median is -> " + str(median))

#Calculation of mode
data2 = Counter(newData)
dataRange = {
    "50-60":0, 
    "60-70":0,
    "70-80":0
}

for height, count1 in data2.items():
    if 50 < float(height) < 60:
        dataRange["50-60"] += count1
    
    elif 60 < float(height) < 70:
        dataRange["60-70"] += count1

    elif 70 < float(height) < 80:
        dataRange["70-80"] += count1

dataMode, dataCount = 0, 0
for range, count1 in dataRange.items():
    if count1 > dataCount:
        dataMode, dataCount = [int(range.split("-")[0]), int(range.split("-")[1])], count1
        mode = float((dataMode[0] + dataMode[1])/2) 
        print(f"mode is -> {mode: 2f} ")



