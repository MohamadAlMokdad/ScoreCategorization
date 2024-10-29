
x=int(input("Enter Number of students you need to know if they fail or pass:"))

for i in range(x):
  
    score = float(input(f"Enter score for student {i + 1}: "))

    
    if score >= 60:
        print(f"Score: {score}, Result: Pass")
    else:
        print(f"Score: {score}, Result: Fail")
