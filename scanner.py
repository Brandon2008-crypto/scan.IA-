import socket

print("=== MINI CYBER SCANNER 🔐 ===")

target = input("Entrez une adresse IP ou un site : ")

# Résoudre le nom de domaine en IP
try:
    target_ip = socket.gethostbyname(target)
except:
    print("Erreur : impossible de trouver l'adresse")
    exit()

print(f"Scan de {target_ip} en cours...\n")

# Ports à scanner
ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 8080]

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target_ip, port))

    if result == 0:
        print(f"[OUVERT] Port {port}")
    else:
        print(f"[FERMÉ] Port {port}")

    sock.close()

print("\nScan terminé 🚀")
