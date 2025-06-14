import os

def get_file_content(working_directory, file_path):
    MAX_CHARS = 10000
    joined_path = os.path.join(working_directory, file_path)
    if not os.path.abspath(joined_path).startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(joined_path):
        return f'Error: File not found or is not a regular file: "{joined_path}"'
    
    try:
        with open(joined_path, "r") as f:

            file_content_string = f.read()
            file_read_max = f.read(MAX_CHARS)
            if len(file_content_string) > MAX_CHARS:
                return f'{file_read_max} ... file {file_path} truncated at {MAX_CHARS} characters'
            return file_content_string
    except Exception as e:
        return f'Error: {str(e)}'