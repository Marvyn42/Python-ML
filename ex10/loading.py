import sys
import time


def ft_progress(listy):
    start = time.monotonic()
    max_cycle = len(listy)
    start_cycle = time.monotonic()
    for elem in listy:
        time_cycle = (time.monotonic() - start_cycle) * (max_cycle - elem+1)
        print(end="\x1b[2K")
        print(f"ETA: {time_cycle:.2f}s [{int(((elem+1) / max_cycle) * 100):3d}%][{}>  ] {elem+1}/{max_cycle} | elapsed time {time.monotonic() - start:.2f}s", flush=True, end="\r")
        start_cycle = time.monotonic()
        yield elem
    print()


listy = range(300)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    time.sleep(0.01)
print()
print(ret)
