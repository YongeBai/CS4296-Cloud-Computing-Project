FROM nvidia/cuda:11.8.0-runtime-ubuntu22.04

WORKDIR /usr/app

RUN apt-get update && apt-get install -y python3.10 python3-pip
RUN apt-get install -y cuda-toolkit-11-8
RUN pip install optimum==1.19.0
RUN pip install transformers==4.40.0
RUN pip install auto-gptq --extra-index-url https://huggingface.github.io/autogptq-index/whl/cu118
RUN pip install text-generation==0.6.1
RUN pip install xformers==0.0.23.post1 --index-url https://download.pytorch.org/whl/cu118
RUN pip install exllamav2==0.0.19
RUN pip install torch==2.1.2 --index-url https://download.pytorch.org/whl/cu118
RUN pip install together
RUN pip install vllm==0.2.7
RUN pip -q install --upgrade fschat accelerate autoawq vllm
RUN pip install torch==2.1.0+cu121 torchvision==0.16.0+cu121 torchaudio==2.1.0 torchtext==0.16.0+cpu torchdata==0.7.0 --index-url https://download.pytorch.org/whl/cu121

