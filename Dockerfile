FROM python:3.10

WORKDIR /usr/app

# Instead of using the requirements.txt file, we can install the packages directly
# This is useful to save time when building the image by caching the layers
# If you have a new package to install, you can put at the "end" of the list
RUN pip install vllm==0.2.1
RUN pip install text-generation==0.6.1