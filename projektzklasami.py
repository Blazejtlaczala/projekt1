class Angle:
    def __init__(self, grades=0, minutes=0, seconds=0):
        self.seconds = abs(seconds) % 60
        if seconds < 0:
            self.seconds = -self.seconds
            minutes -= abs(seconds) // 60
        else:
            minutes += seconds // 60
        self.minutes = abs(minutes) % 60
        if minutes < 0:
            self.minutes = -self.minutes
            grades -= abs(minutes) // 60
        else:
            grades += minutes // 60
        self.grades = abs(grades) % 360
        if grades < 0:
            self.grades = -self.grades

    def to_seconds(self):
        total_seconds = abs(self.grades)*3600+self.minutes*60+self.seconds
        if self.grades < 0:
            total_seconds = -total_seconds
        return total_seconds

    @staticmethod
    def from_seconds(total_seconds):
        negative = total_seconds < 0
        total_seconds = abs(total_seconds)
        grades = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        if negative:
            grades = -grades
        return Angle(grades, minutes, seconds)

    def __str__(self):
        return f"{self.grades}° {self.minutes:02d}' {self.seconds:02d}''"

    def __add__(self_1, self_2):
        total_seconds = self_1.to_seconds() + self_2.to_seconds()
        return Angle.from_seconds(total_seconds)

    def __sub__(self_1, self_2):
        total_seconds = self_1.to_seconds() - self_2.to_seconds()
        return Angle.from_seconds(total_seconds)

    def __eq__(self1, self2):
        return self1.to_seconds() == self2.to_seconds()

    def __lt__(self1, self2):
        return self1.to_seconds() < self2.to_seconds()

    def __le__(self1, self2):
        return self1.to_seconds() <= self2.to_seconds()
