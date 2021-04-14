/**
 * @param {number[]} arr
 * @param {number} a
 * @param {number} b
 * @param {number} c
 * @return {number}
 */

const abs = (a, b) => Math.abs(a - b);

var countGoodTriplets = function (arr, a, b, c) {
  let ans = 0;
  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      for (let k = j + 1; k < arr.length; k++) {
        if (
          abs(arr[i], arr[j]) <= a &&
          abs(arr[j], arr[k]) <= b &&
          abs(arr[i], arr[k]) <= c
        ) {
          ans++;
        }
      }
    }
  }
  return ans;
};
