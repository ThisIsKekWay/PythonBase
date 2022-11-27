# Написать рандомайзер без библиотеки Random
import time

def random_number(minimum,maximum):
    for i in range(maximum - minimum):
        now = str(time.perf_counter_ns())
        rnd = float(now[::-1][1:5:])/1000
        print(minimum + rnd*(maximum-minimum))

(random_number(0,4))
