import os
import subprocess

print(subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"], encoding="UTF-8").strip())
#print(os.getenv("GIT_BRANCH"))
