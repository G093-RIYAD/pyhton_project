marks = int(input("Your mark : "))

def your_grade (grade):
    print(f"You have got: {grade}")

if marks >= 90:
    your_grade("Golden A+")
elif marks < 90 and marks >= 80 :
    your_grade("A+")
elif marks < 80 and marks >= 70 :
    your_grade("A")
elif marks < 70 and marks >= 60 : 
    your_grade("A-")
elif marks < 60 and marks >= 50 : 
    your_grade("B")
elif marks < 50 and marks >= 40 : 
    your_grade("C")
elif marks < 40 and marks >33 : 
    your_grade("D")
elif marks >= 33:
    print("You Got passed SOMEHOW")
else:
    print("You have Failled")
