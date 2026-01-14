# internship task 1
# fibonacci generator
def fibonacci_generator(n):
    if n <=0:
        return []
    elif n == 1:
        return [0]
    
    seq = [0, 1]
    for i in range (2 , n ):
        seq.append(seq[-1] + seq [-2])

    return seq

print(fibonacci_generator(9))
