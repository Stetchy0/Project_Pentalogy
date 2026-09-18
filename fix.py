import os

# Define the absolute target directory paths on your hard drive
base_path = r"C:\Users\losti\Documents\GitHub\Project_Pentalogy"

lock_file = os.path.join(base_path, "package-lock.json")
nvmrc_file = os.path.join(base_path, ".nvmrc")

print("Initiating full clean-slate tracking cache override sweep...")

# 1. Forcefully unlink the desynchronized package-lock cache file
if os.path.exists(lock_file):
    try:
        os.remove(lock_file)
        print(" -> Successfully removed desynchronized package-lock.json cache.")
    except Exception as e:
        print(f" Could not clear lock file: {e}")
else:
    print(" -> package-lock.json already cleared from repository root.")

# 2. Extract any hidden Node Version Manager (.nvmrc) boundary limits
if os.path.exists(nvmrc_file):
    try:
        os.remove(nvmrc_file)
        print(" -> Successfully extracted legacy .nvmrc runtime overrides.")
    except Exception as e:
        print(f" Could not clear .nvmrc: {e}")
else:
    print(" -> No conflicting .nvmrc file present.")

print("\nSystem workspace metadata cleared! Ready for a pristine production push.")
