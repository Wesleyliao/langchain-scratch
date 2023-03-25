from dropbox.files import FolderMetadata
from langchain.tools.base import BaseTool

from . import dbx


class ListFilesTool(BaseTool):

    name = "DropboxListFiles"
    description = "Tool for listing all files in DropBox. No parameter is necessary."

    def _run(self, tool_input: str) -> str:
        entries = dbx.files_list_folder("", recursive=True).entries
        res = [
            dict(
                path=entry.path_display,
                type="folder" if isinstance(entry, FolderMetadata) else "file",
            )
            for entry in entries
        ]
        return str(res)

    async def _arun(self) -> str:
        raise NotImplementedError()
