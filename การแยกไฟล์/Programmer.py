from Employee import FinalEmployee
class Programmer(FinalEmployee):
    _department = "Software Development"
    def __init__(self, name: str, salary: int, experience: int, skill: str):  # overloading
        super().__init__(name, salary, self._department)  
        self.experience = experience
        self.skill = skill
    # overriding
    def _showData(self) -> None:
        super()._showData()  # Call the _showData method of the parent class
        print(f"Experience: {self.experience} years, Skill: {self.skill}")
        print("#############")