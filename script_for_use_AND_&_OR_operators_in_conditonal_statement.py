# For Refrence https://www.fosslinux.com/46256/python-script-examples.htm



#assignment marks
assignment_marks = float(input("Enter the assigment one marks:"))

#assignment marks2
assignmenttwo_marks = float(input("Enter the assigment two marks:"))


#use AND and OR operator to check if it passes the condition
if(assignment_marks >= 40 and assignmenttwo_marks >= 30) or (assignment_marks + assignmenttwo_marks)>=70:
    print("\nYou are successfull")
else:
        print("\nYou are one level up")
