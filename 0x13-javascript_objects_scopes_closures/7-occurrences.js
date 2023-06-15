#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nOccurences = 0;
  for (let i = 0; i < list.lenght; i++) {
    if (searchElement === list[i]) {
      nOccurences++;
    }
  }
  return nOccurences;
};
