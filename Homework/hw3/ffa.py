import sys

nums_instance = int(sys.stdin.readline())

for i in range(nums_instance):
    nums_job = int(sys.stdin.readline())
    split_jobs = []
    for j in range(nums_job):
        job = sys.stdin.readline()
        job_split = job.split()
        int_jobs = []
        for i in job_split:
            int_jobs.append(int(i))
        split_jobs.append(int_jobs)
        
    sorted_jobs = sorted(split_jobs, key=lambda x: x[-1])
    #print(sorted_jobs)
    plausible_jobs = []
    plausible_jobs.append(sorted_jobs[0])
    last_finish = sorted_jobs[0][1]
    for job in sorted_jobs:
        #start time >=last finish time: do it 
        if job[0]>=last_finish:
            #do job
            plausible_jobs.append(job)
            #update last finish time
            last_finish = job[1]
    print(len(plausible_jobs))