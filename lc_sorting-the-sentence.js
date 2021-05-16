/**
 * @param {string} s
 * @return {string}
 */
var sortSentence = function (s) {
  const sentence = new Array(10).fill(null);
  s = s.split(' ');
  for (const word of s) {
    const idx = parseInt(word[word.length - 1]);
    sentence[idx] = word
      .split('')
      .splice(0, word.length - 1)
      .join('');
  }
  let ans = '';
  for (let word of sentence) {
    if (word != null) {
      ans += word + ' ';
    }
  }
  return ans.trim();
};
