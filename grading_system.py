while True:
    grade = float(input("Enter your grade: "))
    
    if grade < 0 or grade > 100:
        print("Invalid number. Number must be between 0 and 100") 
        # loop if number is less then 0 or higher then 100
    else:
        if 90 <= grade <= 100:
            grade = "A"
        elif 80 <= grade <= 90:
            grade = "B"
        elif 70 <= grade <= 80:
            grade = "C"
        elif 60 <= grade <= 70:
            grade = "D"
        else:
            grade = "F"
            
    print("Your grade is: " + grade)
    break # way to exit the loop