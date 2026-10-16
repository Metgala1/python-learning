import csv

students = [
    {"Name": "Roger", "Score": 85},
    {"Name": "Mary", "Score": 92},
    {"Name": "John", "Score": 78},
    {"Name": "David", "Score": 96}
]
header = ["Name" , "Score"]

with open("score.csv" , "w" , encoding="utf-8") as file:
    writer = csv.DictWriter(file , fieldnames=header)
    writer.writeheader()
    writer.writerows(students)

print("Successful")
    