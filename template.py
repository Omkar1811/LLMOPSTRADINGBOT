import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

list_of_files=[
    "tradingbot/__init__.py",
    "tradingbot/helper.py",
    "tradingbot/prompt.py",
    ".env",
    "requirements.txt",
    "setup.py",
    "research/test.ipynb",
    "app.py",
    "test.py",

]

for filepath in list_of_files:
    file_path = Path(filepath)
    filedir,filename = os.path.split(filepath)
    if filedir!="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory {filedir} for the files {filename}")

    if (not os.path.exists(filepath)) or (not os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"Created empty file: {filepath}")
    else:
        logging.info(f"File {filepath} already exists")