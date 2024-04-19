import os
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
    settings = ExLlamaV2Sampler.Settings()
    settings.disallow_tokens(tokenizer, [tokenizer.eos_token_id])
    llm.warmup()
    
    def single_request():
        start = timer()
        llm.generate_simple(prompt, settings, num_tokens=1)
        return timer() - start
    return single_request

def tpot_measurer(prompt, args):
    llm, tokenizer = init_llm(args)
    settings = ExLlamaV2Sampler.Settings()
    settings.disallow_tokens(tokenizer, [tokenizer.eos_token_id])
    llm.warmup()        
    def single_request():
        start_time = timer()
        response = llm.generate_simple(prompt, settings, num_tokens=args.output_tokens)
        end_time = timer()
        print(f"generated {args.output_tokens} in {end_time-start_time}s")
        return (end_time-start_time)/args.output_tokens
    return single_request

def throughput_measurer(prompt, args):
    llm, tokenizer = init_llm(args)
    settings = ExLlamaV2Sampler.Settings()
    settings.disallow_tokens(tokenizer, [tokenizer.eos_token_id])
    llm.warmup()        

    def single_request():        
        start_time = timer()
        response = llm.generate_simple(prompt, settings, num_tokens=args.output_tokens)
        end_time = timer()        
        print(f"generated {args.output_tokens} in {end_time-start_time}s")
        return args.output_tokens/(end_time-start_time)
    return single_request

def init_llm(args):
    global llm, tokenizer
    try:
        return llm, tokenizer
    except:
        user, model = args.model.split("/")
        # model_directory = f"./.HF_CACHE/hub/models--{user}--{model}/snapshots/6ae1e4ae2cfbaf107c705ed722ec243b4f88014d"

        snapshots_path = f"./.HF_CACHE/hub/models--{user}--{model}/snapshots"
        first_directory = os.listdir(snapshots_path)[0]        

        model_directory = os.path.join(snapshots_path, first_directory) if first_directory else None

        config = ExLlamaV2Config(model_directory)
        model = ExLlamaV2(config)
        cache = ExLlamaV2Cache(model, lazy = True)
        model.load_autosplit(cache)
        tokenizer = ExLlamaV2Tokenizer(config)
        llm = ExLlamaV2BaseGenerator(model, cache, tokenizer)
        
        return llm, tokenizer
