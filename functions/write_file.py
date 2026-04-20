import os 
from google.genai import types

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    if os.path.isdir(abs_file_path):
        return f'Error: Cannot write to "{file_path}" as it is a directory'
    
    parent_dir = os.path.dirname(abs_file_path)
    os.makedirs(parent_dir, exist_ok=True)
    try:
        with open(abs_file_path, 'w') as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Failed to write into the file {file_path} , {e}"
    

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write into the file who exits, if not exit create it and write into it",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path which we want write into it",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content we want to write into the file"
            )
        },
    ),
)