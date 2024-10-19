import json
import csv

# Load the JSON data
with open('rooms.json', 'r') as json_file:
    data = json.load(json_file)

# Open a CSV file for writing
with open('rooms.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    # Write the header
    writer.writerow(['rid', 'building', 'room_number', 'capacity'])
    # Iterate over each building in the JSON data
    for building, rooms in data.items():
        for room in rooms:
            rid = room['id']
            room_number = room['number']
            capacity = room['capacity']
            writer.writerow([rid, building, room_number, capacity])

print("CSV file has been created successfully.")
