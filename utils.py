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


def read_prompt_from_file(file_path):
    with open(file_path, 'r') as file:
        prompt = file.read()
    return prompt


def run_test_n_times(test, n, mesurer_name, framework, prompt_size):
    os.makedirs(f"results/{framework}", exist_ok=True)
    file_name = f"{framework}_{mesurer_name}_{prompt_size}"
    with open(f"results/{framework}/{file_name}.txt", "w") as f:
        f.write(file_name+"\n")
        total = 0
        for i in range(n):
            value = test()
            total += value
            f.write(f"Iteration {i}: {value}\n")
        f.write(f"Average: {total/n}\n")
    # vram usage
    with open(f"results/{framework}/{framework}_gpu_usage", "w") as f:
        f.write(f"VRAM: {str(get_max_gpu_memory())} GB")


def get_max_gpu_memory():
    max_memory = torch.cuda.max_memory_allocated()
    max_memory_gb = max_memory / (1024 ** 3)

    return max_memory_gb
