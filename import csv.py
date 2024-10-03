import csv
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client.user_data
collection = db.user_details

class User:
    def __init__(self, age, gender, total_income, expenses):
        self.age = age
        self.gender = gender
        self.total_income = total_income
        self.expenses = expenses

    def to_csv(self, filename):
        data = collection.find()
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Age", "Gender", "Total Income", "Utilities", "Entertainment", "School Fees", "Shopping", "Healthcare"])
            for user in data:
                writer.writerow([
                    user["age"],
                    user["gender"],
                    user["total_income"],
                    user["expenses"]["utilities"],
                    user["expenses"]["entertainment"],
                    user["expenses"]["school_fees"],
                    user["expenses"]["shopping"],
                    user["expenses"]["healthcare"]
                ])

user = User(None, None, None, None)
user.to_csv('user_data.csv')
