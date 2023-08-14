import datetime


class FileContextManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        self.file.write(f"File opened at {datetime.datetime.now()}\n")
        return self.file

    def __exit__(self, type, value, traceback):
        self.file.write(f"File closed at {datetime.datetime.now()}\n")
        self.file.close()


with FileContextManager("example.txt", "a") as file:
    file.write("This is a test line.\n")

with open("example.txt", "r") as file:
    contents = file.read()
    print(contents)
