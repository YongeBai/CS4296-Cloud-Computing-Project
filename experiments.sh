MODEL_NAME=TheBloke/Mistral-7B-Instruct-v0.1-GPTQ

ITERATIONS=1
# INPUT_PATH=prompts/10_tokens.txt

export HF_HOME=./.HF_CACHE
export TOGETHER_API_KEY="cff8f3a535c305a959cecce468e51ee0ceeae78dec8e580368cb7aa8c85798f0"

# python3 llmperf.py ttft --iterations $ITERATIONS baseline --model $MODEL_NAME
python3 llmperf.py ttft --iterations $ITERATIONS exllama --model $MODEL_NAME
python3 llmperf.py ttft --iterations $ITERATIONS together --model $MODEL_NAME
# python3 llmperf.py ttft --iterations $ITERATIONS vllm --model $MODEL_NAME

# python3 llmperf.py tpot vllm --model $MODEL_NAME
# python3 llmperf.py tpot baseline --model $MODEL_NAME
python3 llmperf.py tpot --iterations $ITERATIONS exllama --model $MODEL_NAME
python3 llmperf.py tpot --iterations $ITERATIONS together --model $MODEL_NAME
# python3 llmperf.py tpot --iterations $ITERATIONS exllama --model $MODEL_NAME

# python3 llmperf.py throughput --iterations $ITERATIONS exllama --model $MODEL_NAME

# python3 llmperf.py throughput vllm --model $MODEL_NAME
# python3 llmperf.py throughput baseline --model $MODEL_NAME 
# Script to run tpot on vllm
# python llmperf.py tpot --prompt_file $INPUT_PATH --iterations $ITERATIONS --output_tokens 5 \
#     vllm --model $MODEL_NAME --dtype float16