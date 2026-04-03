student = {
    "name": "Sagar",
    "age": 27,
    "course": "Computer Science"
}

keyName = 'age'

print(student[keyName])
for stud in student:
    print(f"stud = {stud} , type of stud = {type(stud)} keyValue = {student.get(stud)}")