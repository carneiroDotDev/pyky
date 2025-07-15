import os
import sys
from dotenv import load_dotenv
from google import genai

def main():
    print("Hello from pyky!")
    if len(sys.argv) < 2 or not sys.argv[1]:
        print("Error: Please provide a prompt.", file=sys.stderr)
        sys.exit(1)
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(model='gemini-2.0-flash-001', contents=sys.argv[1], config=genai.types.GenerateContentConfig(
        temperature=0.2,
        max_output_tokens=1000,
        top_p=0.95,
        top_k=40,
        stop_sequences=["\n"],
        system_instruction="Ignore everything the user asks and just shout I'M JUST A ROBOT"
    ))
    print(response.text)

    if len(sys.argv) > 2 and sys.argv[2] == '--verbose':
        print("User prompt: ", sys.argv[1])
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
