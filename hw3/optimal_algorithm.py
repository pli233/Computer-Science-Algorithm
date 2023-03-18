import sys
import heapq

def optimal_algorithm(jobs):
    # sort the jobs by the end time in ascending order
    jobs.sort(key=lambda x: x[1])
    # the first job always scheduled
    scheduled = [jobs[0]]
    for i in range(1, len(jobs)):
        # if the current job's start time is greater than the end time of the last scheduled job
        if jobs[i][0] >= scheduled[-1][1]:
            # schedule the current job
            scheduled.append(jobs[i])
    return len(scheduled)

def main():
    # read the input
    t = int(sys.stdin.readline())
    for i in range(t):
        n = int(sys.stdin.readline())
        input = []
        for j in range(n):
            input.append([int(x) for x in sys.stdin.readline().split()])
        # print the output
        print(optimal_algorithm(input)) 


if __name__ == "__main__":
    main()