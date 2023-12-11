#import modules
import sqlite3
from datetime import datetime
import matplotlib.pyplot as plt
# Create empty data lists for analysis
factors = []
timeStamps = []
piValue = []
timeStamps2 = []
piValue2 = []
factors2 = []
# Connect to the sqllite and fetch data
connection = sqlite3.connect('api_data.db')
database = connection.cursor()
database.execute('SELECT * FROM api_data')
data = database.fetchall()

# Plot relationship between timestamps and factors
# Append data items
for entry in data:
    factors.append(entry[1])
    timeStamps.append(datetime.strptime(entry[3], "%Y-%m-%d %H:%M:%S"))
# Plot factor vs timestamp
plt.plot(timeStamps, factors, marker='o', linestyle='-', color='b')
plt.title('Factor vs. Timestamp')
plt.xlabel('Timestamp')
plt.ylabel('Factor')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Plot relationship between pi and timestamp
# Append data
for entry in data:
    piValue.append(entry[2])
    timeStamps2.append(datetime.strptime(entry[3], "%Y-%m-%d %H:%M:%S"))
# Plotting pi vs. time
plt.plot(timeStamps2, piValue, marker='o', linestyle='-', color='r')
plt.title('Pi Value vs. Timestamp')
plt.xlabel('Timestamp')
plt.ylabel('Pi Value')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Plot relationship between pi vs factor
# Append data
for entry in data:
    piValue2.append(entry[2])
    factors2.append(entry[1])
# Plot pi vs factor
plt.plot(factors2, piValue2, marker='o', linestyle='-', color='c')
plt.title('Pi Value vs. Factor')
plt.xlabel('Factor')
plt.ylabel('Pi Value')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# exit database
connection.close()