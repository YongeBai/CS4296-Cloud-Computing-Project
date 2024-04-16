MODEL_NAME=TheBloke/Mistral-7B-Instruct-v0.1-GPTQ
ITERATIONS=10
INPUT_PATH=prompts/10_tokens.txt

# Script to run ttft on both
python llmperf.py ttft --prompt_file $INPUT_PATH --iterations $ITERATIONS vllm --model $MODEL_NAME
python llmperf.py ttft --prompt_file $INPUT_PATH --iterations $ITERATIONS baseline --model $MODEL_NAME

# Script to run tpot on vllm
# python llmperf.py tpot --prompt_file $INPUT_PATH --iterations $ITERATIONS --output_tokens 5 \
#     vllm --model $MODEL_NAME --dtype float16