import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f"Error: '{file_path}' is not in the working directory"

    if not os.path.isfile(abs_file_path):
        parent_dir = os.path.dirname(abs_file_path)
        try:
            os.makedirs(parent_dir, exist_ok=True)
        except Exception as e:
            return f"Exception creating directory '{parent_dir}': {e}"

    try:
        with open(abs_file_path, 'w') as f:
            f.write(content)
        return f"File '{file_path}' written successfully with {len(content)} characters"
    except Exception as e:
        return f"Exception writing file '{file_path}': {e}"