import os
from google.genai import types

from config import Config

def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    

    try:
        with open(abs_file_path, 'r') as f:
            file_content = f.read(Config.MAX_CHARS)

            # After reading the first MAX_CHARS...
            if f.read(1):
                file_content += f'[...File "{file_path}" truncated at {Config.MAX_CHARS} characters]'

        return file_content
    except Exception as e:
        return f"Exception reading file {e}"

        
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Give us the content of the file provided",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path which we want the content of this file",
            ),
        },
    ),
)