import os

def get_prompts():
    files = os.listdir("prompts")
    prompts_files = [f for f in files if f.endswith(".txt")]
    prompts = []
    for file in prompts_files:
        with open("prompts/" + file, "r") as f:
            prompts.append(f.read())
    return prompts
    

def run_test_n_times(test, n, test_name, framework):
    file_name = f"{framework}_{test_name}_results"
    with open(file_name+".txt", "w") as f:
        f.write(file_name+"\n")
        total = 0
        for i in range(n):
            value = test()
            total += value
            f.write(f"Iteration {i}: {value}\n")
        f.write(f"Average: {total/n}")

