/**
 * @param {number} num
 * @return {number}
 */
var numberOfSteps = function (num) {
  ans = 0;
  while (num) {
    if (num % 2 == 0) {
      num /= 2;
    } else {
      num -= 1;
    }
    ans++;
  }
  return ans;
};

// Recursive solution

var numberOfSteps2 = function (num, ans = 0) {
  if (num === 0) {
    return ans;
  }
  return num % 2 === 0
    ? numberOfSteps(num / 2, ++ans)
    : numberOfSteps(num - 1, ++ans);
};
