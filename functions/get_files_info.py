import os

def get_files_info(working_directory, directory=None):
    joined_path = os.path.join(working_directory, directory)
    if not os.path.isdir(joined_path):
        return (f'Error: "{joined_path}" is not a directory')
    if not os.path.abspath(joined_path).startswith(os.path.abspath(working_directory)):
        return (f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
   
    try:

        directory_list = os.listdir(joined_path)
        new_list = []
        for line in directory_list:
            if os.path.isfile(os.path.join(joined_path, line)):
                file_path = os.path.join(joined_path, line)
                file_size = os.path.getsize(file_path)
                new_list.append(f'- {line}: file_size={file_size} bytes, is_dir=False')
            elif os.path.isdir(os.path.join(joined_path, line)):
                file_size = 128
                new_list.append(f'- {line}: file_size={file_size} bytes, is_dir=True')
        return "\n".join(new_list)
    except Exception as e:
        return f'Error: {str(e)}'