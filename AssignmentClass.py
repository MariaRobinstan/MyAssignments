class MyAssignments():
    def Subfields():
        list=["Subfields in AI are:","Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        for subfields in list:
            print(subfields)
    def OddEven():
        num=int(input("Enter the number:"))
        if((num%2)==1):
            print("Odd Number")
            message ="Odd Number"
        else:
            print("Even Number")
            message ="Even Number"
        return message
    def MarriageEligibility():
        gender=input("Enter your gender:")
        age=int(input("Ener your age:"))
        if(age>=18 and gender=="Female"):
            print("Eligible")
            message="Eligible"
        elif(age>=21 and gender=="Male"):
            print("Eligible")
            message="Eligible"
        else:
            print("Not Eligible")
            message="Not Eligible"
        return message
    def PercentageofMarks():
        num1=int(input("Subject1="))
        num2=int(input("subject2="))
        num3=int(input("subject3="))
        num4=int(input("subject4="))
        num5=int(input("subject5="))
        add=num1+num2+num3+num4+num5
        print("Total=",add)
        print("Percentage=",add/5)
    def Triangle():
        num1=int(input("Height:"))
        num2=int(input("Breadth:"))
        Answer=num1*num2/2
        print("Area Formula:(Height*Breadth)/2")
        print("Area of Triangle:",Answer)
        num3=int(input("Height1:"))
        num4=int(input("Height2:"))
        num5=int(input("Breadth:"))
        Add=num3+num4+num5
        print("Perimeter Formula:Height1+Height2+Breadth")
        print("Perimeter of Triangle:",Add)

