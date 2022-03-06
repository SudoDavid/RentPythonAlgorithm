def Calc_total():
    electricCost = float(input('Please enter the total electric for the month:\n'))
    quotient = 3/5
    portion = quotient * 10
    rent = 1235.0
    Finalele = (electricCost/float(portion))
    electric = electricCost - Finalele 
    FinalDue = electric + rent
    print(FinalDue)
Calc_total()