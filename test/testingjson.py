import json

# Read from a JSON file
with open("test/testdatabase.json", "r") as file:
    data = json.load(file)

# Access a value
print(data["People"]["Denya"]["stats"]["ExamsCompleted"])

# Modify it
data["People"]["Denya"]["stats"]["ExamsCompleted"] += 1

# Save changes
with open("testdatabase.json", "w") as file:
    json.dump(data, file, indent=2)

