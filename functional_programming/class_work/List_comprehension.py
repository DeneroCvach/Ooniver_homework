lst_1 = [1, 2, 3, 5, 6, 7, 8, 9, 0]
lst_gen = [x + 1 for x in lst_1]
print(lst_gen)


class User:
    def __init__(self, age):
        self.age = age


user_1 = User(10)
user_2 = User(15)
user_3 = User(20)
users_list = [user_1, user_2, user_3]
changed_age = [user.age + 1 for user in users_list if user.age > 18]
print(changed_age)

lst_2 = [1, 2, 3, 5, 6, 7, 8, 9, 0]
new_list = [x for x in lst_2 if not x % 2]
print(new_list)
print()

b = 10
matrix = [[n for n in range(b * n - 10 + 1, b * n + 1)] for n in range(1, 11)]
for row in matrix:
    print(row)
