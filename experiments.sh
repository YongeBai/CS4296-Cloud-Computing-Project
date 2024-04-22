MODEL_NAME=TheBloke/Mistral-7B-Instruct-v0.1-GPTQ

ITERATIONS=1
SHORT_PROMPT=prompts/10_tokens.txt
MID_PROMPT=prompts/191_tokens.txt
LONG_PROMPT=prompts/660_tokens.txt

export HF_HOME=./.HF_CACHE
export TOGETHER_API_KEY="cff8f3a535c305a959cecce468e51ee0ceeae78dec8e580368cb7aa8c85798f0"

# TTFT tests
python3 llmperf.py ttft --iterations $ITERATIONS --prompt_file $SHORT_PROMPT baseline --model $MODEL_NAME
python3 llmperf.py ttft --iterations $ITERATIONS --prompt_file $SHORT_PROMPT exllama --model $MODEL_NAME
python3 llmperf.py ttft --iterations $ITERATIONS --prompt_file $SHORT_PROMPT together --model $MODEL_NAME

# TPOT tests
python3 llmperf.py tpot --iterations $ITERATIONS --prompt_file $SHORT_PROMPT baseline --model $MODEL_NAME
# python3 llmperf.py tpot --iterations $ITERATIONS --prompt_file $MID_PROMPT baseline --model $MODEL_NAME
# python3 llmperf.py tpot --iterations $ITERATIONS --prompt_file $LONG_PROMPT baseline --model $MODEL_NAME

python3 llmperf.py tpot --iterations $ITERATIONS --prompt_file $SHORT_PROMPT exllama --model $MODEL_NAME
# python3 llmperf.py tpot --iterations $ITERATIONS --prompt_file $MID_PROMPT exllama --model $MODEL_NAME
# python3 llmperf.py tpot --iterations $ITERATIONS --prompt_file $LONG_PROMPT exllama --model $MODEL_NAME


python3 llmperf.py tpot --iterations $ITERATIONS --prompt_file $SHORT_PROMPT together --model $MODEL_NAME
# python3 llmperf.py tpot --iterations $ITERATIONS --prompt_file $MID_PROMPT together --model $MODEL_NAME
# python3 llmperf.py tpot --iterations $ITERATIONS --prompt_file $LONG_PROMPT together --model $MODEL_NAME

# throughput tests
python3 llmperf.py throughput --iterations $ITERATIONS --prompt_file $SHORT_PROMPT baseline --model $MODEL_NAME
# python3 llmperf.py throughput --iterations $ITERATIONS --prompt_file $MID_PROMPT baseline --model $MODEL_NAME
# python3 llmperf.py throughput --iterations $ITERATIONS --prompt_file $LONG_PROMPT baseline --model $MODEL_NAME


python3 llmperf.py throughput --iterations $ITERATIONS --prompt_file $SHORT_PROMPT exllama --model $MODEL_NAME
# python3 llmperf.py throughput --iterations $ITERATIONS --prompt_file $MID_PROMPT exllama --model $MODEL_NAME
# python3 llmperf.py throughput --iterations $ITERATIONS --prompt_file $LONG_PROMPT exllama --model $MODEL_NAME


python3 llmperf.py throughput --iterations $ITERATIONS --prompt_file $SHORT_PROMPT together --model $MODEL_NAME
# python3 llmperf.py throughput --iterations $ITERATIONS --prompt_file $MID_PROMPT together --model $MODEL_NAME
# python3 llmperf.py throughput --iterations $ITERATIONS --prompt_file $LONG_PROMPT together --model $MODEL_NAME

