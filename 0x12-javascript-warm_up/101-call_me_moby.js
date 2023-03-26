#!/usr/bin/node

const callMeMoby = function (x, theFunction) {
  for (i = 0; i < x; i++) { theFunction(); }
};

module.exports = { callMeMoby };
