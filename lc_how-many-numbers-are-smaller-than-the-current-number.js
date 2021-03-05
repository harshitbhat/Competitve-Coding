/**
 * @param {number[]} nums
 * @return {number[]}
 */
// O(n^2) solution
var smallerNumbersThanCurrent = function (nums) {
  const answer = new Array(nums.length).fill(0);
  for (let i = 0; i < nums.length; i++) {
    answer[i] = nums.filter((el, idx) => el < nums[i] && idx != i).length;
  }
  return answer;
};
// Better
var smallerNumbersThanCurrent2 = function (nums) {
  const arr = [...nums].sort((a, b) => a - b);
  return nums.map((el) => arr.indexOf(el));
};
