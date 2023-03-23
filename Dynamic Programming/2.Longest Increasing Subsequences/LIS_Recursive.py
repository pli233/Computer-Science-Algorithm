
def lis_recursive(k,arr):
    """
    Input: This function will take a integer k and array of 
    integers arr as input
    
    Output: It will return length of LIS where every value >k
    """
    
    #Base case: if the input do not contain elements anymore, we return 0    
    if len(arr) ==0:
        return 0
    
    #Case1:
    #in this case, the first element in input is <=k, so condition is not
    #matched we our expectation, we should return the remain array
    elif arr[0]<=k:
        return lis_recursive(k,arr[1:])
    
    #Case2:
    else:
        skip = lis_recursive(k,arr[1:])
        take = lis_recursive(arr[0],arr[1:])+1

        return max(skip,take)

def lis_dp(arr):
    input = [float("-inf")]
    input.extend(arr)
    length = len(input)
    DP_Matrix = [ [0] * length  for i in range(length)]
    return DP_Matrix

def _lis_dp(arr,DP_Matrix):
    """
    Input: This function will take a integer k and array of 
    integers arr as input
    
    Output: It will return length of LIS where every value >k
    """
    length = len(arr)
    #Base case: if the input do not contain elements anymore, we return 0    
    for j in range(length,0,-1):
        for i in range(j-1,0,-1):
            if j > length:
                DP_Matrix[i,j] = 0
            elif arr[]
    
    #Case1:
    #in this case, the first element in input is <=k, so condition is not
    #matched we our expectation, we should return the remain array
    
    #Case2:
    







def main():
    test1 = [0,1,0,3,2,3]
    #result = lis_recursive(1,test1)
    #print("test1:  "+str(result))
    #test2 = [10,9,2,5,3,7,101,18]
    #result = lis_recursive(0,test2)
    #print("test2:  "+str(result))
    lis_dp(test1)
    
if __name__ == '__main__':
    main()