def fib(n):
    if n <= 1:
        return n
    return fib (n - 1) + fib (n - 2)
# Returns the number of ways to
# reach the nth stair
def countWays (s) :
    return fib (s + 1)
# Driver program
s = int (input ("Enter no of steps: " ))
print ("Number of ways =", countWays (s) )
