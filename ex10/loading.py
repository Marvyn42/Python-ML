import time


def ft_progress(listy):
    start = time.monotonic()
    max_cycle = len(listy)
    start_cycle = time.monotonic()
    for elem in listy:
        time_loop = (time.monotonic() - start_cycle) * (max_cycle-1 - elem)
        pourcent = int(((elem+1)/max_cycle)*30)
        print(end="\x1b[2K")
        print(f"ETA: {time_loop:.2f}s [{int(((elem+1) / max_cycle) * 100):3d} \
%][{pourcent * '='}>{(30 - pourcent) * ' '}] {elem+1}/{max_cycle} \
| elapsed time {time.monotonic() - start:.2f}s", flush=True, end="\r")
        start_cycle = time.monotonic()
        yield elem
    print()


listy = range(3333)
ret = 0
for elem in ft_progress(listy):
    ret += elem
    time.sleep(0.005)
print()
print(ret)
