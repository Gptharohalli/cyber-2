def bubblesort(a):
    n=len(a)
    for i in range(n-1):
        for j in range(n-1-i):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
a=[21,12,34,22,43,65,76,89,80]
print("Before sorting:",a)
bubblesort(a)
print("After sorting:",a)
