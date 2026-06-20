import socket
import struct

def main():
    try:
        # Raw socket create
        sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)

        host = socket.gethostbyname(socket.gethostname())
        sniffer.bind((host, 0))

        sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

        print("Packet Sniffer Started...\n")

        while True:
            raw_data, addr = sniffer.recvfrom(65535)

            ip_header = raw_data[0:20]
            iph = struct.unpack('!BBHHHBBH4s4s', ip_header)

            version_ihl = iph[0]
            version = version_ihl >> 4
            ttl = iph[5]
            protocol = iph[6]
            src = socket.inet_ntoa(iph[8])
            target = socket.inet_ntoa(iph[9])

            print(f"Version: {version}")
            print(f"TTL: {ttl}")
            print(f"Protocol: {protocol}")
            print(f"Source IP: {src}")
            print(f"Destination IP: {target}")
            print("-" * 50)

    except PermissionError:
        print("Run as Administrator / Root.")
    except KeyboardInterrupt:
        print("\nStopped.")

if __name__ == "__main__":
    main()
