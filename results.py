import pandas as pd
import os

result_path = "results/"

def getFileNames():
    filenames = []
    for framework in os.listdir(result_path):
        for filename in os.listdir(f"{result_path}{framework}"):
            if "gpu_usage" not in filename:
                filenames.append(filename)
    return filenames


def getFeatureFromFilename(filename: str):
    text = filename.replace(".txt", "").replace(
        "_ot", "").replace("tokens", "").replace("__", "_")
    framework = text.split("_")[0]
    measurer = text.split("_")[1]
    prompt_size = text.split("_")[2]
    output_size = "none"
    if "ot" in filename:
        output_size = text.split("_")[3]

    return framework, measurer, prompt_size, output_size


def getResult(filename: str):
    # check if file exists
    if not os.path.isfile(filename):
        print(f"File {filename} does not exist")
        return [0]
    with open(filename, "r") as f:
        lines = f.readlines()
        data = []
        for line in lines:
            if "Iteration" in line:
                data.append(
                    float(line.split(":")[1].replace("GB", "").strip()))
    return data


def combineResults() -> pd.DataFrame:
    df = pd.DataFrame()
    df["framework"] = []
    df["measurer"] = []
    df["prompt_size"] = []
    df["output_size"] = []
    df["iterations"] = []
    df["average"] = []
    df["max"] = []
    df["min"] = []
    df["std"] = []
    df["gpu_usage"] = []

    filenames = getFileNames()
    for filename in filenames:
        framework, measurer, prompt_size, output_size = getFeatureFromFilename(
            filename)
        data = getResult(f"{result_path}{framework}/{filename}")
        if (len(data) == 0):
            data = [0]

        # gpu
        gpu_usage = getResult(
            f"{result_path}{framework}/{filename.replace('.txt', '')}_gpu_usage.txt")
        if (len(gpu_usage) == 0):
            gpu_usage = [0]
        gpu_usage = sum(gpu_usage) / len(gpu_usage)
        if gpu_usage == 0:
            gpu_usage = "none"

        # measurer
        average = sum(data) / len(data)
        max_value = max(data)
        min_value = min(data)
        std = sum([(x - average) ** 2 for x in data]) / len(data)
        df = pd.concat([df, pd.DataFrame({
            "framework": framework,
            "measurer": measurer,
            "prompt_size": prompt_size,
            "iterations": len(data),
            "average": average,
            "max": max_value,
            "min": min_value,
            "std": std,
            "output_size": output_size,
            "gpu_usage": gpu_usage
        }, index=[0])], ignore_index=True)

    return df

data = combineResults()
data = data.sort_values(
    by=["framework", "measurer", "prompt_size", "output_size"])
data.to_csv("combined_results.csv", index=False)