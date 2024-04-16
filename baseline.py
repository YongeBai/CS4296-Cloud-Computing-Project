from utils import *
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import time

model_name_or_path = "TheBloke/Mistral-7B-Instruct-v0.1-GPTQ"
model = AutoModelForCausalLM.from_pretrained(
    model_name_or_path, device_map="auto", trust_remote_code=False, revision="main"
)

tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, use_fast=True)

def ttft(prompt):
    
    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=1,
    )
    start_time = time.perf_counter()
    pipe(prompt)
    return time.perf_counter() - start_time

if __name__ == "__main__":
    prompts = get_prompts()
    framework = "baseline"    

    for prompt in prompts:
        print("ttft test")
        run_test_n_times(ttft(prompts), 5, "ttft", framework)
