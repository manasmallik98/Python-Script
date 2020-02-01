import re
print("Enter a Email Address")
Email=input()
regex="^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"
Valid_mail=re.search(regex,Email)
if(Valid_mail):
    print("Thank you")
else:
    print(" Please Enter a Valid Email")
