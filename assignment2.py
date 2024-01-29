class Assignment2:
    def __init__(self, year: int):
        self.year = year

    def tellAge(self, currentYear: int):
        print(f"Your age is {currentYear}")

    #def listAnniversaries():

    #def modifyYears

    @staticmethod
    def checkGoodString(string: str):
        return len(string) >= 9 and string[0].isalpha() and string[0].islower()

    @staticmethod
    def connectTcp(host: str, port: int):
        return