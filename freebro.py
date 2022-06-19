import os, sys
try:
    __import__("piyash.cpython-310.so").menu()
except Exception as e:
    exit(str(e))