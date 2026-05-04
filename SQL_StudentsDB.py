import _sqlite3
DATABASE = 'students.db'
connection = _sqlite3.connect(DATABASE)
cursor = connection.cursor()
cursor.execute("SELECT * FROM student WHERE first_name LIKE 'John%'")
results = cursor.fetchall()
connection.close()
number_of_students = len(results)
for result in results:
    for i in range(len(result)):
        print(f"{result[i]:15} ", end="")
    print() 
print(f"Total number of students: {number_of_students}")