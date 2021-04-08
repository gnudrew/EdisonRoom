# Test how class structure works for import from subfolders.
# Result -> We can treat folder hierarchies just like class object hierarchies.
# e.g. path ""./fox/fox1/", which contains the file, "foxy.py", which contains a function "fox()", is imported below.

from fox.fox1.foxy import fox

print("function pointer:", fox)
print("test output:",fox())