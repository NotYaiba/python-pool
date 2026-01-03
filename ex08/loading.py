from time import time
import sys

def ft_tqdm(lst: range):
    total = len(lst)
    start_time = time()
    for i, item in enumerate(lst, start=1):
        percent = int(i / total * 100)
        bar_length = 60  # bar display length
        filled_length = int(bar_length * i // total)
        bar = '=' * filled_length + '>' + ' ' * (bar_length - filled_length - 1)
        elapsed = time() - start_time

        # carriage return + flush to overwrite line
        sys.stdout.write(f"\r{percent:3}%|[{bar}]| {i}/{total}")
        sys.stdout.flush()

        yield item
    print()  # new line after loop finishes
