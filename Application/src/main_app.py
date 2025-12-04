import os
import sys
import platform
import subprocess
from pathlib import Path
import permission_handler as perms

def admin():
    system = platform.system()
    if not(perms.is_admin(system)):
        perms.request_admin_privileges(system)
        if not(perms.is_admin(system)):
            return False
    return True

def save_user(email):
    system = platform.system

    match system:
        case "Windows":
            subprocess.run(['powershell', '-Command', f'setx CYBERCLINIC_USER {email}'])
        case "Linux":
            shell = os.environ.get("SHELL", "")
            if 'zsh' in shell:
                with open(Path.home() / ".zshrc", 'a') as f:
                    print(f"Save {email} to ~/.zshrc")
                    f.write(f'export CYBERCLINIC_USER={email}')
                    f.close()
            elif 'bash' in shell:
                with open(Path.home() / ".bashrc", 'a') as f:
                    print(f"Save {email} to ~/.bashrc")
                    f.write(f'export CYBERCLINIC_USER={email}')
                    f.close()
        case "Darwin":
            with open("/etc/launchd.conf") as f:
                print(f"Save {email} to /etc/launchd.conf")
                f.write(f'setenv CYBERCLINIC_USER={email}')
                f.close()
        case _:
            sys.exit("Invalid OS!")