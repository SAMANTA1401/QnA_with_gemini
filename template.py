import os
from pathlib import Path

list_of_files=[
    "qawithgemini/__init__.py",
    "qawithgemini/components/data_ingestion.py",
    "qawithgemini/components/embedding.py",
    "qawithgemini/components/model_api.py",
    "qawithgemini/logger/logger.py",
    "qawithgemini/exception/exception.py",
    "Data/data.txt",
    "notebook/experiment.ipynb"
    "Experiments/experiment.ipynb",
    "app.py",
    "setup.py",
    "requirements.txt"
        ]


for filepath in list_of_files:
   filepath = Path(filepath)
   filedir, filename = os.path.split(filepath)

   if filedir !="":
      os.makedirs(filedir, exist_ok=True)

   if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
      with open(filepath, 'w') as f:
         pass