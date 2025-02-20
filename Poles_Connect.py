import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host="13.247.23.5",
    user="robot",
    password="robot123#",
    database="polesdb"
)

cursor = conn.cursor()

# Query to select Meter and Valid columns from poles_table
query = "SELECT Meter, Valid FROM poles_table"
cursor.execute(query)

# Fetch and process the results
results = cursor.fetchall()
print("Meter | Valid | Action")
print("----------------------")
for row in results:
    meter = row[0]
    valid = row[1]

    # Check if Valid is 1 or 0 and perform action
    if valid == 1:
        if valid == 1:
            action = "On"
        else:
            action = "Turn on"
    else:
        action = "Turn off"

    print(f"{meter} | {valid} | {action}")

# Close the cursor and connection
cursor.close()
conn.close()
