# universal modifiers for functions
import time

def timed():
    pass


def logged():
    pass


def rate_limited(max_per_sec):
    # Refactored from: http://stackoverflow.com/a/667706
    # Used under the MIT License with reasonable attribution as per Stack Overflow policy dating 2016-03-01.
    min_interval = 1.0 / float(max_per_sec)

    def decorate(func):
        last_called = [0.0]

        def rate_limited_function(*args, **kwargs):
            elapsed = time.clock() - last_called[0]
            left_to_wait = min_interval - elapsed
            if left_to_wait > 0:
                time.sleep(left_to_wait)
            ret = func(*args, **kwargs)
            last_called[0] = time.clock()
            return ret
        return rate_limited_function
    return decorate
