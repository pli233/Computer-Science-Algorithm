
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
    
    """
    Input: This function will take an array of integers arr as input
    
    Output: It will return the maximum length of LIS 
    """
    
    #Initialization: 
    
    # add -infinite in input
    input = [float("-inf")]
    input.extend(arr)
    
    #extract the number of input  
    length = len(input)+1
    #print(length)

    #
    M= [ [0] * length  for i in range(length)]
    for j in range((length-1),1,-1):
        #j index is the true position of the element in input
        j_index = j-1
        j_element = input[j_index]
        #we going to compare all elements before jth element in input
        for i_index in range(j_index):
            #print(j_index,i_index)
            i_element = input[i_index]
            
            #case1: out of range
            if j_index > length:
                M[i_index][j_index] = 0
            #case2: j element does not > i element, it does not maintain an increasing order   
            elif j_element <= i_element:
                M[i_index][j_index] = M[i_index][j_index+1]
            #case3: j element > i element, it do maintain an increasing order, so it could be part of optimal solution
            else:
                #3.a: assume this element is not in the optimal solution, find the LIS 
                a = M[i_index][j_index+1]
                #3.b: assume this element is in the optimal soltion, find the LIS, here 
                b = M[j_index][j_index+1]+1
                M[i_index][j_index] = max(a,b)
    return M[0][1]





def main():
    test1 = [0,1,0,3,2,3]
    result = lis_recursive(-10000000,test1)
    print("test1:  "+str(result))
    
    result = lis_dp(test1)
    print("test2:  "+str(result))
    print()
    
    test2 = [10,1,2,5,3,7,101,18,2,20,100,30,10,91,-1,20,30,0,2,3,4,56,7,8,9,0,10,23,4501,200,1023,1023,21203,1,22330,112210,112301,2133,1232,123,55,43,10000000]
    result = lis_recursive(-10000000,test2)
    print("test1:  "+str(result))
    
    result = lis_dp(test2)
    print("test2:  "+str(result))
if __name__ == '__main__':
    main()