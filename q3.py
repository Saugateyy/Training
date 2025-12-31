choice=int(input("convert: 1)cel to far    2)far to cel"))
if choice==1:
 tcel=float(input("Enter your temperature in celsius scale"))
 tfar=(tcel*9/5)+32
 print(f"Temperature in farhenheit scale is {tfar}")
elif choice==2:
 tfar=float(input("Enter your temperature in farhenheit scale"))
 tcel=(tfar-32)*5/9
 print(f"Temperature in celsius scale is {tcel}")
else:
 print("Invalid Choice")



              