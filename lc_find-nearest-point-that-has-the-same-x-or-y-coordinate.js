/**
 * @param {number} x
 * @param {number} y
 * @param {number[][]} points
 * @return {number}
 */
var nearestValidPoint = function (x, y, points) {
  const valid = points.filter((el) => el[0] == x || el[1] == y);
  if (valid.length == 0) {
    return -1;
  }
  let minDistance = 99999999;
  let ans = 0;
  for (let i = 0; i < points.length; i++) {
    point = points[i];
    if (point[0] === x || point[1] === y) {
      const dist = Math.abs(point[0] - x) + Math.abs(point[1] - y);
      if (dist < minDistance) {
        minDistance = dist;
        ans = i;
      }
    }
  }
  return ans;
};
