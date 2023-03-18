unsorted_arr = [7,2,1,9,3,10,8]

def quick_select(arr,k):
    result_arr,L = partition(arr)
    #print(result_arr)
    #print(L)
    #     print("Looking for = "+str(k))
    rank = L+1
    print("reuslt:"+str(result_arr)+"  Position:"+str(L))
    if rank == k:
        return result_arr[L]
    #lower quartile
    elif rank > k: 
        quick_select(result_arr[0:L],k)
    #rank < k
    else:
        new_rank = k-rank
        quick_select(result_arr[rank:],new_rank)          

def partition(arr):
    L = 0
    R = len(arr)-1
    value = arr[0]
    result_arr= arr.copy()
    while L < R:
        if(len(arr)<=2):
            break
        current = result_arr[L]
        #next is value at the right of current
        next = result_arr[L+1]
        #current value is bigger than the number next to it:
        if(current>next):
            #swap current's position with next 
            result_arr[L+1] = current
            result_arr[L] = next
            L = L+1
        #current value is smaller than the number next to it:
        else:
            #print(unsort_arr[R])
            right = result_arr[R]
            result_arr[L+1] = right
            #print("R:"+str(R))
            result_arr[R] = next
            R = R-1
    print(value)
    return result_arr, result_arr.index(value)


ans = quick_select(unsorted_arr,5)
print(ans)
r = [9,9,10]
print(r.index(10))