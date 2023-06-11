FROM python:3.9.7

WORKDIR /app

# Copy the .ipynb file to the working directory
COPY peft_lora_seq2seq.ipynb .

# Install Jupyter Notebook and the required Python packages
RUN pip install accelerate transformers peft torch datasets tqdm torchvision torchaudio

# Start the Jupyter Notebook server
CMD ["python3.9", "peft_lora_seq2seq.ipynb"]