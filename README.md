## 🚀 Instalación y Uso

Sigue estos pasos detallados en tu terminal de Kali Linux para clonar el repositorio, configurar el entorno de Python e iniciar el laboratorio:

### 1. Clonar el repositorio y entrar a la carpeta
Descarga la herramienta a tu máquina local y accede de inmediato al directorio del proyecto usando el comando `cd`:
```bash
git clone [https://github.com/redsocietydev/nebulaurl.git](https://github.com/redsocietydev/nebulaurl.git)
cd nebulaurl
2. Actualizar el sistema e instalar Python 3
Asegúrate de contar con el entorno de ejecución de Python y su gestor de paquetes (pip) actualizados en tu sistema operativo:

Bash
sudo apt update
sudo apt install python3 python3-pip -y
3. Instalar la biblioteca requerida
Instala el motor de conexión externa para que funcionen las APIs de acortamiento de enlaces:

Bash
pip3 install pyshorteners
4. Asignar permisos de ejecución al script
Otorga los permisos binarios necesarios al script para poder lanzarlo como una aplicación nativa en Linux:

Bash
chmod +x nebulaurl.py
5. Desplegar el laboratorio
Inicia el simulador interactivo ejecutando la herramienta desde la consola:

Bash
./nebulaurl.py
