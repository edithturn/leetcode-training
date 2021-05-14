public static List<String> findMissingRanges(int[] nums, int lower, int upper) {
	List<String> ans = new ArrayList<>();
	if (nums.length == 0) {
		ans = addRange(ans, lower, upper);
		return ans;
	}
	if (nums.length == 1) {
		ans = addRange(ans, lower, nums[0] - 1);
		ans = addRange(ans, nums[0] + 1, upper);
		return ans;
	}
	for (int i = 0; i < nums.length; i++) {
		int prev = lower - 1
		if (i + 1 != nums.length) {
			ans = addRange(ans, lower, nums[i] - 1);
			if (prev == nums[i] - 1)
				continue;
			else {
				ans = addRange(ans, nums[i] + 1, nums[i + 1] - 1);
			}
		} else {
			if (nums[i] != upper) {
				ans = addRange(ans, nums[i] + 1, upper);
			} else {
				if (nums[i - 1] != nums[i] - 1)
					ans = addRange(ans, lower, nums[i] - 1);
				ans = addRange(ans, nums[i] + 1, upper);
			}
		}
	}
	return ans;
}