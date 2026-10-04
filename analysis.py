from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def load_data(file_path):
    """Membaca data inferens daripada fail CSV."""
    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"Fail tidak ditemui: {file_path}")

    data = pd.read_csv(file_path)
    return data

def filter_data(data, threshold):
    """Menapis rekod yang confidence-nya sama atau melebihi threshold."""
    filtered_data = data[data["confidence"] >= threshold].copy()
    return filtered_data

def calculate_statistics(data):
    """Mengira statistik asas daripada data inferens."""
    if data.empty:
        return {
            "accepted_records": 0,
            "average_confidence": 0,
            "highest_confidence": 0,
            "lowest_confidence": 0,
            "average_inference_time": 0,
            "object_counts": {},
        }

    return {
        "accepted_records": len(data),
        "average_confidence": np.mean(data["confidence"]),
        "highest_confidence": np.max(data["confidence"]),
        "lowest_confidence": np.min(data["confidence"]),
        "average_inference_time": np.mean(data["inference_time_ms"]),
        "object_counts": data["object_class"].value_counts().to_dict(),
    }

def create_bar_chart(data, output_path):
    """Menghasilkan carta bar jumlah pengesanan mengikut kelas objek."""
    if data.empty:
        print("Carta tidak dihasilkan kerana tiada data.")
        return False

    object_counts = data["object_class"].value_counts()

    plt.figure(figsize=(8, 5))
    bars = plt.bar(
        object_counts.index,
        object_counts.values,
        color=["#1565C0", "#2E7D32", "#F57C00", "#7B1FA2"],
    )

    plt.title("Jumlah Pengesanan Mengikut Kelas Objek")
    plt.xlabel("Kelas Objek")
    plt.ylabel("Jumlah Pengesanan")
    plt.bar_label(bars)
    plt.tight_layout()

    plt.savefig(output_path, dpi=300)
    plt.close()
    return True
