import os

def remove_known_hosts():
    known_hosts_path = os.path.expanduser("~/.ssh/known_hosts")
    try:
        os.remove(known_hosts_path)
        print("Fingerprints de known_hosts eliminados exitosamente.")
    except FileNotFoundError:
        print("El archivo known_hosts no existe. No se eliminaron fingerprints.")

if __name__ == "__main__":
    remove_known_hosts()
