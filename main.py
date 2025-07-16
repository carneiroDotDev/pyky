import os
import sys
from dotenv import load_dotenv
from google import genai
from functions.get_files_info import functionDeclarations


def main():
    print("Hello from pyky!")
    if len(sys.argv) < 2 or not sys.argv[1]:
        print("Error: Please provide a prompt.", file=sys.stderr)
        sys.exit(1)
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    available_functions = genai.types.Tool(
                           function_declarations=functionDeclarations()
                       )
    
    print(f"sys.argv: {sys.argv}")
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=sys.argv[1],
        config=genai.types.GenerateContentConfig(
            # temperature=0.2,
            # max_output_tokens=1000,
            # top_p=0.95,
            # top_k=40,
            # stop_sequences=["\n"],
            tools=[available_functions],
            system_instruction="""
            You are a helpful AI coding agent.
            
            When a user asks a question or makes a request, make a function call plan. You can perform the following operations:
            
            - List files and directories
            - Read file contents
            - Execute Python files with optional arguments
            - Write or overwrite files
            
            All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
            """,
        ),
    )
    # print(f"response obj: {response}")
    print(f"response: {response.text}")
    print(f"Calling function: {response.function_calls}({response.function_calls})")

    if len(sys.argv) > 2 and sys.argv[2] == "--verbose":
        print("User prompt: ", sys.argv[1])
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
