# Proyecto de Ansible para Gestión de Switches Extreme EXOS

Este proyecto de Ansible está diseñado para gestionar y extraer configuraciones de switches Extreme EXOS. Incluye scripts para convertir archivos de inventario INI a CSV, agregar hosts al archivo `known_hosts`, y un playbook de Ansible para ejecutar comandos en los switches y guardar la salida.

## Estructura del Proyecto

- `add_fingerprint.py`: Script para agregar los fingerprints de hosts al archivo `known_hosts`.
- `add_known_hosts.yml`: Playbook de Ansible para agregar hosts específicos al archivo `known_hosts`.
- `configs/`: Directorio donde se almacenan las configuraciones extraídas de los switches.
- `convertcsv.py`: Script para convertir un archivo de inventario INI a formato CSV.
- `group_vars/extreme_switches.yml`: Variables específicas para los switches Extreme EXOS.
- `hosts.csv`: Archivo CSV que contiene las direcciones IP de los hosts.
- `hosts.ini`: Archivo de inventario en formato INI que contiene los hosts y sus detalles.
- `library/`: Directorio para módulos personalizados de Ansible.
- `playbook.yml`: Playbook de Ansible para extraer configuraciones de los switches Extreme EXOS.
- `remove_knowhosts.py`: Script para eliminar el archivo `known_hosts`.
- `run.sh`: Script bash para ejecutar los scripts Python y el playbook de Ansible.

## Requisitos

- Python 3
- Ansible
- Acceso SSH a los switches Extreme EXOS

## Instalación y Uso

1. Clona este repositorio:
   ```bash
   git clone <URL del repositorio>
   cd <nombre del directorio>
Asegúrate de tener los requisitos instalados:

bash
Copiar código
pip install ansible
Configura los archivos de inventario y variables:

hosts.ini: Añade tus hosts y credenciales.
group_vars/extreme_switches.yml: Asegúrate de que las variables sean correctas para tu entorno.
Ejecuta el script principal:

bash
Copiar código
./run.sh
Descripción de los Scripts
add_fingerprint.py
Este script lee un archivo CSV (hosts.csv) que contiene direcciones IP y agrega los fingerprints de estos hosts al archivo known_hosts.

add_known_hosts.yml
Playbook de Ansible que asegura que los hosts especificados estén en el archivo known_hosts del usuario.

convertcsv.py
Convierte un archivo de inventario INI (hosts.ini) en un archivo CSV (hosts.csv). Extrae las direcciones IP de los hosts y las guarda en el formato CSV.

group_vars/extreme_switches.yml
Contiene variables específicas para la conexión a los switches Extreme EXOS, incluyendo usuario, contraseña y parámetros de conexión SSH.

hosts.csv
Archivo CSV que contiene las direcciones IP de los hosts. Este archivo es generado por convertcsv.py.

hosts.ini
Archivo de inventario en formato INI que define los hosts y sus credenciales. Es la fuente de datos para convertcsv.py.

playbook.yml
Playbook de Ansible que ejecuta varios comandos en los switches Extreme EXOS y guarda la salida en archivos de texto dentro del directorio configs/.

remove_knowhosts.py
Script que elimina el archivo known_hosts para limpiar los fingerprints almacenados.

run.sh
Script bash que automatiza la ejecución de los scripts Python y el playbook de Ansible en el orden correcto.

Contribuciones
Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request.

Licencia
Este proyecto está licenciado bajo la MIT License.
