import numpy

actual = numpy.random.binomial(10, .6, size=10)
print(actual)

#20 is amount of coin flips
#6 is expected number of heads in the flips
#Formula P(x:n,p) = nCx x px(1-p)n-x

#(20! / (6! × (20 - 6)!)) × (0.50) ^ (6) × (1 - 0.50) ^ (20 - 6)

#Can be translated to 20 amount of days
#10 expected up days. I think minervini mentioned something about how many weeks before something goes up after the VCP

