FROM nvidia/cuda:11.8.0-runtime-ubuntu22.04

WORKDIR /usr/app

RUN apt-get update && apt-get install -y python3.10 python3-pip
RUN apt-get install -y cuda-toolkit-11-8
RUN pip install optimum==1.19.0
RUN pip install transformers==4.40.0
RUN pip install auto-gptq --extra-index-url https://huggingface.github.io/autogptq-index/whl/cu118
RUN pip install text-generation==0.6.1
RUN pip install https://github.com/vllm-project/vllm/releases/download/v0.4.0/vllm-0.4.0+cu118-cp310-cp310-manylinux1_x86_64.whl --extra-index-url https://download.pytorch.org/whl/cu118
RUN pip install cupy-cuda11x==12.1
RUN pip install xformers==0.0.23.post1 --index-url https://download.pytorch.org/whl/cu118
RUN pip install exllamav2==0.0.19
RUN pip install torch==2.1.2 --index-url https://download.pytorch.org/whl/cu118
RUN pip install together