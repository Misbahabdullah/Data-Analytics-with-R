def reverse(z):
    n=len(z)
    m=n//2
    is_odd=n%2
    q=[]


    for i in range(n):
        q.append(0)

    for i in range(m):
        q[i]=z[n-i-1]
        q[n-i-1]=z[i]
        if is_odd>0:
            q[m]=z[m]

    return q


print(reverse([1,2,3,4,5]))
