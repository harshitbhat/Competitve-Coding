// Question: https://leetcode.com/problems/two-sum/description/

var twoSum = function (nums, target) {
  const ans = [];
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] === target) {
        ans.push(i);
        ans.push(j);
        break;
      }
    }
  }
  return ans;
};
