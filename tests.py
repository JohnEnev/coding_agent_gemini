from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file

def main():
    working_dir = "calculator"
    #root_content = get_files_info(working_dir)
    #print(root_content)
    #pkg_content = get_files_info(working_dir, "pkg")
    #print(pkg_content)
    #bin_content = get_files_info(working_dir, "/bin")
    #print(bin_content)
    #up_content = get_files_info(working_dir, "../")
    #print(up_content)

    #print(get_file_content(working_dir, "lorem.txt"))
    #print(get_file_content(working_dir, "main.py"))
    #print(get_file_content(working_dir, "pkg/calculator.py"))
    #print(get_file_content(working_dir, "pkg/notexists.py"))
    #print(get_file_content(working_dir, "bin/cat"))
    #print(write_file(working_dir, "lorem.txt", "Hello, world!"))
    #print(write_file(working_dir, "pkg/new_text.txt", "print('Hello, world!')"))
    #print(write_file(working_dir, "/tmp/tmp.txt", "print('Hello, world!')"))
main()