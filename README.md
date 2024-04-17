# Cloud Computing project
## Installation

1. Clone the project repository:

```git clone https://github.com/YongeBai/CS4296-Cloud-Computing-Project.git```

2. Navigate to the project directory:

```cd CS4296-Cloud-Computing-Project```

3. Install the required Python packages:

```pip install -r requirements.txt```

## Usage

### Docker Image

You can run the benchmarking script inside the docker container. You may run the bash script `dev.sh` to start the container and enter the container's shell using development mode.

```bash
sh dev.sh
```

Or you can just run the following command to start the container and run the benchmarking script.

```bash
docker run --rm -it --name <YOUR_CONTAINER_NAME> --gpus all -v $(pwd):/usr/app <YOUR_IMAGE_NAME> bash
```
### Benchmarking

We leverages llmperf to test on multiple aspects of the model. For example, we can test the time per output token using vLLM. For the detailed scripts, refer to the `experiments.sh`.

```bash
sh experiments.sh
```

### Supporting Accelarators(Engines)
1. baseline(This is just a baseline model without any accelarators)
2. vllm

# Abbreviations

- TTFT: Time To First Token
- TPOT: Time Per Output Token