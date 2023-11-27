#!/usr/bin/env python3
import os

print(f"Home: {os.environ.get('HOME', '')} ")
print("SHELL: " + os.environ.get("SHELL", ""))
print("FRUIT: " + os.environ.get("FRUIT", ""))
