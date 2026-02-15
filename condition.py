# Mini Task 1 – Lead Quality Checker
"""
Create program:
User se input lo:
Name
Industry
Company size
Phir condition lagao:
Agar company size > 100 → High Potential
Warna → Low Potential 
"""

name = input("Enter your Name: ")
industry = input("Enter industry name:")
company_size = int(input("Enter the size of company:"))

if(industry == "Tech" or company_size >100):
    print(name +" has pontentail")
else:
    print(name + " has not pontential")
