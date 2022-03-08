import nmap


class netmapper:
    """
    netmapper parent class
    """
    def __init__(self) -> None:
        self.scanner = nmap.PortScanner()
        self.ip_addr = None
        self.resp = None


def display():
    return "netmapper monitor"


def getInput(self):
    ip_addr = input("Please Enter the IP address you want to Scan: ")
    print("The IP you entered is: ", ip_addr)
    type(ip_addr)

    resp = input("""\nPlease Enter the type of Scan you want to run
                1)SYN ACK Scan
                2)UDP Scan
                3)Comprehensive Scan\n""")
    print("You have selected option: ", resp)
