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

new_list_filter_01 = list(map(lambda user: User(user.name, user.age + 1, user.gender), filter(lambda user: 'a' in user.name or 'e' in user.name, users)))

new_list_filter_02 = list(map(lambda user: setattr(user, 'salary', 1000), filter(lambda user: user.age > 18, users)))
# new_list = [setattr(user, 'salary', 1000) for user in users if user.age > 18]

new_list_filter_03 = list(map(lambda user: f"{user.name}, {user.age}", users))

for user in new_list_filter_01:
    print(user.name, user.age)
print()
for user in users:
    if hasattr(user, 'salary'):
        print(user.name, user.salary)
print()
print(new_list_filter_03)
