"""Cross-process browser semaphore: at most N Chromium instances at once (2-core box).
usage:  from _sem import slot;  with slot(): ...launch browser..."""
import fcntl, os, time, contextlib, random
N = int(os.environ.get('SB_BROWSER_SLOTS', '3'))
D = '/tmp/sb-browser-slots'
os.makedirs(D, exist_ok=True)

@contextlib.contextmanager
def slot():
    fh = None
    while fh is None:
        order = list(range(N)); random.shuffle(order)
        for i in order:
            f = open(f'{D}/{i}.lock', 'w')
            try:
                fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB); fh = f; break
            except OSError:
                f.close()
        if fh is None:
            time.sleep(0.4 + random.random() * 0.6)
    try:
        yield
    finally:
        try: fcntl.flock(fh, fcntl.LOCK_UN)
        finally: fh.close()
