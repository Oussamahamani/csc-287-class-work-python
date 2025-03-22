from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('weather_data/sitka_weather_2021_simple_missing_data.csv')
lines = path.read_text().splitlines()
reader = csv.reader(lines)

header_row = next(reader)
print(header_row)
for index, column_header in enumerate(header_row):
    print(index, column_header)

highs = []
dates = []
lows = []
for row in reader:
    try:
        high = int(row[4])
        low = int(row[5])
        date = str(row[2])
        date = datetime.strptime(date, '%Y-%m-%d')   
    except ValueError:
        print(f"Missing data for {date}")
    else:

        lows.append(low)
        highs.append(high)
        dates.append(date)

# print(dates)
# print(highs,lows)

x = [0, 1, 2, 3, 4, 5]

# plt.style.use('seaborn-v0_8-paper')

# plt.plot(dates,highs,
#     color='red',          # Line color
#     linestyle='-',          # Solid line style
#     linewidth=2,            # Line width
#     marker='s',             # Square markers
#     # markerfacecolor='orange', # Marker fill color
#     markersize=2            # Marker size
# )


# # Add titles and labels
# plt.title("Daily Hight temperatures, july 21")
# # plt.xlabel("temps")
# plt.ylabel("temps")
# # Customize grid and add legend
# plt.grid(True, linestyle='--', linewidth=0.5) # Dashed grid lines
# # plt.legend(["Sample Data"], loc="upper left")
# first_date = datetime.strptime('2021-07-01', '%Y-%m-%d')
# print(first_date)

# plt.show()



plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()


ax.plot(dates,highs,color='red')
ax.plot(dates,lows,color='blue')

# ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("", fontsize=14)
ax.set_ylabel("temps", fontsize=14)
fig.autofmt_xdate()
ax.fill_between(dates,
			 highs,
			 lows,
			 facecolor='blue',
			 alpha=0.1)

# ax.locator_params(axis='x', nbins=5)
plt.show()