def fibonacci(n):
    F = [0]*(n+1) #all initialize with 0
    
    if n<=1:
        return n
    F[0] = 0
    F[1] = 1

    for i in range(2,n+1):
        F[i] = F[i-2]+ F[i-1]
        
    return F[n]





#Driver Code
Term = int(input('Enter Term : '))
fibonacci(Term)
print(f'Your Answer is: {fibonacci(Term)}')