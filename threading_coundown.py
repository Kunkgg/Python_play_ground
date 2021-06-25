from threading import Thread

n = 100000000


def countdown(n):
    while n > 0:
        n -= 1


t1 = Thread(target=countdown, args=[n // 4])
t2 = Thread(target=countdown, args=[n // 4])
t3 = Thread(target=countdown, args=[n // 4])
t4 = Thread(target=countdown, args=[n // 4])

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

# countdown(n)
