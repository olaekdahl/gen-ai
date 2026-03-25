FROM python:3.10-slim

RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
RUN pip install transformers flask

ENV HF_HOME=/tmp/hf_home

RUN python -c "from transformers import pipeline; pipeline('text-generation', model='distilgpt2')"

COPY app.py /app/app.py

WORKDIR /app

CMD ["python", "app.py"]
