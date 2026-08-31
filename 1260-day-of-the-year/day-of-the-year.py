class Solution:
    def dayOfYear(self, date: str) -> int:
        year = int(date[0:4])
        month = int(date[5:7])
        day = int(date[8:10])

        days = [31, 28, 31, 30, 31, 30,
                31, 31, 30, 31, 30, 31]

        if month > 2 and (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
            days[1] = 29

        total = 0

        for i in range(month - 1):
            total += days[i]

        total += day

        return total