import subprocess, ufw, logging

def firewall_ban(_con):
    try:
        subprocess.check_call(["ufw", "deny", "incoming", "from", str(_con)])
    except subprocess.CalledProcessError:
        logging.warning("Firewall role is not added!")
        exit(1)
    logging.warning("Firewall role succefully added: %s (incoming traffic has blocked)" % str(_con))
