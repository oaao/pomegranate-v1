import time

'''
A. Manual, repeated version:

t_identifier = time.time()
# do stuff
print("--- %s seconds ---\n" % (time.time() - t_identifier))
'''

'''
B. Defining a class, running code inside "with" instantiation:

NOTE - "breaks scope"; method A still more advisable given this criterion.
'''


class Interval():
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.stop = time.time()
        self.duration = self.stop - self.start


with Interval() as d:
    print([i for i in range(10)])

print('--- %.04f seconds ---\n' % d.duration)

'''
C. Create a function decorator "@timed".

# TODO
'''