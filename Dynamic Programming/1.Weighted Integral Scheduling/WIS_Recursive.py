import sys

class interval:
    def __init__(self,start,finish,value):
        self.start = start
        self.finish= finish
        self.value = value
    def __repr__(self):
        #repr = "<"+"name:"+str(self.name)+" start:"+str(self.start)+" finish:"+str(self.finish)+" value:"+str(self.value)+">"
        repr = "<"+str(self.start)+" "+str(self.finish)+" "+str(self.value)+">"
        return repr


def WIS(arr):
    #1. Sort the array by finish time, increasingly 
    j = len(arr)-1
    sorted_arr= sorted(arr, key=lambda x: x.finish)
    #print(sorted_arr)
    
    #2.Since we need n first element, so we actually have it in j-1 index in arr
    #print("j-1:"+str(j-1))
    
    #3. The empty dp, is an array where its index is correspond to the value of OPT(j)
    max_value = OPT(j,sorted_arr)
    return DP_Matrix[j]

def OPT(j,input):
    #print(str(input[j])+": "+str(DP_Matrix))
    j_element = input[j]
    if(DP_Matrix[j]!=None):
        #print("Trigger!")
        return DP_Matrix[j]
    if(j==0):
        #add to DP_Matrix
        DP_Matrix[j] = j_element.value
        return j_element.value
    
    #5. Find i, where i is the lastest non overlapping schedule
    i_element = None
    
    #get the elements before j
    #reverse the sorted arr
    reversed_arr = list(reversed(input[0:j]))

    for interval in reversed_arr:
        #non overlap condition
        if interval.finish <= j_element.start:
            #we only need the first element, so we break
            i_element = interval
            break
   
    #6. Calculate max possible value 
    #if there is no element i, we compare j_element's value and OPT(j-1)
    if i_element == None:
        #print("i_elements")
        
        #v1: exclude this value
        v1 = OPT(j-1,input)
        #v2: value of this interval
        v2 = j_element.value
        result = max(v1,v2)
        
    #if there is such an element i, we compare j_element's value+OPT(i) and OPT(j-1)    
    else:
        i_index = input.index(i_element)
        #print(i_element)
        
        #v1: exclude this value
        v2 = OPT(i_index,input)+j_element.value
        v1 = OPT(j-1,input)
        result = max(v1,v2)
        
    #add result to DP_Matrix
    DP_Matrix[j] = result
    #print(result)
    return result

def main():
    #read num of instance
    nums_instance = int(sys.stdin.readline())

    #read by instances
    for i in range(nums_instance):
        #read num of jobs
        nums_job = int(sys.stdin.readline())
        split_jobs = []
        #read jobs by line
        for j in range(nums_job):
            job = sys.stdin.readline()
            job_split = job.split()
            int_jobs = []
            for i in job_split:
                int_jobs.append(int(i))
            new_interval = interval(int_jobs[0],int_jobs[1],int_jobs[2])
            split_jobs.append(new_interval)
        #print()
        global DP_Matrix
        DP_Matrix= [None for i in range(len(split_jobs))] 
        max_value= WIS(split_jobs)
        #print(DP_Matrix)
        print(max_value)

if __name__ == '__main__':
    main()
    