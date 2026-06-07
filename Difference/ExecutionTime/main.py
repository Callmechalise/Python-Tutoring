import time

limit = 1_000_000_000

start = time.perf_counter()

i = 0
while i < limit:
    i += 1

end = time.perf_counter()

print("Counted to", limit)
print("Time taken:", end - start, "seconds")