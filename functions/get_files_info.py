import os
from google.genai import types

# - README.md: file_size=1032 bytes, is_dir=False
# - src: file_size=128 bytes, is_dir=True
# - package.json: file_size=1234 bytes, is_dir=False

def get_files_info(working_directory, directory="."):
    abs_working_dir = os.path.abspath(working_directory)
    abs_dir = os.path.abspath(os.path.join(abs_working_dir, directory))

    if not abs_dir.startswith(abs_working_dir):
        return f"Result for '{directory}' directory:\n\t" + f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    contents = os.listdir(abs_dir)
    response = ""
    if directory == ".":
        response += f"Result for current directory:\n\t"
    else:
        response += f"Result for '{directory}' directory:\n\t"
    for content in contents:
        content_path = os.path.join(abs_dir, content)
        is_dir = os.path.isdir(content_path)
        size = os.path.getsize(content_path)

        response += f"- {content}: file_size={size} bytes, is_dir={is_dir}\n\t"

    return response    
    

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory. Use '.' for the current/root working directory.",
            ),
        },
        required=["directory"],
    ),
)
    

