# Cloud Computing project

## Tasks
| Task                                        | Name        | Status |
| ------------------------------------------- | ----------- | ------ |
| Write proposal                              | Yonge       | ---    |
| Write benchmarking script                   | Woojang     | ---    |
| Decide on instance type                     |             | ---    |
| set up and run vllm                         | Joseph      | ---    |

### Installation

1. Clone the project repository:

```git clone https://github.com/YongeBai/CS4296-Cloud-Computing-Project.git```

2. Navigate to the project directory:

```cd CS4296-Cloud-Computing-Project```

3. Install the required Python packages:

```pip install -r requirements.txt```

### Usage

You can run the benchmarking script inside the docker container. You may run the bash script `dev.sh` to start the container and enter the container's shell using development mode.

```bash
sh dev.sh
```

Or you can just run the following command to start the container and run the benchmarking script.

```bash
docker run --rm -it --name <YOUR_CONTAINER_NAME> --gpus all -v $(pwd):/usr/app <YOUR_IMAGE_NAME> bash

```python3 
python3 test_script.py
```

Further, we can use llmperf to test on multiple aspects of the model. For example, we can test the time per output token using vLLM.

```bash
python llmperf.py tpot --prompt_file input_examples/llama2/128_tokens --iterations 10 --output_tokens 5 vllm --model TheBloke/Mistral-7B-Instruct-v0.1-GPTQ --dtype float16
```

# Abbreviations

- TTFT: Time To First Token
- TPOT: Time Per Output Token