import os

import openai
from dotenv import load_dotenv

# Load env variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def query_chatgpt_basic() -> None:
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "How long does it take light to reach Mars?"},
        ],
        temperature=0.2,
        n=2,
    )

    print("full response:", completion)
    print("first message:", completion.choices[0].message.content)


def main() -> None:
    query_chatgpt_basic()


if __name__ == "__main__":
    main()
