// Question: https://leetcode.com/problems/maximum-subarray/

var maxSubArray = function (nums) {
  const sumArray = [];
  sumArray.push(nums[0]);
  for (let i = 1; i < nums.length; i++) {
    sumArray.push(
      sumArray[i - 1] + nums[i] > nums[i] ? sumArray[i - 1] + nums[i] : nums[i]
    );
  }
  let ans = sumArray[0];
  for (let i = 1; i < nums.length; i++) {
    if (sumArray[i] > ans) {
      ans = sumArray[i];
    }
  }
  return ans;
};
