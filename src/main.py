import os

import psutil

if __name__ == "__main__":
    proc = psutil.Process(os.getpid())

    print(proc.memory_info().rss)
