from functions.get_file_content import get_file_content

print("Result for 'lorem.txt':\n" + get_file_content("calculator", "lorem.txt") + "\n")
print("Result for 'main.py':\n" + get_file_content("calculator", "main.py") + "\n")
print(
    "Result for 'pkg/calculator.py':\n"
    + get_file_content("calculator", "pkg/calculator.py")
    + "\n"
)
print("Result for '/bin/cat':\n" + get_file_content("calculator", "/bin/cat") + "\n")
print(
    "Result for 'pkg/does_not_exist.py':\n"
    + get_file_content("calculator", "pkg/does_not_exist.py")
)
