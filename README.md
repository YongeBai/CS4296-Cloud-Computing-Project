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

### Results
After running all the experiment, you can find the results in the `results` directory. The structure of the results directory is as follows:
```
results
├── <framework>
│   ├── <framework>_<measurer>_<input_size>_tokens_ot_<output_size>.txt
│   ├── <framework>_<measurer>_<input_size>_tokens_ot_<output_size>_gpu_usage.txt
```

Since the results are too hard to interpret when they are in the raw format, we provide a script to generate the summary of the results. You can run the following command to generate the summary of the results as `combined_results.csv`.

```bash
python3 results.py
```



### Supporting Accelarators(Engines)
1. baseline (Huggingface text generation pipeline)
2. vLLM
3. SGLang
4. ExLLaMaV2

# Abbreviations

- TTFT: Time To First Token
- TPOT: Time Per Output Token