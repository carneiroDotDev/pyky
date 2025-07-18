def main():
    from functions.get_files_info import get_files_info
    from functions.get_files_info import get_file_content
    from functions.get_files_info import write_file
    from functions.get_files_info import run_python_file
    
    get_files_info("calculator", ".")
    get_files_info("calculator", "pkg")
    get_files_info("calculator", "/bin")
    get_files_info("calculator", "../")
    
    get_file_content("calculator", "lorem.txt")
    
    get_file_content("calculator", "main.py")
    get_file_content("calculator", "pkg/calculator.py")
    get_file_content("calculator", "/bin/cat")
    
    write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    
    run_python_file("calculator", "main.py")
    run_python_file("calculator", "tests.py")
    # run_python_file("calculator", "../main.py")
    # run_python_file("calculator", "nonexistent.py")
    
    return 'Outermost script executed successfully.'

if __name__ == "__main__":
    main()
