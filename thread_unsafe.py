import threading

n = 0


def foo():
    global n
    n += 1


threads = [threading.Thread(target=foo) for _ in range(10000)]

for t in threads:
    t.start()

for t in threads:
    t.join()

print(n)
