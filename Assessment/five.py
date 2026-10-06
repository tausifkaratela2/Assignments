def safe_divide(a, b):
    try:
        x= a/b
        return x
    except ZeroDivisionError:
        print("cannot be divided by zero")
    except TypeError:
        print("should be numbers")
    finally:
        print("done!")

safe_divide(10, 2)
safe_divide(10, 0)
safe_divide(10, "two")

import sys
print("YOUR PYTHON PATH IS:")
print(sys.executable)
