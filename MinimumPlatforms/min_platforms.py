# You are given the arrival times arr[] and departure times dep[] of all trains that arrive at a railway station on the same day. 
# Your task is to determine the minimum number of platforms required at the station to ensure that no train is kept waiting.

# At any given time, the same platform cannot be used for both the arrival of one train and the departure of another. 
# Therefore, when two trains arrive at the same time, or when one arrives before another departs, additional platforms are required to accommodate both trains.


def min_platforms(arr, dep):
    # Sort the arrival and departure times
    arr.sort()
    dep.sort()

    # Initialize variables
    n = len(arr)
    platforms_needed = 1
    max_platforms = 1

    # Initialize pointers for arrival and departure times
    i = 1
    j = 0

    # Iterate through all trains
    while i < n and j < n:
        # If the next train arrives before the previous one departs, we need a new platform
        if arr[i] <= dep[j]:
            platforms_needed += 1
            i += 1
        # If the next train departs before the previous one arrives, we can free up a platform
        else:
            platforms_needed -= 1
            j += 1

        # Update the maximum number of platforms needed at any time
        max_platforms = max(max_platforms, platforms_needed)

    return max_platforms


print(min_platforms([900, 940, 950, 1100, 1500, 1800], [910, 1200, 1120, 1130, 1900, 2000])) # Output: 3
print(min_platforms([900, 1235, 1100], [1000, 1240, 1200])) # Output: 1
print(min_platforms([1000, 935, 1100], [1200, 1240, 1130])) # Output: 3


# Examples:

# Input: arr[] = [900, 940, 950, 1100, 1500, 1800], dep[] = [910, 1200, 1120, 1130, 1900, 2000]
# Output: 3
# Explanation: There are three trains during the time 9:40 to 12:00. So we need a minimum of 3 platforms.
# Input: arr[] = [900, 1235, 1100], dep[] = [1000, 1240, 1200]
# Output: 1
# Explanation: All train times are mutually exclusive. So we need only one platform
# Input: arr[] = [1000, 935, 1100], dep[] = [1200, 1240, 1130]
# Output: 3
# Explanation: All 3 trains have to be there from 11:00 to 11:30
# Constraints:
# 1≤ number of trains ≤ 50000
# 0000 ≤ arr[i] ≤ dep[i] ≤ 2359
# Note: Time intervals are in the 24-hour format(HHMM) , where the first two characters represent hour (between 00 to 23 ) and the last two characters represent minutes (this will be <= 59 and >= 0).