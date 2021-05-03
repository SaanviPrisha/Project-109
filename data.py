import statistics
import pandas as pd

file1 = pd.read_csv("data.csv")
data = file1["reading score"].to_list()

mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)

print("The mean of this data is ", mean)
print("The median of this data is ",median)
print("The mode of this data is ",mode)

std_deviation = statistics.stdev(data)

std1_start, std1_end = mean - std_deviation, mean + std_deviation
std2_start, std2_end = mean - (2*std_deviation), mean+(2*std_deviation)
std3_start, std3_end   = mean - (3*std_deviation), mean+(3*std_deviation)

print("Standard Deviation of this data is",std_deviation)

std1 = [result for result in data if result> std1_start and result< std1_end]
std2 = [result for result in data if result> std2_start and result< std2_end]
std3 = [result for result in data if result> std3_start and result< std3_end]

print("{}% Of Data Lies Within 1 Deviation".format(len(std1)*100/len(data)))
print("{}% Of Data Lies Within 2 Deviation".format(len(std2)*100/len(data)))
print("{}% Of Data Lies Within 3 Deviation".format(len(std3)*100/len(data)))