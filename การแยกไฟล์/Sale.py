from Employee import FinalEmployee
class Sale(FinalEmployee):
    _department = "Sales"
    def __init__(self, name: str, salary: int, area: str):  # overloading
        super().__init__(name, salary, self._department)  
        self.area = area

    # overriding
    def _showData(self) -> None:
        super()._showData()  # Call the _showData method of the parent class
        print(f"Area: {self.area}")
        print("#############")