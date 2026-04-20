from google.genai import types

from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.run_python_file import run_python_file
from functions.write_file import write_file
from config import Config

def call_function(function_call, verbose=False):
    if verbose:
        print(f"Calling function: {function_call.name}({function_call.args})")
    else:
        print(f" - Calling function: {function_call.name}")

    if function_call.name == "":
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call.name,
                    response={"error": f"Unknown function: {function_call.name}"},
                )
            ],
        )
    
    function_results = ""
    if function_call.name == "get_files_info":
        function_results = get_files_info(Config.WORKING_DIR, **function_call.args)
    if function_call.name == "get_file_content":
        function_results = get_file_content(Config.WORKING_DIR, **function_call.args)
    if function_call.name == "run_python_file":
        function_results = run_python_file(Config.WORKING_DIR, **function_call.args)
    if function_call.name == "write_file":
        function_results = write_file(Config.WORKING_DIR, **function_call.args)
    
    if function_results == "":
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call.name,
                    response={"error": f"Unknown function: {function_call.name}"},
                )
            ],
        )
    
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_call.name,
                response={"result": function_results},
            )
        ],
    )
        
