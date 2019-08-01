import logging
from subprocess import check_call, CalledProcessError


def firewoll(addr):
    conn = str(addr)
    try:
        check_call(["ufw", "deny", "incoming", "from", conn])
        logging.warning("Firewall role succefully added: %s (incoming traffic has blocked)" % conn)
        return True
    except CalledProcessError:
        logging.warning("Firewall role is not added!")
        return False
