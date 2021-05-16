/**
 * @param {character[][]} box
 * @return {character[][]}
 */
const moveToEnd = (arr) => {};
var rotateTheBox = function (box) {
  const m = box.length;
  const n = box[0].length;
  const ans = [];
  for (let arr of box) {
    let i = 0;
    let count = 0;
    while (i < arr.length && count < arr.length) {
      if (arr[i] === '.') {
        [arr[count], arr[i]] = [arr[i], arr[count]];
        count++;
      } else if (arr[i] === '*') {
        count = i + 1;
      }
      i++;
    }
    ans.push(arr);
  }

  const final = [];
  for (let j = 0; j < n; j++) {
    const orient = [];
    for (let i = 0; i < m; i++) {
      orient.push(ans[i][j]);
    }
    final.push(orient.reverse());
  }
  return final;
};
