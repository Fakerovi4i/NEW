
class Date:
    def __init__(self, dd=0, mm=0, yyyy=0):
        self.dd = dd
        self.mm = mm
        self.yyyy = yyyy


    def __str__(self) -> str:
        return f"День: {self.dd}\tМесяц: {self.mm}\tГод: {self.yyyy}"

    @classmethod
    def from_string(cls, string: str):
        if cls.is_date_valid(string):
            lst = [int(i) for i in string.split('-')]
            obj = cls(lst[0], lst[1], lst[2])
            return obj


    @staticmethod
    def is_date_valid(string: str) -> bool:
        # lst = string.split('-')
        # lst = [int(i) for i in lst]
        day, month, year = map(int, string.split('-'))
        return 0 < day <= 31 and 0 < month <= 12 and 0 < year < 9999






date = Date.from_string('31-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
