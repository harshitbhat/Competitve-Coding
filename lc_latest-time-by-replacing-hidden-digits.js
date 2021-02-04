// https://leetcode.com/contest/weekly-contest-225/problems/latest-time-by-replacing-hidden-digits/

/**
 * @param {string} time
 * @return {string}
 */
var maximumTime = function (time) {
  let hh = "";
  let mm = "";
  if (time[0] === "?") {
    if (
      time[1] === "?" ||
      time[1] == "0" ||
      time[1] == "1" ||
      time[1] == "2" ||
      time[1] == "3"
    ) {
      hh += "2";
    } else {
      hh += "1";
    }
  } else {
    hh += time[0];
  }
  if (time[1] === "?") {
    if (time[0] === "0" || time[0] === "1") {
      hh += "9";
    } else {
      hh += "3";
    }
  } else {
    hh += time[1];
  }
  if (time[3] === "?") {
    mm += "5";
  } else {
    mm += time[3];
  }
  if (time[4] === "?") {
    mm += "9";
  } else {
    mm += time[4];
  }

  return hh + ":" + mm;
};
