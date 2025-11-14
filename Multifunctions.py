class multiplefunctions():
    def Findpercent():
        sub1=int(input("Enter the Subject1 : "))
        sub2=int(input("Enter the Subject2 : "))
        sub3=int(input("Enter the Subject3 : "))
        sub4=int(input("Enter the Subject4 : "))
        sub5=int(input("Enter the Subject5 : "))
        total = sub1+sub2+sub3+sub4+sub5
        percent =(total/500)*100
        return ("Total:",total, "Percent :",percent)

    def Elegible():
        gender=input("Your gender : ")
        age=int(input("Your age : "))
        if(gender=="Male" and age >=21):
            #print(gender)
            #print("you age :" , age)
            print("you are elible for marriage")
            result = "you are elible for marriage"
        elif(gender=="female" and age >=18):
            print("you are elible for marriage")
            result = "you are elible for marriage"
        else:
            print("you are not elible for marriage")
            result = "you are not elible for marriage"
        return result


    def Triangle(height, breadth):
        print("Height :",height)
        print("Breadth :",breadth)
        print("Area of triangle :", (height*breadth)/2)

    def Triangle(height1, height2,breadth,):
        print("Height1 :",height1)
        print("Height2 :",height2)
        print("Breadth :",breadth)
        print("Perimeter of triangle :",height1+height2+breadth)
