from functions.run_python_file import run_python_file

print("Result for 'main.py':\n" + run_python_file("calculator", "main.py") + "\n")
print(
    "Result for 'main.py(3+5)':\n"
    + run_python_file("calculator", "main.py", ["3 + 5"])
    + "\n"
)
print("Result for 'tests.py':\n" + run_python_file("calculator", "tests.py") + "\n")
print("Result for '../main.py':\n" + run_python_file("calculator", "../main.py") + "\n")
print(
    "Result for 'nonexistent.py':\n"
    + run_python_file("calculator", "nonexistent.py")
    + "\n"
)
print("Result for 'lorem.txt':\n" + run_python_file("calculator", "lorem.txt") + "\n")
