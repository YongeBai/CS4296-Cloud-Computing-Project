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
        print(f"generated {num_tokens} in {end_time-start_time}s")
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
        start_time = timer()
        response = pipe(prompt)[0]["generated_text"]
        end_time = timer()
        num_tokens = len(tokenizer.tokenize(response))
        print(f"generated {num_tokens} in {end_time-start_time}s")
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
        tokenizer = AutoTokenizer.from_pretrained(
            args.model, use_fast=True)
        
        return llm, tokenizer

