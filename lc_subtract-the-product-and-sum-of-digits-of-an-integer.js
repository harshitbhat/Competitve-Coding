/**
 * @param {number} n
 * @return {number}
 */
var subtractProductAndSum = function (n) {
  return (
    ('' + n).split('').reduce((prod, cur) => prod * +cur, 1) -
    ('' + n).split('').reduce((sum, cur) => sum + +cur, 0)
  );
};
