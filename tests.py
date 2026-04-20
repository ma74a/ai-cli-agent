# from functions.get_files_info import get_files_info
# from functions.get_file_content import get_file_content
# from functions.write_file import write_file
from functions.run_python_file import run_python_file

def main():
    # File info function
    # print(get_files_info("calculator", "."))
    # print(get_files_info("calculator", "pkg"))
    # print(get_files_info("calculator", "/bin"))
    # # print(get_files_info("calculator", "../"))

    # File content function
    # print(get_file_content("calculator", "lorem.txt"))
    # print(get_file_content("calculator", "main.py"))
    # print(get_file_content("calculator", "pkg/calculator.py"))
    # print(get_file_content("calculator", "/bin/cat"))
    # print(get_file_content("calculator", "pkg/does_not_exist.py"))
    
    # File writing
    # print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    # print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    # print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
    # print(write_file("calculator", "pkg2/morelorem.txt", "lorem ipsum dolor sit amet"))

    # File running
    # print(run_python_file("calculator", "main.py"))
    print(run_python_file("calculator", "main.py", ["3 + 5"]))
    # print(run_python_file("calculator", "test.py"))
    # print(run_python_file("calculator", "../main.py"))
    # print(run_python_file("calculator", "nonexistent.py"))
    # print(run_python_file("calculator", "lorem.txt"))


if __name__ == "__main__":
    main()