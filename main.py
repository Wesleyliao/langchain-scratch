import os

import openai
from dotenv import load_dotenv

# Load env variables
load_dotenv()


def main() -> None:

    openai.api_key = os.getenv("OPENAI_API_KEY")

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who won the world series in 2020?"},
            {
                "role": "assistant",
                "content": "The Los Angeles Dodgers won the World Series in 2020.",
            },
            {"role": "user", "content": "Where was it played?"},
        ],
        temperature=0.2,
    )

    print("response:", completion)


if __name__ == "__main__":
    main()
