import os

# Target paths for the configuration files
repo_root = r"C:\Users\losti\Documents\GitHub\Project_Pentalogy"
yaml_default = os.path.join(repo_root, "quartz.config.default.yaml")
yaml_alt = os.path.join(repo_root, "quartz.config.yaml")

print("Initiating full clean-slate configuration purge pass...")

# 1. Forcefully delete the legacy default YAML file if it exists
if os.path.exists(yaml_default):
    try:
        os.remove(yaml_default)
        print(" -> Successfully purged quartz.config.default.yaml from workspace.")
    except Exception as e:
        print(f" Error removing default YAML: {e}")
else:
    print(" -> quartz.config.default.yaml is already fully removed.")

# 2. Forcefully delete any secondary fallback YAML files
if os.path.exists(yaml_alt):
    try:
        os.remove(yaml_alt)
        print(" -> Successfully purged quartz.config.yaml from workspace.")
    except Exception as e:
        print(f" Error removing alt YAML: {e}")
else:
    print(" -> No alternative YAML configuration file present.")

print("\nCleanup sweep complete! Your repository is now pristine.")
