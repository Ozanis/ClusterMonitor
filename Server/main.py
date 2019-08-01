import ServiceServer, Firewoll, logging, autocleaner
from os import getcwd, chdir

if __name__ == "__main__":
    logging.basicConfig(filename=getcwd() + "logs.log")
    print("START")
    try:
        DFservice = ServiceServer.ServerSsl()
        work_direct = getcwd() + "/Clients/"
        chdir(work_direct)
        autocleaner.Cleaner(work_direct)
        DFservice.con(work_direct)
    except KeyboardInterrupt:
        logging.info("Stopping server")
        print("Keyboard interrupt")
    finally:
        exit(0)
