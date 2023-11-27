#!/usr/bin/env python3
import sys
print(f"The program name used to launch me is {sys.argv[0]}.")
print("I was passed the following arguments:")
for arg in sys.argv[1:]:
    print(arg)
