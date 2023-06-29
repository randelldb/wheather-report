from urllib.request import urlopen
import json

# Define Unicode characters
u_char_celcius = '\u2103'

# Load Json file from URL
data =  "https://data.buienradar.nl/2.0/feed/json"
responds = urlopen(data)

# Convert Json Object to usable parsed data
data_to_json = json.loads(responds.read())

# List weather stations
read_stations = data_to_json["actual"]["stationmeasurements"]
for i in range(len(read_stations)):
    print(f"|{i}| {read_stations[i]['stationname']}")
print("-----")

# Ask user to select weather station and make sure its a number
user_input = input("Input the number of the weather station closesed to your location:")
if user_input.isdigit():
    user_input = int(user_input)
else:
    user_input = input("Please enter a number, try again:")
print("-----")

# Function to check wich entrys are available and display them
def print_if_available(key, label, unit=""):
    if key in read_stations[user_input]:
        value = read_stations[user_input][key]
        print(f"{label}: {value} {unit}")


print(
f"""
=======================================

{read_stations[user_input]['stationname']}

Location: {read_stations[user_input]["regio"]}

Last updated: {read_stations[user_input]["timestamp"]}

Current forcast: {read_stations[user_input]["weatherdescription"]}
"""
)

print_if_available('temperature', 'Temperature', u_char_celcius)
print_if_available('windspeedBft', 'Wind speed', 'Bft')
print_if_available('winddirection', 'Wind direction')
print_if_available('airpressure', 'Air pressure', 'Hpa')
print_if_available('humidity', 'Humidity', '%')
print_if_available('precipitation', 'Rain fall', 'mm')

print(
"""
=======================================
"""
)

