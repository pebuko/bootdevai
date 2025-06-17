import os
from google import genai
from dotenv import load_dotenv
import sys
from sys import argv as sys_argv
import argparse

#if len(sys_argv) != 2:
   # print("Usage: python3 main.py <your AI prompt>")
  #  sys.exit(1)
if len(sys_argv) < 1:
    print("Usage: python3 main.py <your AI prompt>")
    sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Example script using arguments and environment variables.")

    parser.add_argument("c1", type=str, help="required string argument for the AI prompt")
    
    parser.add_argument("--verbose", action="store_true", help="Optional argument (default: False)")

    args = parser.parse_args()

    
    load_dotenv()

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=args.c1
    )
    
    if args.verbose: 
        

    
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
        print("User prompt: {args.c1}")
        print("Response:")
    print(response.text)    


if __name__ == "__main__":
    main()
