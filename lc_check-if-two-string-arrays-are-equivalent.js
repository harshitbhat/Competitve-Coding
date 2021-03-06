/**
 * @param {string[]} word1
 * @param {string[]} word2
 * @return {boolean}
 */

// Using Reduce
var arrayStringsAreEqual = function (word1, word2) {
  return (
    word1.reduce((acc, cur) => acc + cur, '') ===
    word2.reduce((acc, cur) => acc + cur, '')
  );
};

// Using Join
var arrayStringsAreEqual2 = function (word1, word2) {
  return word1.join('') === word2.join('');
};
