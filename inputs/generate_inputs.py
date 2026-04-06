import random
import os

random.seed(42)
CHARS = ['a', 'b', 'c']
VALUES = {'a': 2, 'b': 4, 'c': 5}
LENGTHS = [25, 50, 100, 200, 300, 400, 500, 600, 750, 1000]

out_dir = os.path.dirname(os.path.abspath(__file__))

for length in LENGTHS:
    A = ''.join(random.choices(CHARS, k=length))
    B = ''.join(random.choices(CHARS, k=length))
    fname = os.path.join(out_dir, f"input_{length}.in")
    with open(fname, 'w') as f:
        f.write(f"{len(VALUES)}\n")
        for ch, val in VALUES.items():
            f.write(f"{ch} {val}\n")
        f.write(A + "\n")
        f.write(B + "\n")
    print(f"Generated {fname}")
