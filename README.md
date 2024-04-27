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

Note that for together.ai, it requires the API key to run the benchmarking. You can get the API key from the [together.ai](https://together.ai/). After getting the API key, you can set the API variable `TOGETHER_API_KEY` in the `experiments.sh`. If you do not have the API key, you can just comment out the line for the together.ai.

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

### Charts
After generating the summary of the results, you can generate the charts using the jupyter notebook `graphing.ipynb`. You can run the entire notebook to generate the charts. The charts will be saved in the `charts` directory.


## Customization
The experiment have arguments to customize the experiment. You can modify the `experiments.sh` to customize the experiment. The basic structure of the experiment is as follows:

```bash
python3 llmperf.py \
    <measurer> \
    --iterations <num_iterations> \
    --prompt_file <prompt_file_path> \
     --output_tokens <output_size> \ # not supported for ttft
    <framework> \
    --model <model> \

```


- `measurer`: The measurer to test. The supported measurers are `ttft`, `tpot`, and `throughput`.
- `num_iterations`: The number of iterations to test.
- `prompt_file_path`: The path to the prompt file.
- `output_size`: The number of output tokens to generate.
- `framework`: The framework to test. The supported frameworks are `vllm`, `together`, `exllama`, and `baseline`.
- `model`: The model to test.




### Supporting Accelarators(Engines)
1. baseline (Huggingface text generation pipeline)
2. vLLM
3. SGLang
4. ExLLaMaV2

# Abbreviations

- TTFT: Time To First Token
- TPOT: Time Per Output Token