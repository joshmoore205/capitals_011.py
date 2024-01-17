#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

for line in lines:
  line = line.strip()
  fc = line[0].capitalize()
  lc = line[-1].capitalize()
  chop = line[1:len(line) - 1]
  t = fc + chop + lc
  print(t)
