
from functions.get_files_info import get_files_info
from functions.get_files_info import get_file_content

# get_files_info("calculator", ".")
# get_files_info("calculator", "pkg")
# get_files_info("calculator", "/bin")
# get_files_info("calculator", "../")

# get_file_content("calculator", "lorem.txt")

get_file_content("calculator", "main.py")
get_file_content("calculator", "pkg/calculator.py")
get_file_content("calculator", "/bin/cat")
