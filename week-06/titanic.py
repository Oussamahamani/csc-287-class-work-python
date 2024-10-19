# Open the file and read into a list of lines.
with open('./file.csv', encoding="utf-8") as f:
    lines = f.readlines()

# Iterate through all the lines.
# Output includes the line number.
passenger_count = 0
classes_passenger_count = {
    "1":0,
    "2":0,
    "3":0,
}

for index,line in enumerate(lines):
    if(index ==0): continue
    passenger_class = line.rstrip().split(",")[2]
    classes_passenger_count[passenger_class] +=1
    
    passenger_name = line.rstrip().split(",\"")[1].split("\"")[0]
    print(passenger_name)
    
    passenger_count += 1

print("there are in total " +str(passenger_count) + " passengers")

with open("summary.txt", "w") as file:
    file.write(f"first class has {classes_passenger_count["1"]}\n")
    file.write(f"second class has {classes_passenger_count["2"]}\n")
    file.write(f"third class has {classes_passenger_count["3"]}\n")
