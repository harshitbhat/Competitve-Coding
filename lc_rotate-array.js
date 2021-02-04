// Question: https://leetcode.com/problems/rotate-array/description/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function (nums, k) {
  const n = nums.length;
  k = k % n;
  const ans = [];
  for (let i = n - k; i < n; i++) {
    ans.push(nums[i]);
  }
  for (i = 0; i < n - k; i++) {
    ans.push(nums[i]);
  }
  for (let i = 0; i < n; i++) {
    nums[i] = ans[i];
  }
};
