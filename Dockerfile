FROM python:3.10

WORKDIR /usr/app

# Instead of using the requirements.txt file, we can install the packages directly
# This is useful to save time when building the image by caching the layers
# If you have a new package to install, you can put at the "end" of the list
RUN pip install text-generation==0.6.1
RUN pip install vllm==0.2.7

# # fixing problem with vllm
# # https://github.com/vllm-project/vllm/issues/3033#issuecomment-1964061542
RUN pip install cupy-cuda11x==12.1
RUN pip install --force-reinstall torch==2.0.1+cu118 --extra-index-url https://download.pytorch.org/whl/

# # Fixing problem with GPTQ models
RUN pip install optimum
RUN pip install git+https://github.com/huggingface/transformers.git@72958fcd3c98a7afdc61f953aa58c544ebda2f79
RUN pip install auto-gptq --extra-index-url https://huggingface.github.io/autogptq-index/whl/cu118/

