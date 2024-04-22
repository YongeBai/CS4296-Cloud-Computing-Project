# Cloud Computing project
## Installation

1. Clone the project repository:

```git clone https://github.com/YongeBai/CS4296-Cloud-Computing-Project.git```

2. Navigate to the project directory:

```cd CS4296-Cloud-Computing-Project```

## Usage

### Docker Image

You can run the benchmarking script inside the docker container. You may run the bash script `dev.sh` to start the container and enter the container's shell using development mode.

```bash
sh dev.sh
```

### Benchmarking

We leverages llmperf to test on multiple aspects of the model. For example, we can test the time per output token using vLLM. For the detailed scripts, refer to the `experiments.sh`.

```bash
sh experiments.sh
```

### Supporting Accelarators(Engines)
1. baseline (Huggingface text generation pipeline)
2. vLLM
3. SGLang
4. ExLLaMaV2

# Abbreviations

- TTFT: Time To First Token
- TPOT: Time Per Output Token