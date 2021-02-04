// Question: https://leetcode.com/problems/running-sum-of-1d-array/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function (nums) {
  const ans = [];
  ans.push(nums[0]);
  for (let i = 1; i < nums.length; i++) {
    ans.push(nums[i] + ans[i - 1]);
  }
  return ans;
};
