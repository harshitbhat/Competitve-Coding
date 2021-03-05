/**
 * @param {string} s
 * @param {number[]} indices
 * @return {string}
 */
var restoreString = function (s, indices) {
  return s
    .split('')
    .map((_, ind) => s[indices.indexOf(ind)])
    .join('');
};
