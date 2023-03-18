import sys

nums_instance = int(sys.stdin.readline())

for i in range(nums_instance):
    
    ##PartA: Initialization
    
    
    #number of cache size
    cache_size = int(sys.stdin.readline())
    cache = []
    int_coordinates = {}
    #number of pages we have from input 
    num_pages = int(sys.stdin.readline())
    str_pages = sys.stdin.readline().split()
    int_pages = [int(s) for s in str_pages]
    page_fault = 0
    
    #Store every different value into a dictionary, 
    #it can be access through key with num
    for i in range(len(int_pages)):
        num = int_pages[i]
        if num not in int_coordinates.keys():
            int_coordinates[num] = [i]
        else:
            int_coordinates[num].append(i)
    #print(int_coordinates)
    
    

    for page_index in range(num_pages):
        page = int_pages[page_index]
        #uncomment below for test
        #print("page = "+str(page),end = "")
        
        
        
        #Case 1, Hit: current input is in cahce, do nothing
        if page in cache:
            #uncomment below for test
            #print("  cache = "+str(cache))
            continue
    
        #Case 2: if cache is not full, and element is not find in
        #current cache, add element to cache 
        elif len(cache)<cache_size:
            #1) add this page to cache
            cache.append(page)
            #2) update page_fault
            page_fault +=1
            continue
            
        #Case 3, Miss: if current input is not in cache and 
        # cache is full, solve it
        else:
            page_fault +=1
            #These are the remain elements 
            max_pos = 0
            to_remove = None
            
            for cache_element in cache:
                positions = int_coordinates[cache_element]
                valid_positions= [num for num in positions if num > page_index]
                if len(valid_positions) ==0:
                    to_remove = cache_element
                    break
                first_position = valid_positions[0]
                if first_position>max_pos:
                    max_pos = first_position
                    to_remove = cache_element
            #if there is at least one cache element found in remain list, delete furthest one
            if(to_remove != None):
                cache.remove(to_remove)
                cache.append(page)
            #cache are all not usefull, randomly pop 1
            else:
                cache.pop()
                cache.append(page)
        # uncomment below to test
        #print("  cache = "+str(cache))
    print(page_fault)