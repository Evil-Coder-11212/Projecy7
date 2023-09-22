import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd


df = pd.read_csv("data.csv")
dice_result = df["temp"].tolist()
mean = sum(dice_result) / len(dice_result)
sd = statistics.stdev(dice_result)
median = statistics.median(dice_result)
mode = statistics.mode(dice_result)


first_std_deviation_start, first_std_deviation_end = mean-sd, mean+sd
second_std_deviation_start, second_std_deviation_end = mean-(2*sd), mean+(2*sd)
third_std_deviation_start, third_std_deviation_end = mean-(3*sd), mean+(3*sd)
fig = ff.create_distplot([dice_result], ["Result"], show_hist=False)
fig.show()


list_of_data_within_1_std_deviation = [result for result in dice_result if result > first_std_deviation_start and result < first_std_deviation_end]
list_of_data_within_2_std_deviation = [result for result in dice_result if result > second_std_deviation_start and result < second_std_deviation_end]
list_of_data_within_3_std_deviation = [result for result in dice_result if result > third_std_deviation_start and result < third_std_deviation_end]


print(f"Mean = {mean}")
print(f"Median = {median}")
print(f"Mode = {mode}")
print(f"Standard deviation = {sd}")
print(f"Lies 1 Standard deviation={len(list_of_data_within_1_std_deviation)*100.0/len(dice_result)}")
print(f"Lies 2 Standard deviation={len(list_of_data_within_2_std_deviation)*100.0/len(dice_result)}")
print(f"Lies 3 Standard deviation={len(list_of_data_within_3_std_deviation)*100.0/len(dice_result)}")