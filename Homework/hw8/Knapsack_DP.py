import sys

def Knapsack_max_value_DP(capacity,data_packages):
    """
    Input: This function will take three inputs:
    1. (int) capacity: the maximum capacity that we could have
    2. (list) data_packages: the weight and value of each packages we are about to schedule 
    
    Output: It will return length of LIS where every value >k
    """

    #1. Initialize a N x W 2D dimentional array, default value is None
        # N is the number of packages we are able to schedule, 
        # W is the maximum capacity of the theive
    num_packages = len(data_packages)
    N = num_packages+1
    W =  capacity+1
    # Inner loops create space for each Weight
    # Outer loops create space for each package
    M = [[None for i in range(W)] for j in range(N)]
    
    #Initialize M [0, W]= 0 for each w = 0,1,...,W
    for i in range(W):
        M[0][i] = 0
    
    #2. Use the created matrix to store value
    # M[i,j] represents the maximum value the theive can get for package for Ni, and total weight < Wj

    #loop through each package
    for i in range(1,N,1):
        #retrieve the weight and value for the ith package
        wi = data_packages[i-1][0]
        vi = data_packages[i-1][1]
        #loop through each weight
        for j in range(W):

            #1. current weight < wi
            if wi>j:
                #therefore, we cannot add the current package's value to our package, 
                # track the preivous bag's maximum value with same weight
                M[i][j] = M[i-1][j]
                
            #2: current weight >= wi
            else:
                #two possibility: 
                # a.the preivous bag's maximum value with same weight is optimal
                # track the preivous bag's maximum value with same weight
                
                # b.add the current packages' value to our set is optimal
                # we have to track the previous package's maximum with the weight of j-ith package's weight
                #choose the maximum of the above two value 
                a = M[i-1][j]
                b = vi+M[i-1][j-wi]
                M[i][j] = max(a,b)
    return M[-1][-1]

#main function to call 
def main():
    #read num of instance
    nums_instance = int(sys.stdin.readline())

    #read file by instances
    for i in range(nums_instance):
        
        #read num of jobs
        info_instance = sys.stdin.readline().split()
        num_packages = int(info_instance[0])
        capacity = int(info_instance[1])
        #print("nums_job: "+str(nums_job)+" capacity: "+str(capacity))
        
        #split packages contains every package we can carry, and it is listed as [ [weight1,value1],[weight2,value2]  ]
        split_packages = []
        
        #read info of packages by line
        for j in range(num_packages):
            package = sys.stdin.readline().split()
            int_packages = []
            for i in package:
                int_packages.append(int(i))
            split_packages.append(int_packages)
            
        #Use DP to solve the maximum value
        max_steal_value = Knapsack_max_value_DP(capacity,split_packages)
        print(max_steal_value)
        
        

if __name__ == '__main__':
    main()
    