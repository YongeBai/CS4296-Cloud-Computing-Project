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


def run_test_n_times(test, n, mesurer_name, framework, prompt_size, output_tokens=-1):
    os.makedirs(f"results/{framework}", exist_ok=True)
    file_name = f"{framework}_{mesurer_name}_{prompt_size}"
    if output_tokens >= 0:
        file_name += f"_ot_{output_tokens}"

    with open(f"results/{framework}/{file_name}.txt", "w") as f_test:
        with open(f"results/{framework}/{file_name}_gpu_usage.txt", "w") as f_gpu:
            f_test.write(file_name+" "+mesurer_name+"\n")
            f_gpu.write(file_name+" GPU USAGE\n")
            total_test = 0
            total_gpu = 0
            for i in range(n):
                value = test()
                gpu_usage = get_max_gpu_memory()
                total_test += value
                total_gpu += gpu_usage
                f_test.write(f"Iteration {i}: {value}\n")
                f_gpu.write(f"Iteration: {str(gpu_usage)} GB\n")
            f_test.write(f"Average: {total_test/n}\n")
            f_gpu.write(f"Average: {total_gpu/n}\n")


async def async_run_test_n_times(test, n, mesurer_name, framework, prompt_size):
    os.makedirs(f"results/{framework}", exist_ok=True)
    file_name = f"{framework}_{mesurer_name}_{prompt_size}"
    with open(f"results/{framework}/{file_name}.txt", "w") as f:
        f.write(file_name+"\n")
        total = 0
        for i in range(n):
            value = await test()
            total += value
            f.write(f"Iteration {i}: {value}\n")
        f.write(f"Average: {total/n}\n")


def get_max_gpu_memory():
    max_memory = torch.cuda.max_memory_allocated()
    max_memory_gb = max_memory / (1024 ** 3)

    return max_memory_gb
