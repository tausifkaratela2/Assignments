def get_marks():
    try:
        marks = int(input("enter your marks: "))
    except ValueError:
        print("enter a number")

    if 0 > marks < 100:
        print("Marks must be between 0 to 100")
    elif marks >= 40:
        print(f"Marks: {marks} - Pass")
    else:
        print(f"Marks: {marks} - Fail")

get_marks()