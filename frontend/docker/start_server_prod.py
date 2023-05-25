import subprocess
import os

def cleanup() -> None:
    file_to_remove = "/tmp/nitro/worker-*.sock"
    result = subprocess.call(f"rm -f {file_to_remove}", shell=True)
    print("Done") if result == 0 else print("Failed to remove file .sock")

# Cleanup
cleanup()

PS_YARN_INSTALL = "yarn install"
PS_YARN_RUN_BUILD = "yarn build"
PS_LAUNCH_NODE = "node .output/server/index.mjs"

os.chdir("frontend/")

subprocess.call(PS_YARN_INSTALL, shell=True)
subprocess.call(PS_YARN_RUN_BUILD, shell=True)
subprocess.call(PS_LAUNCH_NODE, shell=True)
