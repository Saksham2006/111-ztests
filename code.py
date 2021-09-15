import pandas as pd
import random
import plotly.figure_factory as ff
import plotly.express as px
import plotly.graph_objects as go
import statistics

# 1st Stdev, 2nd Stdev, 3rd Stdev

data = pd.read_csv("data.csv")
datalist = data["reading_time"].to_list()

total_mean = statistics.mean(datalist)

def random_sample(counter):
    sample_space = []
    for i in range(0, counter):
        random_index = random.randint(0, len(datalist)-1)
        value = datalist[random_index]
        sample_space.append(value)
    sample_mean = statistics.mean(sample_space)
    sample_stdev = statistics.stdev(sample_space)
    return sample_mean

mean_list = []

for i in range(0, 100):
    mean_set = random_sample(30)
    mean_list.append(mean_set)

stdev = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)
print("mean of sample1:- ", mean)

first_stdev_start, first_stdev_end = mean-stdev, mean+stdev  
second_stdev_start, second_stdev_end = mean-(2*stdev), mean+(2*stdev)  
third_stdev_start, third_stdev_end = mean-(3*stdev), mean+(3*stdev)


figure = ff.create_distplot([mean_list], ["reading_time"], show_hist=False)
figure.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.8], mode="lines", name="Mean"))
figure.add_trace(go.Scatter(x=[first_stdev_start, first_stdev_start], y=[0, 0.8], mode="lines", name="Standard Deviation 1 - Start"))
figure.add_trace(go.Scatter(x=[second_stdev_start, second_stdev_start], y=[0, 0.8], mode="lines", name="Standard Deviation 2 - Start"))
figure.add_trace(go.Scatter(x=[third_stdev_start, third_stdev_start], y=[0, 0.8], mode="lines", name="Standard Deviation 3 - Start"))
figure.add_trace(go.Scatter(x=[first_stdev_end, first_stdev_end], y=[0, 0.8], mode="lines", name="Standard Deviation 1 - End"))
figure.add_trace(go.Scatter(x=[second_stdev_end, second_stdev_end], y=[0, 0.8], mode="lines", name="Standard Deviation 2 - End"))
figure.add_trace(go.Scatter(x=[third_stdev_end, third_stdev_end], y=[0, 0.8], mode="lines", name="Standard Deviation 3 - End"))
figure.show()

zscore_1 = (mean-total_mean)/stdev

print("z-score 1 = ", zscore_1)