import json
import pandas as pd


# CONVERTER FROM JSON FORMAT TO CSV FORMAT



# FIRST WE LOAD THE JSON FILE WE WANT TO TRANSFORM
with open('rooms.json') as f:
    json_data = json.load(f)

# Flatten the JSON data into a list of dictionaries
flat_data = []
for building, rooms in json_data.items():
    for room in rooms:
        flat_data.append({
            'id' : room['id'],
            'building': building,
            'number': room['number'],
            'capacity': room['capacity']
        })

# Create a DataFrame from the flattened data
data = pd.DataFrame(flat_data)

# THE EMPTY VALUES, ADD IT THE VALUE NULL
data.fillna(value='null', inplace=True)

# Save to CSV, index needs to be false or will show the number of the row as a campus
data.to_csv('rooms.csv', index=False)


