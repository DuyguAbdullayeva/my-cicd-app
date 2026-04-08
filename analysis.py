import numpy as np
import pandas as pd

def compute_statistics(data):
    return {
        "mean": np.mean(data),
        "std": np.std(data),
        "min": np.min(data),
        "max": np.max(data),
    }

if __name__ == "__main__":
    data = [10, 20, 30, 40, 50]
    stats = compute_statistics(data)
    with open("report.txt", "w") as f:
        f.write("=== Data Analysis Report ===\n")
        for key, val in stats.items():
            f.write(f"{key}: {val}\n")
    print("report.txt yaradildi")
