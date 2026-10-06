import time
import random
import statistics

# =======================================================
# DO NOT MODIFY THE ALGORITHM IMPLEMENTATIONS
# =======================================================

def find_duplicates_slow(data):
    """An O(n^2) algorithm to find duplicates."""
    n = len(data)
    for i in range(n):
        for j in range(i + 1, n):
            if data[i] == data[j]:
                return True
    return False

def find_duplicates_fast(data):
    """An O(n) algorithm to find duplicates."""
    seen = set()
    for item in data:
        if item in seen:
            return True
        seen.add(item)
    return False


# =======================================================
# YOUR TASK: FIX THE BENCHMARKING SCRIPT BELOW
# =======================================================

def benchmark_duplicates():
    """
    Empirically compare the performance of the two duplicate-checking algorithms.

    Both algorithms are tested on identical inputs at increasing sizes.
    Each input is timed over multiple trials, and the median time is reported for each algorithm.
    """
    sizes = (250, 500, 1000, 2000, 3000)
    trials = 7
    rng = random.Random(0)

    algorithms = (
        ("slow", find_duplicates_slow),
        ("fast", find_duplicates_fast),
    )

    print("Duplicate-checking benchmark")
    print("Median of 7 trials")
    print()
    print(f"{'n':>6} {'slow (s)':>12} {'fast (s)':>12} {'speedup':>10}")
    print("-" * 44)

    for size in sizes:
        # Create one identical, duplicate-free input for both algorithms.
        data = list(range(size))
        rng.shuffle(data)

        timings = {
            "slow": [],
            "fast": []
            }

        for trial in range(trials):
            # Alternate execution order to reduce systematic timing bias.
            if trial % 2 == 0:
                ordered_algorithms = algorithms
            else:
                ordered_algorithms = algorithms[::-1]

            for name, algorithm in ordered_algorithms:
                start = time.perf_counter()
                result = algorithm(data)
                elapsed = time.perf_counter() - start

                # Verify that both algorithms produce the expected result.
                if result is not False:
                    raise AssertionError(
                        f"{name} returned {result!r} for a "
                        "duplicate-free input"
                    )
                
                timings[name].append(elapsed)

        slow_median = statistics.median(timings["slow"])
        fast_median = statistics.median(timings["fast"])

        speedup = (
            slow_median / fast_median 
            if fast_median > 0
            else float("inf")
        )

        print(
            f"{size:>6} "
            f"{slow_median:>12.6f} " 
            f"{fast_median:>12.6f} "
            f"{speedup:>9.1f}x"
        )


if __name__ == "__main__":
    benchmark_duplicates()