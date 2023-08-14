class User:
    name: str
    gender: str
    age: int

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def __str__(self):
        return f'{self.name} {self.gender} {self.age} {self.salary if hasattr(self, "salary") else ""}'


user1 = User('ALex', 'm', 22)
user2 = User('olga', 'f', 23)
user3 = User('ALeks', 'm', 24)
user4 = User('Oleg', 'm', 25)
user5 = User('Anna', 'f', 21)
users = [user5, user4, user3, user2, user1]

new_list_filter_01 = [User(user.name, user.gender, user.age + 1) for user in users if 'a' or 'e' in user.name]

new_list_filter_02 = [setattr(user, 'salary', 1000) for user in users if user.age > 18]

new_list_filter_03 = [f"{user.name}, {user.age}" for user in users]

for user in new_list_filter_01:
    print(user)
print()
for user in users:
    print(user.name, user.salary)
print()
print(new_list_filter_03)