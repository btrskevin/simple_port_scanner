import socket

def scan_single_port(target, port):
    
    try:
        print(f"\nScanning {target} on port {port}")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port}: OPEN")
        else:
            print(f"Port {port}: CLOSED")
        sock.close()
    except Exception:
        print(f"Error scanning port {port}")

def scan_selective_ports(target, ports):
    
    try:
        print(f"\nScanning {target} on ports {ports}")
        for port in ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex((target, port))
                if result == 0:
                    print(f"Port {port}: OPEN")
                sock.close()
            except Exception:
                print(f"Error scanning port {port}")
    except Exception:
        print(f"Error scanning ports {ports}")

def scan_port_range(target, start_port, end_port):
    
    try:
        print(f"\nScanning {target} from port {start_port} to {end_port}")
        for port in range(start_port, end_port + 1):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex((target, port))
                if result == 0:
                    print(f"Port {port}: OPEN")
                sock.close()
            except Exception:
                print(f"Error scanning port {port}")
    except Exception:
        print(f"Error scanning port range {start_port}-{end_port}")

if __name__ == "__main__":
    try:
        target = input("\nEnter the target IP address (or domain): ")
        
        print(f"Port Scanner Menu for {target}:")
        print("1. Scan a single port")
        print("2. Scan selective ports")
        print("3. Scan a range of ports")
        
        choice = input("Select an option > ")
        
        if choice == "1":
            try:
                port = int(input("Enter the port to scan: "))
                scan_single_port(target, port)
            except ValueError:
                print("Invalid port number. Please enter an integer.")
        
        elif choice == "2":
            try:
                ports = input("Enter the ports to scan (comma-separated, e.g., 22,80,443): ")
                ports = [int(p.strip()) for p in ports.split(",")]
                scan_selective_ports(target, ports)
            except ValueError:
                print("Invalid ports. Please enter integers separated by commas.")
        
        elif choice == "3":
            try:
                start_port = int(input("Enter the starting port: "))
                end_port = int(input("Enter the ending port: "))
                if start_port > end_port:
                    print("Invalid range. Starting port must be less than or equal to ending port.")
                else:
                    scan_port_range(target, start_port, end_port)
            except ValueError:
                print("Invalid input. Please enter integers for the port range.")
        
        else:
            print("Invalid choice. Please run the program again.")
    except KeyboardInterrupt:
        print("\n\nExiting..")
    except Exception:
        print("An unexpected error occurred.")
