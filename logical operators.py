temp=int (input("what is the temperatur outside?"))
if temp>=0 and temp<=30:
    print("the temperature is good outside today!")
    print("go outside")
elif temp<0 or temp>30:
    print("the temperature is bad today")
elif not(temp>=0):
    print("But its atleast not that cold!")