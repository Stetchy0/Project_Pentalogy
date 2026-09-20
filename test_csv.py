import os, csv
p = r"C:\Users\losti\Documents\GitHub\Project_Pentalogy\content\private\Character_Core_Data.csv"
print(f"File Exists: {os.path.exists(p)}")
if os.path.exists(p):
    with open(p, 'r', encoding='utf-8-sig', errors='ignore') as f:
        print(f"Total Character Length: {len(f.read())}")
        f.seek(0)
        for i in range(5):
            print(f"Line {i+1}: {repr(f.readline())}")
