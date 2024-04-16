from vllm import LLM, SamplingParams
import torch
import time

lm = LLM(
    "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    dtype='float16',
    gpu_memory_utilization=1.0
)

sampling_params = SamplingParams(max_tokens=512)

# Sample input
input = "The quick brown fox jumps over the lazy dog."

# Benchmark the model
start = time.time()
output = lm.generate(input, sampling_params=sampling_params)
end = time.time()
time_taken = end - start
print(f"Time taken: {time_taken:.2f}s")

# Calculate generated tokens per second
num_tokens = len(output)
tokens_per_second = num_tokens / time_taken
print(f"Tokens per second: {tokens_per_second:.2f}")

# Benchmark GPU usage
gpu_memory = torch.cuda.max_memory_allocated() / 1024 ** 2
print(f"GPU memory used: {gpu_memory:.2f}MB")
