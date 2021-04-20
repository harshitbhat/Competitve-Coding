/**
 * @param {number[][]} image
 * @return {number[][]}
 */

var flipAndInvertImage = function (image) {
  for (const arr of image) {
    let i = 0;
    let j = arr.length - 1;
    while (i < j) {
      let temp = arr[i];
      arr[i] = arr[j];
      arr[j] = temp;
      i++;
      j--;
    }
  }
  for (let i = 0; i < image.length; i++) {
    for (let j = 0; j < image[i].length; j++) {
      image[i][j] = !image[i][j];
    }
  }
  return image;
};
