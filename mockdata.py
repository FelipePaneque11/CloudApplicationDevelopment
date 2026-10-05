import csv 

def csvToJson():
    with open("MOCK_DATA.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            print(row)

csvToJson()


