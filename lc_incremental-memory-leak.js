/**
 * @param {number} memory1
 * @param {number} memory2
 * @return {number[]}
 */
var memLeak = function (memory1, memory2) {
  let time = 1;
  for (let i = 1; ; i++) {
    if (memory1 === memory2 || memory1 > memory2) {
      if (i > memory1) {
        break;
      } else {
        memory1 -= i;
        time++;
      }
    } else if (memory2 > memory1) {
      if (i > memory2) {
        break;
      } else {
        memory2 -= i;
        time++;
      }
    }
  }
  return [time, memory1, memory2];
};
