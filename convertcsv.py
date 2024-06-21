import re
import csv

# Ruta del archivo INI
ini_file = 'hosts.ini'

# Ruta del archivo CSV
csv_file = 'hosts.csv'

# Función para convertir el archivo INI a CSV
def convert_ini_to_csv(ini_file, csv_file):
    # Crear lista para almacenar los datos del CSV
    csv_data = []

    # Leer el archivo INI
    with open(ini_file, 'r') as file:
        for line in file:
            # Buscar la dirección IP usando una expresión regular
            match = re.search(r'ansible_host=(\d+\.\d+\.\d+\.\d+)', line)
            if match:
                ip_address = match.group(1)
                csv_data.append([ip_address])

    # Escribir los datos en el archivo CSV
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Escribir encabezados
        writer.writerow(['IP'])
        # Escribir los datos de cada host
        writer.writerows(csv_data)

    print(f"Archivo CSV generado: {csv_file}")

# Llamar a la función para convertir el archivo INI a CSV
convert_ini_to_csv(ini_file, csv_file)
