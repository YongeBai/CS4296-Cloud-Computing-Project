FROM nvidia/cuda:11.8.0-runtime-ubuntu22.04

WORKDIR /usr/app

RUN apt-get update && apt-get install -y python3.10 python3-pip

RUN apt-get install -y cuda-toolkit-11-8

# Instead of using the requirements.txt file, we can install the packages directly
# This is useful to save time when building the image by caching the layers
# If you have a new package to install, you can put at the "end" of the list

# TODO: set versions for transformers and optimum

# Fixing problem with GPTQ models
RUN pip install torch==2.1.2 --index-url https://download.pytorch.org/whl/cu118
RUN pip install optimum==1.19.0
RUN pip install transformers==4.40.0
# RUN pip install git+https://github.com/huggingface/transformers.git@72958fcd3c98a7afdc61f953aa58c544ebda2f79
RUN pip install auto-gptq --extra-index-url https://huggingface.github.io/autogptq-index/whl/cu118

# downgrading vllm specified here
# https://github.com/vllm-project/vllm/issues/2797
RUN pip install text-generation==0.6.1
RUN pip install vllm==0.4.0 

# fixing problem with vllm
# https://github.com/vllm-project/vllm/issues/3033#issuecomment-1964061542
RUN pip install cupy-cuda11x==12.1
RUN pip install xformers==0.0.23.post1 --index-url https://download.pytorch.org/whl/cu118

# RUN pip install --force-reinstall torch==2.0.1+cu118 --extra-index-url https://download.pytorch.org/whl/

RUN pip install exllamav2==0.0.12
# Patch
# RUN pip install torch==2.1.2


