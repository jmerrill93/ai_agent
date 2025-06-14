import os

def get_file_content(working_directory, file_path):
    MAX_CHARS = 10000
    joined_path = os.path.join(working_directory, file_path)
    if not os.path.isfile(joined_path):
        return f'Error: File not found or is not a regular file: "{joined_path}"'
    if not os.path.abspath(joined_path).startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    try:
        with open(file_path, "r") as f:

            file_content_string = f.read(MAX_CHARS)
            if len(file_content_string) > MAX_CHARS:
             print ("...File "{file_path}" truncated at 10000 characters")
    except Exception as e:
        return f'Error: {str(e)}'