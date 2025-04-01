# You are given a set of activities, each with a start time and a finish time, represented by the arrays start[] and finish[], respectively. 
# A single person can perform only one activity at a time, meaning no two activities can overlap. 
# Your task is to determine the maximum number of activities that a person can complete in a day.


def activity_selection(start, finish):
    # Sort activities based on their finish times
    activities = sorted(zip(start, finish), key=lambda x: x[1])
    
    # Initialize count of activities and the end time of the last selected activity
    count = 0
    last_finish_time = -1
    
    for s, f in activities:
        # If the start time of the current activity is greater than or equal to the finish time of the last selected activity
        if s > last_finish_time:
            count += 1  # Select this activity
            last_finish_time = f  # Update the finish time of the last selected activity
    
    return count


print(activity_selection([1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9]))  # Output: 4
print(activity_selection([10, 12, 20], [20, 25, 30]))  # Output: 1
print(activity_selection([1, 3, 2, 5], [2, 4, 3, 6]))  # Output: 3


# Examples:

# Input: start[] = [1, 3, 0, 5, 8, 5], finish[] = [2, 4, 6, 7, 9, 9]
# Output: 4
# Explanation: A person can perform at most four activities. The maximum set of activities that can be executed is {0, 1, 3, 4}
# Input: start[] = [10, 12, 20], finish[] = [20, 25, 30]
# Output: 1
# Explanation: A person can perform at most one activity.
# Input: start[] = [1, 3, 2, 5], finish[] = [2, 4, 3, 6]
# Output: 3
# Explanation: A person can perform activities 0, 1 and 3.
# Constraints:
# 1 ≤ start.size() = finish.size() ≤ 2*105
# 1 ≤ start[i] ≤ finish[i] ≤ 109