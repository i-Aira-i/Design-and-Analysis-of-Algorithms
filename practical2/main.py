
import random
import math
import csv
import merge_sort


# Demonstration
arr = [38, 27, 43, 3, 9, 82, 10]

merge_sort.comparisons = 0
merge_sort.merge_sort(arr, 0, len(arr) - 1)

print("Sorted array:", arr)
print("Number of comparisons:", merge_sort.comparisons)


# Experimental analysis
with open("merge_sort_results.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        "Input Size",
        "Average Comparisons",
        "n_log2_n"
    ])

    print("\nSize\tAverage Comparisons\tn log2(n)")

    for t in range(100):
        n = 30 + (t * 970) // 99
        total_comparisons = 0

        for trial in range(10):
            arr = [random.randint(0, 100000) for _ in range(n)]

            merge_sort.comparisons = 0
            merge_sort.merge_sort(arr, 0, len(arr) - 1)

            total_comparisons += merge_sort.comparisons

        average = total_comparisons / 10
        theoretical = n * math.log2(n)

        writer.writerow([
            n,
            round(average, 2),
            round(theoretical, 2)
        ])

        print(f"{n}\t{average:.2f}\t\t{theoretical:.2f}")

print("\nResults saved to merge_sort_results.csv")