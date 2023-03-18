import sys
   
#1. read files and store them line by line in a list
file_content= sys.stdin.read().splitlines()
contents_by_line = []
for i in file_content:
    contents_by_line.append(i.rstrip())

#2. extract how many instances do we have, 
# transfer it to int and delete it from the content list
job_start = 0
instances_num = int(contents_by_line[0])
contents_by_line.pop(0)

for i in range(instances_num):
    #first line of an instances will indicate how many lines are included 
    #in the current instance
    num_of_jobs = int(contents_by_line[0])
    current_jobs = contents_by_line[1:num_of_jobs+1]
    #print("current_jobs:"+str(current_jobs))
    reformat_jobs = []
    #Todo: Manipulate each job and add them to list
    for job in current_jobs:
        formatted_job  = {}
        formatted_job["start"] = int(job.split()[0])
        formatted_job["finish"] = int(job.split()[1])    
        reformat_jobs.append(formatted_job)
        
    plausible_jobs = []
    #Todo: sort each elements in reformat jobs by finish time
    sorted_jobs = reformat_jobs
    while len(sorted_jobs)!=0:
        ##0sort job by finish first
        sorted_jobs = sorted(sorted_jobs, key=lambda x: x["finish"])
        #1. Choose jobs that has first finish time
        #print(sorted_jobs)
        #if there is tie, choose the first one in list
        job_finish = sorted_jobs[0]["finish"]
        #rint("this is the job i did"+str(sorted_jobs[0]))
        #2.Do jobs, and delete it.
        #do job
        plausible_jobs.append(sorted_jobs[0])
        #delete finished job
        sorted_jobs.pop(0)
        
        #3. Remove jobs that has start time smaller than job_finish
        for job in sorted_jobs:
            if(job["start"]<job_finish):
                #print("this is the job i remove"+str(job))
                sorted_jobs.remove(job)
    print(plausible_jobs)
    #update next job
    contents_by_line = contents_by_line[num_of_jobs+1:]
    