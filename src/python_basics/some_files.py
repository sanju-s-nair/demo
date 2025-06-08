try:
    #file = open('testfile', 'r') # does not work because its read only
    file = open('testfilecode.py', 'w')
    file.write('#test file this')

except:
    print("Could not read the file data")

else:
    print("successfully opened the file data")