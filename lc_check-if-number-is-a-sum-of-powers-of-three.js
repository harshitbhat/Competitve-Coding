/**
 * @param {number} n
 * @return {boolean}
 */

var isSubsetSum = function (set, n, sum) {
  if (sum === 0) {
    return true;
  }
  if (n === 0) {
    return false;
  }
  if (set[n - 1] > sum) {
    return isSubsetSum(set, n - 1, sum);
  }
  return (
    isSubsetSum(set, n - 1, sum) || isSubsetSum(set, n - 1, sum - set[n - 1])
  );
};

var checkPowersOfThree = function (sum) {
  const possible = [];
  for (let i = 0; i < 17; i++) {
    possible.push(3 ** i);
  }
  return isSubsetSum(possible, possible.length, sum);
};
