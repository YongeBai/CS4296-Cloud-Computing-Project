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
        max_new_tokens = 1
    )
    start_time = time.perf_counter()
    pipe(prompt)
    return time.perf_counter() - start_time

def tokens_ps(prompt):
    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=512,
    )
    start_time = time.perf_counter()
    response = pipe(prompt)[0]["generated_text"]
    end_time = time.perf_counter()
    num_tokens = len(tokenizer.tokenize(response))

    return num_tokens/(end_time-start_time)
    

if __name__ == "__main__":
    prompts = get_prompts()
    framework = "baseline"    
    os.makedirs(f"results/{framework}", exist_ok=True)
    for prompt_size, prompt in prompts:
        print("ttft test")        
        prompt_size = prompt_size[:-4]

        # time to first token
        run_test_n_times(lambda: ttft(prompt), 10, "ttft", framework, prompt_size)

        #tokens per second
        run_test_n_times(lambda: tokens_ps(prompt), 10, "tokens_ps", framework, prompt_size)
