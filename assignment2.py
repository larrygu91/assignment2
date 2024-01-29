class Assignment2:
    def __init__(self, year: int):
        self.year = year

    def tellAge(self, currentYear: int):
        age = currentYear - self.year
        print(f"Your age is {age}")

    #def listAnniversaries():

    #def modifyYears

    @staticmethod
    def checkGoodString(string: str):
        return (len(string) >= 9 and string[0].isalpha() and string[0].islower() and string.isdigit() and
                len(string) == 1 and string.isdigit())

    #@staticmethod
    #def connectTcp(host: str, port: int):
