import os

def get_files_info(working_directory, directory=None):
    if not os.path.isdir(directory):
        return (f'Error: "{directory}" is not a directory')
    if not os.path.commonpath([working_directory, directory]).startswith(os.path.abspath(working_directory)):
        return (f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
   
    directory_list = os.listdir(directory)
    new_list = []
    for line in directory_list:
        if os.path.isfile(os.path.join(directory, line)):
            file_path = os.path.join(directory, line)
            file_size = os.path.getsize(file_path)
            new_list.append(f'- {line}: file_size={file_size} bytes, is_dir=False')
        elif os.path.isdir(os.path.join(directory, line)):
            file_path = os.path.join(directory, line)
            file_size = os.path.getsize(file_path)
            new_list.append(f'- {line}: file_size={file_size} bytes, is_dir=True')
    return "\n".join(new_list)