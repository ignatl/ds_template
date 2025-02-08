FROM continuumio/miniconda3:latest

WORKDIR /app

# Copy project files
COPY . .

# Create conda environment
RUN conda create -n python_env python=3.13 -y
SHELL ["/bin/bash", "-c"]
RUN echo "conda activate python_env" >> ~/.bashrc

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry to PATH
ENV PATH="/root/.local/bin:$PATH"

# Install project dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Set the default command
CMD ["/bin/bash"]
