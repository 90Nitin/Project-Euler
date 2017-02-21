import numpy

all = numpy.arange(1, 1001)

thr_or_fiv = [i for i in all if i % 3 == 0 or i % 5 == 0]

# done

sum(thr_or_fiv)
