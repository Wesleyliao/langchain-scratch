from dropbox.files import FolderMetadata
from langchain.tools.base import BaseTool

from . import dbx


class CreateFolderTool(BaseTool):

    name = "DropboxCreateFolder"
    description = "Tool for creating a new folder. Path should start with a '/'."

    def _run(self, tool_input: str) -> str:
        _ = dbx.files_create_folder(tool_input)
        return ""

    async def _arun(self) -> str:
        raise NotImplementedError()
