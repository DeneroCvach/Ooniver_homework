class Time:

    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        if not self.hours // 10:
            self.hours = '0' + str(self.hours)
        if not self.minutes // 10:
            self.minutes = '0' + str(self.minutes)
        if not self.seconds // 10:
            self.seconds = '0' + str(self.seconds)
        return f'{self.hours}:{self.minutes}:{self.seconds}'

    # сложение
    def __add__(self, other):
        total_seconds = self.hours * 3600 + self.minutes * 60 + self.seconds
        total_seconds += other.hours * 3600 + other.minutes * 60 + other.seconds

        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60

        return Time(hours, minutes, seconds)

    # вычитание
    def __sub__(self, other):
        total_seconds = self.hours * 3600 + self.minutes * 60 + self.seconds
        total_seconds -= other.hours * 3600 + other.minutes * 60 + other.seconds

        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60

        return Time(hours, minutes, seconds)

    # сравнение - меньше
    def __lt__(self, other):
        return (self.hours, self.minutes, self.seconds) < (other.hours, other.minutes, other.seconds)

    # сравнение - больше
    def __gt__(self, other):
        return (self.hours, self.minutes, self.seconds) > (other.hours, other.minutes, other.seconds)

    def __eq__(self, other):
        return (self.hours, self.minutes, self.seconds) == (other.hours, other.minutes, other.seconds)

    def time_converter(self):
        total_number_of_seconds = self.hours * 3600 + self.minutes * 60 + self.seconds

        hours = total_number_of_seconds // 3600

        minutes = (total_number_of_seconds % 3600) // 60

        seconds = total_number_of_seconds % 60

        return Time(hours, minutes, seconds)


time_1 = Time(5, 332, 442)
time_2 = Time(1, 524, 143)
print(time_1.time_converter(), '--> first argument converted time')
print(time_2.time_converter(), '--> second argument converted time')
print(time_1 + time_2)
print(time_1 - time_2)
print(time_1 > time_2)
print(time_2 < time_1)
print(time_2 == time_1)
