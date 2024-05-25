import psutil

def list_open_ports():
    # Get all active network connections
    connections = psutil.net_connections(kind='inet')
    
    # Iterate through connections and print the open ports
    for conn in connections:
        laddr = conn.laddr  # local address
        raddr = conn.raddr  # remote address
        
        if laddr and laddr.port:
            print(f"Local Address: {laddr.ip}:{laddr.port}")
            if raddr:
                print(f"Remote Address: {raddr.ip}:{raddr.port}")
            print(f"Status: {conn.status}")
            print(f"PID: {conn.pid}")
            print('-' * 40)

if __name__ == "__main__":
    list_open_ports()
