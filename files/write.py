# with open('poems_2.txt', 'w') as my_file:
#     with open('poems.txt') as poem:
#         data = poem.read()
#     my_file.write(data)

with open('poems.txt') as my_file:
    data = my_file.read()
with open('poems_2.txt', 'w') as my_file:
    my_file.write(data)
