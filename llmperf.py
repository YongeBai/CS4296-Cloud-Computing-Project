import argparse
import accelarators.baseline_perf as baseline_perf
import accelarators.vllm_perf as vllm_perf
import accelarators.exllama_perf as exllama_perf
import accelarators.together_perf as together_perf

from timeit import default_timer as timer
from utils import read_prompt_from_file, run_test_n_times


def run_ttft(args):
    measurer = None
    prompt = read_prompt_from_file(args.prompt_file)
    prompt_size = args.prompt_file[8:-4]
    if args.engine == "vllm":
        measurer = vllm_perf.ttft_measurer(prompt, args)
    elif args.engine == "baseline":
        measurer = baseline_perf.ttft_measurer(prompt, args)
    elif args.engine == "exllama":
        measurer = exllama_perf.ttft_measurer(prompt, args)
    elif args.engine == "together":
        measurer = together_perf.ttft_measurer(prompt, args)
    else:
        print(f"TTFT test not implemented for {args.engine}")
        return
    run_test_n_times(measurer, args.iterations, args.test,
                     args.engine, prompt_size)


def run_tpot(args):
    measurer = None
    prompt = read_prompt_from_file(args.prompt_file)
    prompt_size = args.prompt_file[8:-4]
    if args.engine == "vllm":
        measurer = vllm_perf.tpot_measurer(prompt, args)
    elif args.engine == 'baseline':
        measurer = baseline_perf.tpot_measurer(prompt, args)
    elif args.engine == 'exllama':
        measurer = exllama_perf.tpot_measurer(prompt, args)
    elif args.engine == "together":
        measurer = together_perf.tpot_measurer(prompt, args)
    else:
        print(f"TPOT test not implemented for {args.engine}")
        return
    run_test_n_times(measurer, args.iterations, args.test,
                     args.engine, prompt_size, args.output_tokens)


def run_throughput(args):
    measurer = None
    prompt = read_prompt_from_file(args.prompt_file)
    prompt_size = args.prompt_file[8:-4]

    if args.engine == "vllm":
        measurer = vllm_perf.throughput_measurer(prompt, args)
    elif args.engine == "baseline":
        measurer = baseline_perf.throughput_measurer(prompt, args)
    elif args.engine == "exllama":
        measurer = exllama_perf.throughput_measurer(prompt, args)
    elif args.engine == "together":
        measurer = together_perf.throughput_measurer(prompt, args)
    else:
        print(f"throughput test not implemented for {args.engine}")
        return
    run_test_n_times(measurer, args.iterations, args.test,
                     args.engine, prompt_size, args.output_tokens)


def add_engines_parser(base_parser, vllm_batch_size=False):
    engine_parser = base_parser.add_subparsers(
        title="Engine", dest="engine", required=True)
    vllm_parser = engine_parser.add_parser("vllm", help="vLLM Engine")
    vllm_parser.add_argument(
        "--model", type=str, default="", help="The model.")
    vllm_parser.add_argument(
        "--dtype", type=str, default="float16", help="The dtype.")
    vllm_parser.add_argument("--gpu_memory_utilization",
                             type=float, default=0.9, help="GPU Memory fraction")
    if vllm_batch_size:
        vllm_parser.add_argument(
            "--batch_size", type=int, default=128, help="The batch size.")

    baseline_parser = engine_parser.add_parser(
        "baseline", help="just baseline")
    baseline_parser.add_argument(
        "--model", type=str, default="", help="The model.")

    exllama_parser = engine_parser.add_parser(
        "exllama", help="ExLLamaV2")

    exllama_parser.add_argument(
        "--model", type=str, default="", help="The model.")

    together_parser = engine_parser.add_parser(
        "together", help="together.ai api")

    together_parser.add_argument(
        "--model", type=str, default="", help="The model.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="LLMPerf tools to measure LLM performance")

    test_parser = parser.add_subparsers(
        title="Test", dest="test", required=True)

    ttft_parser = test_parser.add_parser(
        "ttft", help="Measure Time To First Token (TTFT)")
    ttft_parser.add_argument("--prompt_file", type=str,
                             help="Path to a file containing the prompt.")
    ttft_parser.add_argument("--iterations", type=int,
                             default=10, help="The iterations parameter.")
    add_engines_parser(ttft_parser)

    tpot_parser = test_parser.add_parser(
        "tpot", help="Measure Time Per Output Token (TPOT)")
    tpot_parser.add_argument("--prompt_file", type=str,
                             help="Path to a file containing the prompt.")
    tpot_parser.add_argument("--iterations", type=int,
                             default=10, help="The iterations parameter.")
    tpot_parser.add_argument("--output_tokens", type=int,
                             default=128, help="Number of tokens to retrieve")
    add_engines_parser(tpot_parser)

    throughput_parser = test_parser.add_parser(
        "throughput", help="Measure Throughput in tokens/second")
    throughput_parser.add_argument("--prompt_file", type=str,
                                   help="Path to a file containing the prompt.")
    throughput_parser.add_argument("--iterations", type=int,
                                   default=10, help="The iterations parameter.")
    throughput_parser.add_argument("--output_tokens", type=int,
                                   default=128, help="Number of tokens to retrieve")
    add_engines_parser(throughput_parser)

    args = parser.parse_args()

    if args.test == "ttft":
        run_ttft(args)
    elif args.test == "tpot":
        run_tpot(args)
    elif args.test == "throughput":
        run_throughput(args)
