import sglang as sgl


@sgl.function
def query(s, prompt, max_tokens):    
    s = sgl.gen("answer", max_tokens=max_tokens)

def ttft_measurer(prompt, args):
    tokenizer = init_llm(args)
    print("here")
    def single_request():
        start_time = timer()
        query.run(prompt=prompt, max_tokens=1)        
        return timer() - start_time
    return single_request

def tpot_measurer(prompt, args):
    tokenizer = init_llm(args)

    def single_request():
        start_time = timer()
        state = query.run(prompt=prompt, max_tokens=args.output_tokens)          
        end_time = timer()
        num_tokens = len(tokenizer.tokenize(state["answer"].strip()))
        print(f"generated {num_tokens} in {end_time-start_time}s")
        return (end_time-start_time)/num_tokens
    return single_request

    
def throughput_measurer(prompt, args):
    tokenizer = init_llm(args)

    def single_request():        
        start_time = timer()
        state = query.run(prompt=prompt, max_tokens=args.output_tokens)        
        end_time = timer()
        num_tokens = len(tokenizer.tokenize(state["answer"].strip()))
        print(f"generated {num_tokens} in {end_time-start_time}s")
        return num_tokens/(end_time-start_time)
    return single_request

def init_llm(args):
    global tokenizer
    try:
        return tokenizer
    except:
        runtime = sgl.Runtime(model_path=args.model)
        sgl.set_default_backend(runtime)
        tokenizer = sgl.get_tokenizer()
        return tokenizer

# put this somewhere runtime.shutdown()