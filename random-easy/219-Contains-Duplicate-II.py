class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        _dict = dict()
        
        for index, value in enumerate(nums):
            if value in _dict:
                if index - _dict[value] <= k:
                    return True
            _dict[value] = index
        return False