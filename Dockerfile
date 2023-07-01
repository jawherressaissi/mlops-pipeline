FROM python:3.9.7

WORKDIR /app

# Copy the .ipynb file to the working directory
COPY model.py .

# Install Jupyter Notebook and the required Python packages
USER root

RUN apt-get update && apt-get install -y jq
RUN pip install accelerate transformers peft torch datasets tqdm torchvision torchaudio