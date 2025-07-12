
def print_file_info(directory_path):
    """
    Prints information (file size, whether it's a directory) for each
    file and directory within the given path, formatted as requested.
    Handles potential errors by re-raising a custom error.
    """
    import os
    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"Error: The directory '{directory_path}' does not exist.")
    try:
        # Get a list of all entries (files and directories) in the specified path
        for entry_name in os.listdir(directory_path):
            # Construct the full path to the entry
            full_path = os.path.join(directory_path, entry_name)

            is_directory = os.path.isdir(full_path)
            file_size = 0 # Default size for directories or if an error occurs getting size

            # Get file size only if it's not a directory
            if not is_directory:
                try:
                    file_size = os.path.getsize(full_path)
                except OSError as e:
                    # Handle cases where file size cannot be retrieved (e.g., permission issues)
                    print(f"Warning: Could not get size for {full_path}: {e}")
                    file_size = -1 # Indicate an error in getting size

            # Print the formatted string
            print(f"- {entry_name}: file_size={file_size} bytes, is_dir={is_directory}")

    except OSError as e:
        # Catch any OS-related errors (e.g., directory not found, permission denied)
        raise Exception(f"Error: Could not process directory '{directory_path}'. {e}")
    except Exception as e:
        # Catch any other unexpected errors
        raise Exception(f"Error: An unexpected error occurred. {e}")

def get_files_info(working_dir, dir=None):
    """
    Get information about files in the specified directory.

    Args:
        working_dir (str): The directory to search for files.
        dir (str, optional): The subdirectory to search within. Defaults to None.

    Returns:
        list: A list of dictionaries containing file information.
    """
    import os

    if dir is None:
        dir = working_dir

    files_info = []
    # 1. Normalize and absolute paths
    # Get the absolute, normalized path for the working directory
    abs_working_directory = os.path.abspath(working_dir)

    # Create the full path by joining and then normalizing to get the absolute path
    # This resolves any '..' or '.' in the relative_path
    full_path = os.path.abspath(os.path.join(abs_working_directory, dir))

    # 2. Validate using common prefix/path
    # On Windows, drive letters might cause issues with commonprefix if not handled.
    # commonpath (Python 3.5+) is generally more robust than commonprefix.
    # We check if the common path between the working directory and the full path
    # is the working directory itself.
    if os.path.commonpath([abs_working_directory, full_path]) != abs_working_directory:
        print(f"Error: Cannot list '{dir}' as it is outside the permitted working directory")
        return f"Error: Cannot list '{dir}' as it is outside the permitted working directory"

    # 3. Ensure the directory exists
    if not os.path.exists(os.path.join(abs_working_directory, dir)):
        print(f"Error: '{dir}' is not a directory")
        return f"Error: '{dir}' is not a directory"

    print_file_info(os.path.join(abs_working_directory, dir))
    
    return files_info

get_files_info("calculator", ".")

def get_file_content(working_dir, file_path):
    """
    Get the content of a file in the specified directory.

    Args:
        working_dir (str): The directory to search for files.
        file_path (str): The path to the file within the working directory.

    Returns:
        str: The content of the file.
    """
    import os
    from config import MAX_CHARS

    abs_working_directory = os.path.abspath(working_dir)
    full_file_path = os.path.join(abs_working_directory, file_path)

    if not os.path.commonpath([abs_working_directory, full_file_path]) == abs_working_directory:
        print(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(full_file_path):
        print(f"Error: File '{file_path}' does not exist in '{working_dir}'")
        return f"Error: File '{file_path}' does not exist in '{working_dir}'"
    
    if not os.path.isfile(full_file_path):
        print(f'Error: File not found or is not a regular file: "{file_path}"')
        return f'Error: File not found or is not a regular file: "{file_path}"'

    with open(full_file_path, 'r') as file:
        content = file.read(MAX_CHARS)    
        print(f"Content of '{file_path}':\n{content}")
        return content