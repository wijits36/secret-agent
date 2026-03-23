from functions.write_file import write_file

print(
    "Result for 'lorem.txt':\n"
    + write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    + "\n"
)
print(
    "Result for 'pkg/morelorem.txt':\n"
    + write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    + "\n"
)
print(
    "Result for '/tmp/temp.txt':\n"
    + write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    + "\n"
)
print(
    "Result for 'pkg':\n"
    + write_file("calculator", "pkg", "this should not be allowed")
)
