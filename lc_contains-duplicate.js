// QUestion: https://leetcode.com/problems/contains-duplicate/description/
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
  nums.sort();
  for (i = 0; i < nums.length - 1; i++) {
    if (nums[i] == nums[i + 1]) {
      return true;
    }
  }
  return false;
};
