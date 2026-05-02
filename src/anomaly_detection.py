import numpy as np

def detect_anomalies(data, static_threshold=85):

    static = set(np.where(data > static_threshold)[0])

    z = (data - data.mean()) / (data.std() + 1e-6)
    zscore = set(np.where(np.abs(z) > 2)[0])

    q1, q3 = np.percentile(data, [25, 75])
    iqr = q3 - q1

    iqr_set = set(np.where(
        (data < q1 - 1.5 * iqr) | (data > q3 + 1.5 * iqr)
    )[0])

    # AIOps standard: OR-based detection
    return static | zscore | iqr_set