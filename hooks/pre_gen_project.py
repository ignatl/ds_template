import os
from pathlib import Path

# Read the cookiecutter context
cookiecutter = "{{ cookiecutter }}"

# Get the parent directory name
parent_dir = Path(os.getcwd()).parent.name

# Set the project name to the parent directory name
project_name = parent_dir

# Update the cookiecutter context
cookiecutter.update({"project_name": project_name})

# Project readable name
cookiecutter.update({"project_readable_name": project_name.replace("_", " ").title()})
