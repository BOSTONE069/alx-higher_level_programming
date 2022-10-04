#!/usr/bin/node

exports.converter = function (base) {
  return function (val) { return val.toString(base); };
};
