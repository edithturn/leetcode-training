
# You are given a 2D integer array logs where each logs[i] = [birthi, deathi] indicates the birth and death years of the ith person.
# The population of some year x is the number of people alive during that year. The ith person is counted in year x's population if x is in the inclusive range [birthi, deathi - 1]. Note that the person is not counted in the year that they die.
# Return the earliest year with the maximum population.

# Example 1:
# Input: logs = [[1993,1999],[2000,2010]]
# Output: 1993
# Explanation: The maximum population is 1, and 1993 is the earliest year with this population.

# Example 2:
# Input: logs = [[1950,1961],[1960,1971],[1970,1981]]
# Output: 1960
# Explanation: 
# The maximum population is 2, and it had happened in years 1960 and 1970.
# The earlier year between them is 1960.


def maximumPopulation(logs):
    """
    First Approach Brute Force: First loop to calculate the amoung of population per year, 
    not including the death year. Saving it in a dictionaty.
    The second loop will compare the amoung of population per year and it will take the one with
    the earliest year.

    ||======= Big O ======= ||
    * Time complexity : O(nk) 
    * Space complexity: O(n)
    where "n" is the number of years.
    """
    population_year={}
    for i in range(len(logs)):
        for j in range(logs[i][0], logs[i][1]):
            if j not in population_year:
                population_year[j] = 1
            else:
                population_year[j] += 1
    
    max_year = 0
    max_population = 0
                    
    for i in population_year:
        if population_year[i] > max_population:
            max_population = population_year[i]
            max_year = i
        elif population_year[i] == max_population:
            if i < max_year:
                max_year = i
    return max_year


#TODO Sweep Line

# 2005
l1 = [[2033,2034],[2039,2047],[1998,2042],[2047,2048],[2025,2029],[2005,2044],[1990,1992],[1952,1956],[1984,2014]]
# 1993
l2 = [[1993,1999],[2000,2010]]
# 1960
l3 = [[1950,1961],[1960,1971],[1970,1981]]

print(maximumPopulation(l1))
print(maximumPopulation(l2))
print(maximumPopulation(l3))