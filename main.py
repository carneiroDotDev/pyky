import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

from call_function import available_functions, call_function
from prompts import system_prompt


def main():
    load_dotenv()

    verbose = "--verbose" in sys.argv
    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I fix the calculator?"')
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)

    if verbose:
        print(f"User prompt: {user_prompt}\n")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    for i in range(20):
        print(f"\n=== Iteration {i + 1} ===\n")
        try:
            response = generate_content(client, messages, verbose)
            if response and 'finalText' in response:
                print("\n***")
                print(f"\nFinal Response: {response['finalText']}\n")
                break
        except Exception as e:
            print(f"Error: {e}")
            break


def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
        ),
    )
    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

    if not response.function_calls:
        return {'finalText': response.text}

    print("\n***")
    print("\nResponses Candidates: ", response.candidates)
    print("\n")
    for candidate in response.candidates:
        print(f"Candidate: {candidate.content}")
        if candidate.content.role == "function":
            print("\n")
            print(f"Function: {candidate.content.function_call.name}")
            print(f"Response: {candidate.content.parts[0].function_response.response}")
            toolMsg=f"Tool: Here's the result of {candidate.content.parts[0].function_call.name} : {candidate.content.parts[0].function_response.response}"
            print(toolMsg)
            messages.append(
                types.Content(
                    role=candidate.content.role,
                    parts=[types.Part(text=toolMsg)],
                )
            )
            print("\n")
        else:
            # print("Function call detected:", candidate)
            # modelMsg = f"{candidate.content.role.capitalize()}: I want to call {candidate.content.parts[0].function_call.name}..."
            modelMsg = f"{candidate.content.role.capitalize()}: {candidate.content.parts[0].text}"
            print(modelMsg)
            messages.append(
                types.Content(
                    role=candidate.content.role,
                    parts=candidate.content.parts,
                )
            )
            print(modelMsg)
            print("\n")
    
    function_responses = []
    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part, verbose)
        if (
            not function_call_result.parts
            or not function_call_result.parts[0].function_response
        ):
            raise Exception("empty function call result")
        if verbose:
            print(f"-> {function_call_result.parts[0]}")
        function_responses.append(function_call_result.parts[0])
        newContent = types.Content(role="user", parts=[function_call_result.parts[0]])
        messages.append(newContent)
    
        
    if not function_responses:
        raise Exception("no function responses generated, exiting.")

    print("\n***")
    print('messages: ', messages)
    print("\n***")


if __name__ == "__main__":
    main()
