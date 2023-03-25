import os

import openai
from dotenv import load_dotenv
from langchain.agents import initialize_agent
from langchain.llms import OpenAI

from tools import list_files, move_file

# Load env variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def query_agent(query: str) -> str:
    """Query the Dropbox Agent."""
    llm = OpenAI(temperature=0)
    agent = initialize_agent(
        tools=[
            list_files.ListFilesTool(),
            move_file.MoveFileTool(),
        ],
        llm=llm,
        agent="zero-shot-react-description",
        verbose=True,
    )
    return agent.run(query)


def main() -> None:
    output = query_agent(
        "Can you organize the files in my Dropbox. Then summarize the new folder"
        "structure and the contents of each folder."
    )
    print("Output", output)


if __name__ == "__main__":
    main()
