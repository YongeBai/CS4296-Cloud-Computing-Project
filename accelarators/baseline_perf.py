from utils import *
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from timeit import default_timer as timer


def ttft_measurer(prompt, args):
    llm, tokenizer = init_llm(args)

    def single_request():
        pipe = pipeline(
            "text-generation",
            model=llm,
            tokenizer=tokenizer,
            max_new_tokens=1
        )
        start = timer()
        pipe(prompt)
        return timer() - start
    return single_request

def tpot_measurer(prompt, args):
    llm, tokenizer = init_llm(args)
    def single_request():
        pipe = pipeline(
            "text-generation",
            model=llm,
            tokenizer=tokenizer,
            max_new_tokens=args.output_tokens,
        )
        start_time = timer()
        response = pipe(prompt)[0]["generated_text"]
        end_time = timer()
        num_tokens = len(tokenizer.tokenize(response))
        return (end_time-start_time)/num_tokens
    return single_request

def throughput_measurer(prompt, args):
    llm, tokenizer = init_llm(args)
    def single_request():
        pipe = pipeline(
            "text-generation",
            model=llm,
            tokenizer=tokenizer,
            max_new_tokens=args.output_tokens,
        )
        start = timer()
        response = pipe(prompt)[0]["generated_text"]
        end_time = timer()
        num_tokens = len(tokenizer.tokenize(response))
        return num_tokens/(end_time-start_time)
    return single_request

def init_llm(args):
    global llm, tokenizer
    try:
        return llm, tokenizer
    except:
        llm = AutoModelForCausalLM.from_pretrained(
            args.model, device_map="auto", trust_remote_code=False, revision="main"
        )
        llm.config.pad_token_id = llm.config.eos_token_id
        tokenizer = AutoTokenizer.from_pretrained(
            args.model, use_fast=True)
        
        return llm, tokenizer


# if __name__ == "__main__":
#     prompts = get_prompts()
#     framework = "baseline"
#     os.makedirs(f"results/{framework}", exist_ok=True)
#     for prompt_size, prompt in prompts:
#         print("ttft test")
#         prompt_size = prompt_size[:-4]

#         # time to first token
#         run_test_n_times(lambda: ttft(prompt), 10,
#                          "ttft", framework, prompt_size)

#         # tokens per second
#         run_test_n_times(lambda: tokens_ps(prompt), 10,
#                          "tokens_ps", framework, prompt_size)

#     # vram usage
#     with open(f"results/{framework}/{framework}_gpu_usage", "w") as f:
#         f.write(f"VRAM: {str(get_max_gpu_memory())} GB")
