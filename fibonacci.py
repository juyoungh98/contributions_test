fibSequence = list()
for i in range(100):
    fibSequence.append(0)
    if i == 0 or i == 1:
        fibSequence[i] = i
    else:
        fibSequence[i] = fibSequence[i-2] + fibSequence[i-1]

# find specific number from the fibonacci sequence: 233

loc = fibSequence.index(233)

print('233 is the %dth number in the fibonacci sequence.' %(loc+1))