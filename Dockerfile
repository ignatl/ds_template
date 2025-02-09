FROM continuumio/miniconda3:latest

WORKDIR /app

# Copy project files
COPY . .

# Create and activate conda environment
SHELL ["/bin/bash", "-c"]
RUN conda init bash && \
    source ~/.bashrc && \
    conda create -n python_env python=3.13 -y && \
    eval "$(conda shell.bash hook)" && \
    conda activate python_env && \
    python -m pip install --user poetry && \
    export PATH="/root/.local/bin:$PATH" && \
    poetry --version && \
    poetry install --no-interaction --no-ansi && \
    echo "conda activate python_env" >> ~/.bashrc

# Add Poetry to PATH for subsequent commands
ENV PATH="/root/.local/bin:$PATH"

# Set the default command
CMD ["/bin/bash"]
