MODEL_NAME=TheBloke/Mistral-7B-Instruct-v0.1-GPTQ
ITERATIONS=10
INPUT_PATH=prompts/10_tokens.txt

export HF_HOME=./.HF_CACHE

# # Script to run ttft on both
# python3 llmperf.py ttft vllm --prompt_files $INPUT_PATH --iterations $ITERATIONS --model $MODEL_NAME
# python3 llmperf.py ttft baseline --prompt_files $INPUT_PATH --iterations $ITERATIONS --model $MODEL_NAME

# python3 llmperf.py ttft vllm --model $MODEL_NAME
# python3 llmperf.py ttft baseline --model $MODEL_NAME
python3 llmperf.py ttft exllama --model $MODEL_NAME

# python3 llmperf.py tpot vllm --model $MODEL_NAME
# python3 llmperf.py tpot baseline --model $MODEL_NAME

# python3 llmperf.py throughput vllm --model $MODEL_NAME
python3 llmperf.py throughput baseline --model $MODEL_NAME  --iternations 5
# Script to run tpot on vllm
# python llmperf.py tpot --prompt_file $INPUT_PATH --iterations $ITERATIONS --output_tokens 5 \
#     vllm --model $MODEL_NAME --dtype float16