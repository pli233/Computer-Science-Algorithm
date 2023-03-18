import sys
import math

def merge_sort(arr,size):
    #TODO: return a sorted arr and num of inversions
    
    #Base case: if there is only one element in the array, return it self,
    # and the number of inversions here is 0
    if size==1:
        return arr, 0

    #seperate the list by index
    mid_point = math.ceil(size/2)
    left = arr[0:mid_point]
    right = arr[mid_point:]
    
    #recursive left half:
    left_sort_arr,left_inver_count = merge_sort(left,len(left))
    #recursive right half
    right_sort_arr,right_inver_count = merge_sort(right,len(right))
    
    #merge two sorted array
    sort_arr, merge_inver_count = merge(left_sort_arr,right_sort_arr)
    
    #calculate total inversions
    total_inver = left_inver_count+right_inver_count+merge_inver_count
    
    return sort_arr, total_inver
  
def merge(left,right):
    #TODO: merge two sorted array, it can be zero
    sorted_arr = []
    inver_count = 0
    
    while (len(left)!=0) or (len(right)!=0):

        #if left is empty, pop right
        if(len(left)==0):
            sorted_arr.append(right.pop(0))
        #if right is empty, pop left
        elif(len(right)==0):
            sorted_arr.append(left.pop(0))
        #both not empty, compare first element
        else:
            #inversion occurs
            if(right[0]<left[0]):
                sorted_arr.append(right.pop(0))
                inver_count += len(left)
            else:
                sorted_arr.append(left.pop(0))
    return sorted_arr, inver_count


        

#number of instances we have
nums_instance = int(sys.stdin.readline())

for i in range(nums_instance):
    
    ##PartA: Initialization
    
    #number of elements we have in this instance
    size_elements = int(sys.stdin.readline())
    
    if size_elements ==0:
        print(str(0))
        continue
    list_y1 = []
    list_y0 = []
    list_result= []
    
    #read these elements and store them in an array, as unsort
    for elements in range(size_elements):
        num_y1 = int(sys.stdin.readline())
        list_y1.append(num_y1)
        
    for elements in range(size_elements):
        num_y0 = int(sys.stdin.readline())
        list_y0.append(num_y0)
    
    #map each point to a dictionary x0:x1
    for index in range(size_elements):
        list_result.append({list_y0[index]:list_y1[index]})
        
    #sort points by x0
    sorted_arr = sorted(list_result, key=lambda x: list(x.keys())[0])
    
    #extract x1 from sorted points
    values = []
    for d in sorted_arr:
        values.extend(list(d.values()))
        
    sort_arr,inversion_count =merge_sort(values, size_elements)
    
    print(inversion_count)
    
    #print("y1:",str(list_y1))
    #print("y0:",str(list_y0))
    #print("result",str(values))
    
   
