import numpy as np

def inject_failures(cpu, memory, latency):

    # ---- incident A (web-01 issue) ----
    inc_a = np.arange(45, 48)

    cpu[inc_a, 0] = [91, 94, 89]
    memory[inc_a, 0] = [92, 95, 90]
    latency[inc_a, 0] = [85, 110, 92]

    # ---- incident B (app-01 issue) ----
    inc_b = np.arange(120, 123)

    cpu[inc_b, 1] = [95, 98, 93]
    memory[inc_b, 1] = [97, 99, 95]
    latency[inc_b, 1] = [120, 145, 118]

    return cpu, memory, latency