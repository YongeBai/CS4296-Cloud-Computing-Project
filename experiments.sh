MODEL_NAME=TheBloke/Mistral-7B-Instruct-v0.1-GPTQ

ITERATIONS=10
SHORT_PROMPT=prompts/17_tokens.txt
MID_PROMPT=prompts/191_tokens.txt
LONG_PROMPT=prompts/660_tokens.txt

export HF_HOME=./.HF_CACHE
export TOGETHER_API_KEY=""

echo "Running TTFT tests"
python3 llmperf.py ttft --iterations $ITERATIONS --prompt_file $SHORT_PROMPT baseline --model $MODEL_NAME
python3 llmperf.py ttft --iterations $ITERATIONS --prompt_file $MID_PROMPT baseline --model $MODEL_NAME
python3 llmperf.py ttft --iterations $ITERATIONS --prompt_file $LONG_PROMPT baseline --model $MODEL_NAME

python3 llmperf.py ttft --iterations $ITERATIONS --prompt_file $SHORT_PROMPT exllama --model $MODEL_NAME
python3 llmperf.py ttft --iterations $ITERATIONS --prompt_file $MID_PROMPT exllama --model $MODEL_NAME
python3 llmperf.py ttft --iterations $ITERATIONS --prompt_file $LONG_PROMPT exllama --model $MODEL_NAME

python3 llmperf.py ttft --iterations $ITERATIONS --prompt_file $SHORT_PROMPT together --model $MODEL_NAME
python3 llmperf.py ttft --iterations $ITERATIONS --prompt_file $MID_PROMPT together --model $MODEL_NAME
python3 llmperf.py ttft --iterations $ITERATIONS --prompt_file $LONG_PROMPT together --model $MODEL_NAME

python3 llmperf.py ttft --iterations $ITERATIONS --prompt_file $SHORT_PROMPT vllm --model $MODEL_NAME
python3 llmperf.py ttft --iterations $ITERATIONS --prompt_file $MID_PROMPT vllm --model $MODEL_NAME
python3 llmperf.py ttft --iterations $ITERATIONS --prompt_file $LONG_PROMPT vllm --model $MODEL_NAME

echo "Running TPOT tests"
python3 llmperf.py tpot --iterations $ITERATIONS --prompt_file $SHORT_PROMPT baseline --model $MODEL_NAME
python3 llmperf.py tpot --iterations $ITERATIONS --prompt_file $MID_PROMPT baseline --model $MODEL_NAME
python3 llmperf.py tpot --iterations $ITERATIONS --prompt_file $LONG_PROMPT baseline --model $MODEL_NAME

python3 llmperf.py tpot --iterations $ITERATIONS --prompt_file $SHORT_PROMPT exllama --model $MODEL_NAME
python3 llmperf.py tpot --iterations $ITERATIONS --prompt_file $MID_PROMPT exllama --model $MODEL_NAME
python3 llmperf.py tpot --iterations $ITERATIONS --prompt_file $LONG_PROMPT exllama --model $MODEL_NAME

python3 llmperf.py tpot --iterations $ITERATIONS --prompt_file $SHORT_PROMPT together --model $MODEL_NAME
python3 llmperf.py tpot --iterations $ITERATIONS --prompt_file $MID_PROMPT together --model $MODEL_NAME
python3 llmperf.py tpot --iterations $ITERATIONS --prompt_file $LONG_PROMPT together --model $MODEL_NAME

python3 llmperf.py tpot --iterations $ITERATIONS --prompt_file $SHORT_PROMPT vllm --model $MODEL_NAME
python3 llmperf.py tpot --iterations $ITERATIONS --prompt_file $MID_PROMPT vllm --model $MODEL_NAME
python3 llmperf.py tpot --iterations $ITERATIONS --prompt_file $LONG_PROMPT vllm --model $MODEL_NAME

echo "Running TPOT with Longer Output tests"
python3 llmperf.py tpot --iterations $ITERATIONS --prompt_file $SHORT_PROMPT --output_tokens 512 baseline --model $MODEL_NAME
python3 llmperf.py tpot --iterations $ITERATIONS --prompt_file $MID_PROMPT --output_tokens 512 baseline --model $MODEL_NAME
python3 llmperf.py tpot --iterations $ITERATIONS --prompt_file $LONG_PROMPT --output_tokens 512 baseline --model $MODEL_NAME

python3 llmperf.py tpot --iterations $ITERATIONS --prompt_file $SHORT_PROMPT --output_tokens 512 exllama --model $MODEL_NAME
python3 llmperf.py tpot --iterations $ITERATIONS --prompt_file $MID_PROMPT --output_tokens 512 exllama --model $MODEL_NAME
python3 llmperf.py tpot --iterations $ITERATIONS --prompt_file $LONG_PROMPT --output_tokens 512 exllama --model $MODEL_NAME

python3 llmperf.py tpot --iterations $ITERATIONS --prompt_file $SHORT_PROMPT --output_tokens 512 together --model $MODEL_NAME
python3 llmperf.py tpot --iterations $ITERATIONS --prompt_file $MID_PROMPT --output_tokens 512 together --model $MODEL_NAME
python3 llmperf.py tpot --iterations $ITERATIONS --prompt_file $LONG_PROMPT --output_tokens 512 together --model $MODEL_NAME

python3 llmperf.py tpot --iterations $ITERATIONS --prompt_file $SHORT_PROMPT --output_tokens 512 vllm --model $MODEL_NAME
python3 llmperf.py tpot --iterations $ITERATIONS --prompt_file $MID_PROMPT --output_tokens 512 vllm --model $MODEL_NAME
python3 llmperf.py tpot --iterations $ITERATIONS --prompt_file $LONG_PROMPT --output_tokens 512 vllm --model $MODEL_NAME

echo "Running Throughput tests"
python3 llmperf.py throughput --iterations $ITERATIONS --prompt_file $SHORT_PROMPT baseline --model $MODEL_NAME
python3 llmperf.py throughput --iterations $ITERATIONS --prompt_file $MID_PROMPT baseline --model $MODEL_NAME
python3 llmperf.py throughput --iterations $ITERATIONS --prompt_file $LONG_PROMPT baseline --model $MODEL_NAME

python3 llmperf.py throughput --iterations $ITERATIONS --prompt_file $SHORT_PROMPT exllama --model $MODEL_NAME
python3 llmperf.py throughput --iterations $ITERATIONS --prompt_file $MID_PROMPT exllama --model $MODEL_NAME
python3 llmperf.py throughput --iterations $ITERATIONS --prompt_file $LONG_PROMPT exllama --model $MODEL_NAME

python3 llmperf.py throughput --iterations $ITERATIONS --prompt_file $SHORT_PROMPT together --model $MODEL_NAME
python3 llmperf.py throughput --iterations $ITERATIONS --prompt_file $MID_PROMPT together --model $MODEL_NAME
python3 llmperf.py throughput --iterations $ITERATIONS --prompt_file $LONG_PROMPT together --model $MODEL_NAME

python3 llmperf.py throughput --iterations $ITERATIONS --prompt_file $SHORT_PROMPT vllm --model $MODEL_NAME
python3 llmperf.py throughput --iterations $ITERATIONS --prompt_file $MID_PROMPT vllm --model $MODEL_NAME
python3 llmperf.py throughput --iterations $ITERATIONS --prompt_file $LONG_PROMPT vllm --model $MODEL_NAME

echo "Running Throughput tests with Longer Output"
python3 llmperf.py throughput --iterations $ITERATIONS --prompt_file $SHORT_PROMPT --output_tokens 512 baseline --model $MODEL_NAME
python3 llmperf.py throughput --iterations $ITERATIONS --prompt_file $MID_PROMPT baseline --model $MODEL_NAME
python3 llmperf.py throughput --iterations $ITERATIONS --prompt_file $LONG_PROMPT baseline --model $MODEL_NAME

python3 llmperf.py throughput --iterations $ITERATIONS --prompt_file $SHORT_PROMPT --output_tokens 512 exllama --model $MODEL_NAME
python3 llmperf.py throughput --iterations $ITERATIONS --prompt_file $MID_PROMPT exllama --model $MODEL_NAME
python3 llmperf.py throughput --iterations $ITERATIONS --prompt_file $LONG_PROMPT exllama --model $MODEL_NAME

python3 llmperf.py throughput --iterations $ITERATIONS --prompt_file $SHORT_PROMPT --output_tokens 512 together --model $MODEL_NAME
python3 llmperf.py throughput --iterations $ITERATIONS --prompt_file $MID_PROMPT together --model $MODEL_NAME
python3 llmperf.py throughput --iterations $ITERATIONS --prompt_file $LONG_PROMPT together --model $MODEL_NAME

python3 llmperf.py throughput --iterations $ITERATIONS --prompt_file $SHORT_PROMPT --output_tokens 512 vllm --model $MODEL_NAME
python3 llmperf.py throughput --iterations $ITERATIONS --prompt_file $MID_PROMPT vllm --model $MODEL_NAME
python3 llmperf.py throughput --iterations $ITERATIONS --prompt_file $LONG_PROMPT vllm --model $MODEL_NAME
