import os
import torch

def get_prompts():
    files = os.listdir("prompts")
    prompts_files = [f for f in files if f.endswith(".txt")]
    prompts = []
    for file in prompts_files:
        with open(f"prompts/{file}", "r") as f:
            prompts.append((file, f.read()))
    return prompts

def run_test_n_times(test, n, test_name, framework, prompt_size):
    file_name = f"{framework}_{test_name}_{prompt_size}"
    with open(f"results/{framework}/{file_name}.txt", "w") as f:
        f.write(file_name+"\n")
        total = 0
        for i in range(n):
            value = test()
            total += value
            f.write(f"Iteration {i}: {value}\n")
        f.write(f"Average: {total/n}\n")

def get_max_gpu_memory():
    max_memory = torch.cuda.max_memory_allocated()
    max_memory_gb = max_memory / (1024 ** 3)

    return max_memory_gb