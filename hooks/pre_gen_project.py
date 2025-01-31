import os
from pathlib import Path

# Get the parent directory name
parent_dir = Path(os.getcwd()).parent.name

# Set the project name to the parent directory name
project_name = parent_dir

# Update the cookiecutter context
cookiecutter = {"project_name": project_name}

# Project readable name
cookiecutter["project_readable_name"] = project_name.replace("_", " ").title()
