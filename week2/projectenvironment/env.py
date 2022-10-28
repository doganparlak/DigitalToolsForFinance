from dotenv import dotenv_values
from cookiecutter.main import cookiecutter

config = dotenv_values(".env")

git = config["RESEARCH_PATH"]

cookiecutter(git)