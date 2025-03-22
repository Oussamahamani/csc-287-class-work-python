from random import randint
import plotly.express as px

results = []
for roll_num in range(1000):
    result = randint(1, 6)
    results.append(result)

print(results)
frequencies = []
for value in range(1, 6):
    frequencies.append(results.count(value))

print(frequencies)
fig = px.bar(x = range(1, 6), y = frequencies)
fig.show()
