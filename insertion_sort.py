A=[20,10,8,5,2]
bi_count=[0,0,0,0,0,0,0,0,0,0,0]
def insertion_sort(A,bi_count):
    n=len(A)
    bi_count[1]+=1
    for i in range(1,n):
        bi_count[2]+=3
        temp=A[i]
        bi_count[3]+=1
        for j in range(i-1,-2,-1):
            bi_count[4]+=3
            if(j>=0 and A[j]>temp):
                bi_count[5]+=1
                A[j+1]=A[j]
                bi_count[6]+=1
            else:
                bi_count[8]+=1
                break
        A[j+1]=temp
        bi_count[9]+=1
    bi_count[10]+=1
    return A,bi_count      
print(insertion_sort(A,bi_count))
 