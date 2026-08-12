from random import randint
inpsize = int(input("Enter you input size "))

array = [] 
for i in range(inpsize):
    array.append(randint(2,200))

print(array)

def insort(A,n):
    comp = 0

    for i in range(1,n):
        key = A[i]
        j=i-1
        while j >= 0:
            comp += 1

            if A[j] > key:
                A[j+1] = A[j]
                j = j-1
            else:
                break

        A[j+1] = key

    return comp
        


print('Before sorting:', array)

comp = insort(array, inpsize)

print('After sorting:', array)
print('no. of comparision', comp)


'''A version suitable for your practical

I would structure your program like this:'''

'''from random import randint
import numpy as np
import matplotlib.pyplot as plt


def insort(A, n):
    comp = 0

    for i in range(1, n):
        key = A[i]
        j = i - 1

        while j >= 0:
            comp += 1

            if A[j] > key:
                A[j + 1] = A[j]
                j = j - 1
            else:
                break

        A[j + 1] = key

    return comp


# 100 input sizes between 30 and 1000
input_sizes = np.linspace(30, 1000, 100, dtype=int)

average_comparisons = []


for n in input_sizes:

    total_comparisons = 0

    # 10 different input instances
    for i in range(10):

        array = []

        for j in range(n):
            array.append(randint(2, 200))

        comparisons = insort(array, n)

        total_comparisons += comparisons

    average = total_comparisons / 10

    average_comparisons.append(average)


# n log n values for comparison
nlogn = []

for n in input_sizes:
    nlogn.append(n * np.log2(n))


# Plot
plt.plot(input_sizes, average_comparisons, label="Insertion Sort")
plt.plot(input_sizes, nlogn, label="n log n")

plt.xlabel("Input Size (n)")
plt.ylabel("Average Number of Comparisons")
plt.title("Insertion Sort: Comparisons vs Input Size")

plt.legend()
plt.grid()

plt.show()'''


'''What this program does

You have:

input_sizes = np.linspace(30, 1000, 100, dtype=int)

This creates 100 different input sizes between 30 and 1000.

Then:

for n in input_sizes:

takes each input size.

Then:

for i in range(10):

creates 10 different random arrays for that particular size.

Then:

comparisons = insort(array, n)

runs insertion sort and gets the number of comparisons.

Finally:

average = total_comparisons / 10

gives you the required average.

One important thing about your randint(2,200)

You currently have:

randint(2, 200)

That's fine if your practical simply says to generate random integers. However, for n > 198, you're necessarily going to have duplicate values.

That's not a problem for insertion sort. In fact, it can be useful to have random data with duplicates.

About the n log n graph

Your practical specifically asks you to compare insertion sort with:

n log n

So:

nlogn.append(n * np.log2(n))

creates the theoretical n log₂n curve.

However, there's an important point for your discussion/conclusion:

Insertion sort has O(n²) average/worst-case behavior, while n log n represents the growth of algorithms such as merge sort/heapsort in their usual comparison-based bounds.

So your graph should show the insertion-sort comparison curve growing faster than n log n as n becomes large.

You can discuss that in your practical as:

The experimental results show that the number of comparisons made by insertion sort increases approximately quadratically with input size. The growth is significantly faster than the n log n curve, which agrees with the theoretical average/worst-case complexity of insertion sort.

One caveat: your exact comparison-counting convention matters. If your instructor expects the comparison count to include the final failed A[j] > key test, the code above does that when j >= 0. If they define comparisons differently, your count may differ slightly.

Also, if this is for your Algorithms lab, I can help you make the code match the practical exactly, including generating the 100 sizes, averaging the 10 runs, storing the results, plotting the graph, and writing the observation/conclusion.'''