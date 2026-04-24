class FinalEmployee:
    def __init__(self, name: str, salary: int, position: str):
        self.__name = name
        self.__salary = salary
        self._position = position

    def _showData(self) -> None:
        print(f"Name: {self.__name}, Salary: {self.__salary}, Position: {self._position}")
    
    def getIncome(self) -> int:
        return self.__salary*12
    def __str__(self) -> None:
        return ("Name = {}, Salary = {}, Position = {}".format(self.__name, self.__salary, self._position))