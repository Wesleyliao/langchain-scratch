from dropbox.files import FolderMetadata
from langchain.tools.base import BaseTool

from . import dbx


class MoveFileTool(BaseTool):

    name = "DropboxMoveFileBatch"
    description = (
        "Tool for moving files with '>' as the move symbol and pairs delimited by ','."
        'For example input "/file1.txt > /folder1, /file2.txt > /new folder"'
        'moves "file1.txt" into "/folder1" and moves "file2.txt" into "/new folder".'
        "If the destination folder does not exist it will be created."
        'It does not support any wildcards such as "*".'
    )

    def _run(self, tool_input: str) -> str:
        print()
        pairs = tool_input.split(",")
        for pair in pairs:
            pair.strip()
            src, dst = pair.split(">")
            src = src.strip()
            basefile = src.split("/")[-1]
            dst = "/".join([dst.strip(), basefile])
            print("Moving file", src, "to", dst)
            _ = dbx.files_move_v2(src, dst)

        return ""

    async def _arun(self) -> str:
        raise NotImplementedError()
