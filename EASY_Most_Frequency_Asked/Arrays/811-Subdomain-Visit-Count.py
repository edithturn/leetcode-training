
# A website domain like "discuss.leetcode.com" consists of various subdomains. At the top level, we have "com", at the next level, we have "leetcode.com", and at the lowest level, "discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com", we will also visit the parent domains "leetcode.com" and "com" implicitly.
# Now, call a "count-paired domain" to be a count (representing the number of visits this domain received), followed by a space, followed by the address. An example of a count-paired domain might be "9001 discuss.leetcode.com".
# We are given a list cpdomains of count-paired domains. We would like a list of count-paired domains, (in the same format as the input, and in any order), that explicitly counts the number of visits to each subdomain.

# Example 1:
# Input: 
# ["9001 discuss.leetcode.com"]
# Output: 
# ["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
# Explanation: 
# We only have one website domain: "discuss.leetcode.com". As discussed above, the subdomain "leetcode.com" and "com" will also be visited. So they will all be visited 9001 times.
# Example 2:
# Input: 
# ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
# Output: 
# ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
# Explanation: 
# We will visit "google.mail.com" 900 times, "yahoo.com" 50 times, "intel.mail.com" once and "wiki.org" 5 times. For the subdomains, we will visit "mail.com" 900 + 1 = 901 times, "com" 900 + 50 + 1 = 951 times, and "org" 5 times.


from collections import defaultdict


def subdomainVisits(cpdomains): 
    """
     First Approach: Hash Map
    ||======= Big O ======= || 
    - Time complexity : O(N) where N is the length of cpdomains.
    - Space complexity: O(N) the space used in our count
    """   
    # A defaultdict can be created by giving its declaration an argument that can have three values; list, set or int.
    map_domain = defaultdict(int)

    for cpdomain in cpdomains:
        count, domains = cpdomain.split(' ')
        count = int(count)
        domain = domains.split('.')
        for i in range(len(domain)):
            map_domain['.'.join(domain[i:])] += count
    return ('{} {}'.format(x, y) for y, x in map_domain.items())


# Test case
s1 = ["9001 discuss.leetcode.com"]
s2 = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]

print(list(subdomainVisits(s1)))
print(list(subdomainVisits(s2)))