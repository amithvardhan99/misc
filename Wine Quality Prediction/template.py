import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import logging

from numpy.core.defchararray import rindex

logging.basicConfig(level=logging.INFO,format="[%(asctime)s]: %(message)s")

project_name = "mlProject"

list_of_files = [
    f"src/{project_name}/__init__.py",

    # components
    f"src/{project_name}/components/__init__.py",

    # utils
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",

    # config
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",

    # pipeline
    f"src/{project_name}/pipeline/__init__.py",

    # entity
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",

    # constraints
    f"src/{project_name}/constraints/__init__.py",

    f"config/config.yaml",
    f"params.yaml",
    f"schema.yaml",
    f"main.py",
    f"app.py",
    f"requirements.txt",
    f"setup.py",
    f"research/trials.ipynb",
    f"templates/index.html"
]

for i in list_of_files:
    folder_name,file = os.path.split(i)
    current_folder_path = os.getcwd().replace("\\","/")
    folder_path = current_folder_path + "/" + folder_name
    #print(folder_name," : ",file)
    if folder_name != "":
        os.makedirs(folder_name,exist_ok=True)
        logging.info(f"Creating folder {folder_name}")
        logging.info("")
        if not os.path.exists(folder_name + "/" + file):
            logging.info(f"Creating file {file}")
            with open(folder_name + "/" + file,"w") as f:
                f.write("")
        else:
            logging.info(f"File {file} already exists")
        logging.info("")
    else:
        if not os.path.exists(file):
            logging.info(f"Creating file {file}")
            with open(file,"w") as f:
                f.write("")
        else:
            logging.info(f"File {file} already exists")
        logging.info("")