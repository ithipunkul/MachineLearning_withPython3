from Programmer import Programmer
from Sale import Sale

Yew: Programmer = Programmer("Yew", 50000, 5, "Python")
Yew._showData()
print(Yew.getIncome())

Yean: Sale = Sale("Yean", 30000, "Kampangphet")    
Yean._showData()
print(Yean.getIncome())
