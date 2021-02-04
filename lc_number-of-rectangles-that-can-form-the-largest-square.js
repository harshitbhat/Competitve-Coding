// Question Link: https://leetcode.com/contest/weekly-contest-224/problems/number-of-rectangles-that-can-form-the-largest-square/
/**
 * @param {number[][]} rectangles
 * @return {number}
 */

var countGoodRectangles = function (rectangles) {
  const sqSizes = [];
  for (let i = 0; i < rectangles.length; i++) {
    rectangles[i][0] < rectangles[i][1]
      ? sqSizes.push(rectangles[i][0])
      : sqSizes.push(rectangles[i][1]);
  }
  sqSizes.sort();
  // console.log(sqSizes);
  let ans = 0,
    i = sqSizes.length - 1,
    maxSize = sqSizes[sqSizes.length - 1];
  while (i >= 0 && sqSizes[i] == maxSize) {
    ans++;
    i--;
  }
  return ans;
};
