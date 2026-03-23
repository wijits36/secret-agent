import argparse
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

from call_function import available_functions, call_function
from config import MAX_LOOPS, MODEL_NAME
from prompts import system_prompt


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if api_key is None:
        raise RuntimeError("GEMINI_API_KEY not found in .env file")

    parser = argparse.ArgumentParser(description="secret-agent")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable verbose output"
    )
    args = parser.parse_args()

    client = genai.Client(api_key=api_key)
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    if args.verbose:
        print(f"User prompt: {args.user_prompt}")

    for _ in range(MAX_LOOPS):
        final_response = generate_content(client, messages, args)
        if final_response:
            print(final_response)
            return

    # only reached if the loop exhausted all 20 iterations
    print("Error: Agent took too many steps to complete the task")
    exit(1)


def generate_content(client, messages, args):
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
        ),
    )

    if response.usage_metadata is None:
        raise RuntimeError("Failed API request, usage metadata not available")

    if response.candidates:
        for candidate in response.candidates:
            messages.append(candidate.content)

    if args.verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        print()

    function_calls = response.function_calls
    function_results = []

    if function_calls:
        for call in function_calls:
            function_call_result = call_function(call, args.verbose)

            if (
                function_call_result.parts is None
                or len(function_call_result.parts) == 0
            ):
                raise Exception(f"Function {call.name} returned None")

            if function_call_result.parts[0].function_response is None:
                raise Exception(f"Function {call.name} returned an invalid response")

            if function_call_result.parts[0].function_response.response is None:
                raise Exception(f"Function {call.name} returned an invalid response")

            function_results.append(function_call_result.parts[0])

            if args.verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")

        messages.append(types.Content(role="user", parts=function_results))

    else:
        return response.text


if __name__ == "__main__":
    main()
