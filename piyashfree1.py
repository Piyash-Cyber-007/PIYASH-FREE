import os, sys
try:
    __import__("piyash").menu()
except Exception as e:
    exit(str(e))