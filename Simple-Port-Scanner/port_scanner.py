import socket
from datetime import datetime

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    135: "MS RPC",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP"
}


def scan_port(host, port):
    """Check whether a TCP port is open."""

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.settimeout(0.5)

    result = sock.connect_ex((host, port))

    sock.close()

    return result == 0


def main():
    
    host = "127.0.0.1"

    print("=" * 55)
    print("             SIMPLE PORT SCANNER")
    print("=" * 55)

    print("Target:", host)
    print("Scan started:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    print("\nScanning common ports...\n")

    open_ports = []

    for port, service in COMMON_PORTS.items():

        if scan_port(host, port):

            print(f"[OPEN]   Port {port:<5} - {service}")
            open_ports.append((port, service))

        else:

            print(f"[CLOSED] Port {port:<5} - {service}")

    print("\n" + "=" * 55)
    print("                 SCAN REPORT")
    print("=" * 55)

    print("Target:", host)
    print("Open ports:", len(open_ports))

    if open_ports:

        print("\nOpen ports detected:")

        for port, service in open_ports:
            print(f"- Port {port}: {service}")

    else:

        print("\nNo common open ports were detected.")

    print("\nSecurity reminder:")
    print("Only expose services that are necessary.")
    print("Keep unnecessary services disabled and updated.")


if __name__ == "__main__":
    main()