import csv
import os
from itertools import combinations

repo_root = r"C:\Users\losti\Documents\GitHub\Project_Pentalogy"
private_dir = os.path.join(repo_root, "private")

# Establish the strict path channels for both source and target files
primary_csv_path = os.path.join(private_dir, "Character_Core_Data.csv")
output_rel_path = os.path.join(private_dir, "Character_Relationships_Data.csv")

if not os.path.exists(primary_csv_path):
    print(f"Error: Primary data spreadsheet missing at target path:\n {primary_csv_path}")
    exit()

# 1. READ ACTIVE CHARACTER NAMES REGISTERED IN VAULT ENGINE
names = []
with open(primary_csv_path, mode='r', encoding='utf-8-sig', errors='ignore') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Standardize cell mapping to safely capture the name key regardless of header caps
        normalized_row = {k.lower().strip(): v.strip() for k, v in row.items() if k}
        name_val = normalized_row.get('character')
        if name_val and not any(x in name_val.lower() for x in ['character', '---', 'name']):
            names.append(name_val.strip())

# Clean and sort uniquely to prevent stray duplicate spillage
names = sorted(list(set(names)))
print(f"Loaded {len(names)} unique character name strings from your master spreadsheet.")

# 2. GENERATE ALL UNIQUE PAIRINGS COMBINATIONS
# combinations(names, 2) automatically builds unique sets without repeating entries (A-B and B-A)
all_pairs = list(combinations(names, 2))
print(f"Generated {len(all_pairs)} unique character-to-character pairing matrix nodes.")

# 3. CONSTRUCT RECURSIVE TWO-WAY RELATIONSHIP ROWS
# Because your structure requires explicitly defining how Character A views B, and B views A,
# we write out both directions for every mathematical pairing automatically!
two_way_rows = []
for char_a, char_b in all_pairs:
    two_way_rows.append([char_a, "Unlogged/Neutral", char_b])
    two_way_rows.append([char_b, "Unlogged/Neutral", char_a])

# 4. WRITE SYSTEM MAINBOARD TEMPLATE TO DISK
# Safety mechanism: Check if you've already started writing your real relationships data
if os.path.exists(output_rel_path):
    print(f"\n[!] ALERT: A relationships file already exists at target path:")
    print(f"    {output_rel_path}")
    ans = input("Do you want to OVERWRITE completely with fresh blank combo slots? (Y/N): ").lower().strip()
    if ans != 'y':
        print("[!] Execution safely aborted. Your existing relationships file was left untouched.")
        exit()

with open(output_rel_path, mode='w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    # Write your exact required 3-column layout header tags
    writer.writerow(['character_a', 'relation', 'character_b'])
    writer.writerows(two_way_rows)

print(f"\n[+] Success! Master Relational Ledger successfully generated and saved to path.")
print(f"    Injected exactly {len(two_way_rows)} automated interaction rows hands-free!")
