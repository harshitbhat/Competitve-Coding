/**
 * @param {number[]} nums
 * @return {number}
 */
const generateSubsets = (arr) => {
  const n = arr.length;
  const size = 2 ** n;
  const subsets = [];
  for (let i = 0; i < size; i++) {
    const set = [];
    for (let j = 0; j < n; j++) {
      if ((i & (1 << j)) !== 0) {
        set.push(arr[j]);
      }
    }
    subsets.push(set);
  }
  return subsets;
};

const xorOfArr = (arr) => {
  let xor = 0;
  for (const el of arr) {
    xor = xor ^ el;
  }
  return xor;
};
var subsetXORSum = function (nums) {
  const arr = generateSubsets(nums);
  let ans = 0;
  for (const ar of arr) {
    ans += xorOfArr(ar);
  }
  return ans;
};
