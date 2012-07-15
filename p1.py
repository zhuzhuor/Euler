#!/usr/bin/env pypy

print sum([i for i in xrange(1000) if (i % 3) == 0 or (i % 5) == 0])
