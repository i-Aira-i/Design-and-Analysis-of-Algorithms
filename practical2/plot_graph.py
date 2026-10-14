import csv
import matplotlib.pyplot as plt

sizes = []
averages = []
theoretical = []

with open("merge_sort_results.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        sizes.append(int(row["Input Size"]))
        averages.append(float(row["Average Comparisons"]))
        theoretical.append(float(row["n_log2_n"]))

plt.plot(sizes, averages, label="Average Comparisons",
         marker=".", markersize=3)

plt.plot(sizes, theoretical, label="n log2(n)",
         linestyle="--")

plt.xlabel("Input Size (n)")
plt.ylabel("Number of Comparisons")
plt.title("Merge Sort: Comparison Analysis")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("merge_sort_graph.png", dpi=300)
plt.show()