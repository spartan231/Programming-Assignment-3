import sys
import os
import time
import glob
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from src.PA_3 import FindMaxVal, FindSubsequence


def parse_input(filepath):
    with open(filepath) as f:
        lines = f.read().splitlines()
    n = int(lines[0])
    v = {}
    for i in range(1, n + 1):
        ch, val = lines[i].split()
        v[ch] = int(val)
    A = lines[n + 1]
    B = lines[n + 2]
    return A, B, v


def benchmark(input_dir):
    files = sorted(glob.glob(os.path.join(input_dir, "input_*.in")),
                   key=lambda f: int(os.path.basename(f).split('_')[1].split('.')[0]))

    lengths = []
    runtimes = []

    print(f"{'File':<25} {'Length':>8} {'Time (s)':>12}")
    print("-" * 48)

    for fpath in files:
        A, B, v = parse_input(fpath)
        length = len(A)

        start = time.perf_counter()
        max_val, OPT = FindMaxVal(A, B, v)
        subseq = FindSubsequence(OPT, A, B, v)
        elapsed = time.perf_counter() - start

        lengths.append(length)
        runtimes.append(elapsed)
        print(f"{os.path.basename(fpath):<25} {length:>8} {elapsed:>12.6f}")

    return lengths, runtimes


def plot(lengths, runtimes, out_path):
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(lengths, runtimes, marker='o', linewidth=2, color='steelblue',
            markerfacecolor='white', markeredgewidth=2)
    for x, y in zip(lengths, runtimes):
        ax.annotate(f"{y*1000:.2f}ms", (x, y),
                    textcoords="offset points", xytext=(0, 8),
                    ha='center', fontsize=8)
    ax.set_xlabel("Input String Length (n)", fontsize=12)
    ax.set_ylabel("Runtime (seconds)", fontsize=12)
    ax.set_title("Maximum Value Common Subsequence — Runtime vs Input Size", fontsize=13)
    ax.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig(out_path, dpi=150)
    print(f"\nGraph saved to: {out_path}")


if __name__ == "__main__":
    base = os.path.dirname(os.path.abspath(__file__))
    input_dir = os.path.join(base, "inputs")
    out_graph = os.path.join(base, "runtime_graph.png")

    lengths, runtimes = benchmark(input_dir)
    plot(lengths, runtimes, out_graph)
