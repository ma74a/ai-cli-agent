import os 
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    if not file_path.endswith(".py"):
        f'Error: "{file_path}" is not a Python file'

    command = ["python", abs_file_path]
    if args is not None:
        command.extend(args)
    output_string = ""
    try:
        output = subprocess.run(command, cwd=abs_working_dir, timeout=30, capture_output=True)
        # print(output)
        if output.returncode != 0:
            output_string += f"Process exited with code {output.returncode}\n"
        if len(output.stderr) == 0 and len(output.stdout) == 0:
            output_string += "No output produced"
        else:
            output_string += f"STDOUT: {output.stdout}\nSTDERR: {output.stderr}"
        return output_string 
    except Exception as e:
        return f"Error: executing Python file: {e}"
    

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="run the python file with optinal arguments",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path which we want the content of this file",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="An optional array of strings to be used as the args for the file to be run",
                items=types.Schema(
                    type=types.Type.STRING
                )
            )
        },
    ),
)