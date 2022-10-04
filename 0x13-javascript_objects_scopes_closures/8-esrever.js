#!/usr/bin/node

exports.esrever = function (list) {
  const listCopy = [];
  list.forEach(element => listCopy.unshift(element));
  return listCopy;
};
