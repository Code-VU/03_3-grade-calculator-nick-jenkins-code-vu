def calculateGrade():
    # Implement your solution in between the two comment blocks
    print("Calculating Grade")
    # This first line is provided for you


    try:
        score = float(input("Enter Score: "))

        if score > 1.0:
            grade = "Bad Score"
        elif score >= 0.9 and score <= 1.0:
            Grade = "A"            
        elif score >= 0.8:
            Grade = "B"                
        elif score >= 0.7:
            Grade = "C"                
        elif score >= 0.6:
            Grade = "D"    
        elif score <= 0.6:
            Grade = "F"                
        else:
            Grade = "Bad Score"

    except:    
        grade = "Bad Score" 
     
    print(Grade)

    # end assignment

## If you want to test locally before you try to sync
## Run > python calculateGrade.py

if __name__ == "__main__":
    calculateGrade()
