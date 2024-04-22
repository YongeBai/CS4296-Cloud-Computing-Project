from together import Together
from transformers import AutoTokenizer
from timeit import default_timer as timer
import os


def ttft_measurer(prompt, args):
    llm, tokenizer = init_llm(args)
    model = "mistralai/Mistral-7B-Instruct-v0.1"

    def single_request():        
        start = timer()
        llm.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1
            )
        return timer() - start
    return single_request

def tpot_measurer(prompt, args):
    llm, tokenizer = init_llm(args)
    model = "mistralai/Mistral-7B-Instruct-v0.1"
    
    def single_request():
        start_time = timer()
        response = llm.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=args.output_tokens
            )
        end_time = timer()
        response = response.choices[0].message.content
        num_tokens = len(tokenizer.tokenize(response))
        print(f"generated {num_tokens} in {end_time-start_time}s")
        return (end_time-start_time)/num_tokens
    return single_request

def throughput_measurer(prompt, args):
    llm, tokenizer = init_llm(args)
    model = "mistralai/Mistral-7B-Instruct-v0.1"

    def single_request():        
        start_time = timer()
        response = llm.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=args.output_tokens
            )
        end_time = timer()
        response = response.choices[0].message.content
        num_tokens = len(tokenizer.tokenize(response))
        print(f"generated {num_tokens} in {end_time-start_time}s")
        return num_tokens/(end_time-start_time)
    return single_request

def init_llm(args):
    global llm, tokenizer
    try:
        return llm, tokenizer
    except:        
        llm = Together(api_key=os.environ.get("TOGETHER_API_KEY"))
        tokenizer = AutoTokenizer.from_pretrained(args.model, use_fast=True)            

        return llm, tokenizer
