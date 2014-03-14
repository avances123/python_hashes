import timeit


for x in xrange(500):
    # The number 2 has no collisions ()
    time_2  = timeit.timeit("d[2]" ,setup="d = {2:2,10:10,18:18}",number=10000000)
    # The number 10 has one collision ()
    time_10 = timeit.timeit("d[10]",setup="d = {2:2,10:10,18:18}",number=10000000)
    # The number 18 has 3 collisions ()
    time_18 = timeit.timeit("d[18]",setup="d = {2:2,10:10,18:18}",number=10000000)

    print x+1,time_2,time_10,time_18


