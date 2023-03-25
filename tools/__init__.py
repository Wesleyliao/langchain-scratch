import os

import dropbox
from dotenv import load_dotenv

load_dotenv()
dbx = dropbox.Dropbox(os.getenv("DBX_TOKEN"))
