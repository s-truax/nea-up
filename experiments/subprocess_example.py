import subprocess

files = subprocess.run("ls")

print(files.stdout)
