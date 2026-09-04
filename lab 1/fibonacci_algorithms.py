def fibonacci_recursive(n):
    if n<=1: return n
    return fibonacci_recursive(n-1)+fibonacci_recursive(n-2)

def fibonacci_iterative(n):
    a,b=0,1
    for _ in range(n): a,b=b,a+b
    return a

def fibonacci_dynamic(n):
    if n<=1: return n
    dp=[0]*(n+1); dp[1]=1
    for i in range(2,n+1): dp[i]=dp[i-1]+dp[i-2]
    return dp[n]

if __name__=="__main__":
    n=20
    print(f"Python Fibonacci Programs (n={n})")
    print("Recursive           :",fibonacci_recursive(n))
    print("Iterative           :",fibonacci_iterative(n))
    print("Dynamic Programming :",fibonacci_dynamic(n))
