MODEL_NAME=TheBloke/Mistral-7B-Instruct-v0.1-GPTQ
ITERATIONS=2
INPUT_PATH=prompts/10_tokens.txt

export HF_HOME=./.HF_CACHE

# python3 llmperf.py ttft --iterations $ITERATIONS --prompt_file $INPUT_PATH baseline --model $MODEL_NAME
# python3 llmperf.py ttft --iterations $ITERATIONS --prompt_file $INPUT_PATH exllama --model $MODEL_NAME
# python3 llmperf.py ttft --iterations $ITERATIONS --prompt_file $INPUT_PATH vllm --model $MODEL_NAME
python3 llmperf.py ttft --iterations $ITERATIONS --prompt_file $INPUT_PATH sglang --model $MODEL_NAME

python3 llmperf.py tpot --iterations $ITERATIONS --prompt_file $INPUT_PATH sglang --model $MODEL_NAME
# python3 llmperf.py tpot vllm --model $MODEL_NAME
# python3 llmperf.py tpot baseline --model $MODEL_NAME
# python3 llmperf.py tpot --iterations $ITERATIONS exllama --model $MODEL_NAME

# python3 llmperf.py throughput --iterations $ITERATIONS exllama --model $MODEL_NAME

# python3 llmperf.py throughput vllm --model $MODEL_NAME
# python3 llmperf.py throughput baseline --model $MODEL_NAME 
# Script to run tpot on vllm
# python llmperf.py tpot --prompt_file $INPUT_PATH --iterations $ITERATIONS --output_tokens 5 \
#     vllm --model $MODEL_NAME --dtype float16