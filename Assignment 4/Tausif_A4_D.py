with open("invalid_marks.txt", "w") as file:
    file.write("hello")

with open("valid_marks.txt", "w") as file:
    file.write("75")

def read_marks(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            marks = int(content)
            print(marks)
            return marks
    except FileNotFoundError:
        print(f"file {filename} not found")
    except ValueError:
        print("content could not be converted to numbers")
    finally:
        print("File operation finished.")

read_marks("invalid_marks.txt")
read_marks("valid_marks.txt")
read_marks("missing_file.txt")