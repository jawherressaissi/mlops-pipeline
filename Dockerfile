FROM python:3.9.7

WORKDIR /app

# Install Jupyter Notebook and the required Python packages
USER root

RUN apt-get update && apt-get install -y jq
RUN pip install accelerate transformers peft torch datasets tqdm torchvision torchaudio
RUN mkdir results

ENV RESULTS_DIR=/home/jenkins/results

COPY model.py .