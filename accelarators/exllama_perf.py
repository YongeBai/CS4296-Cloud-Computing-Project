import sys, os
from timeit import default_timer as timer

from exllamav2 import(
    ExLlamaV2,
    ExLlamaV2Config,
    ExLlamaV2Cache,
    ExLlamaV2Tokenizer,
)

from exllamav2.generator import (
    ExLlamaV2BaseGenerator,
    ExLlamaV2Sampler
)

def ttft_measurer(prompt, args):
    llm, tokenizer = init_llm(args)
    llm.warmup()
    
    def single_request():
        start = timer()
        llm.generate_simple(prompt, max_new_tokens=1)
        return timer() - start
    return single_request

def tpot_measurer(prompt, args):
    llm, tokenizer = init_llm(args)
    settings = ExLlamaV2Sampler.Settings()
    settings.disallow_tokens(tokenizer, [tokenizer.eos_token_id])
    llm.warmup()        
    def single_request():
        start_time = timer()
        response = llm.generate_simple(prompt, max_new_tokens=args.output_tokens)
        end_time = timer()
        print(f"generated {num_tokens} in {end_time-start_time}s")
        return (end_time-start_time)/args.output_tokens
    return single_request

def throughput_measurer(prompt, args):
    llm, tokenizer = init_llm(args)
    settings = ExLlamaV2Sampler.Settings()
    settings.disallow_tokens(tokenizer, [tokenizer.eos_token_id])
    llm.warmup()        

    def single_request():        
        start_time = timer()
        response = llm.generate_simple(prompt, max_new_tokens=args.output_tokens)
        end_time = timer()        
        print(f"generated {num_tokens} in {end_time-start_time}s")
        return args.output_tokens/(end_time-start_time)
    return single_request

def init_llm(args):
    global llm, tokenizer
    try:
        return llm, tokenizer
    except:
        model_directory =  args.model

        config = ExLlamaV2Config(model_directory)
        model = ExLlamaV2(config)
        cache = ExLlamaV2Cache(model, lazy = True)
        model.load_autosplit(cache)
        tokenizer = ExLlamaV2Tokenizer(config)
        llm = ExLlamaV2BaseGenerator(model, cache, tokenizer)
        
        return llm, tokenizer
