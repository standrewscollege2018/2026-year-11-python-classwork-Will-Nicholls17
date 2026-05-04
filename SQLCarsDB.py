import _sqlite3
DATABASE = 'cars.db'
connection = _sqlite3.connect(DATABASE)
cursor = connection.cursor()
cursor.execute("SELECT * FROM car WHERE colour = 'Red'")
results = cursor.fetchall()
connection.close()
number_of_cars = len(results)
for result in results:
    for i in range(len(result)):
        print(f"{result[i]:15} ", end="")
    print()  # Print a newline after each row
print(f"\nTotal number of red cars: {number_of_cars}\n")