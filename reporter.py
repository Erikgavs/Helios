import os
from pydoc import text
import psutil
import subprocess
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

def enviar_mensaje():
    load_dotenv()
    remitente = os.getenv("REMITENTE")
    destinatario = os.getenv("DESTINATARIO")
    password = os.getenv("PASSWORD")

    # PROCESS REGISTER
    docker_info = subprocess.run(["docker", "ps"], text=True, capture_output=True) # Info de docker
    docker_info_output = docker_info.stdout

    private_ip = subprocess.run("ip a | grep '/24'", text=True, shell=True, capture_output=True)
    private_ip_output = private_ip.stdout

    public_ip = subprocess.run(["curl", "ifconfig.me"], text=True, capture_output=True)
    public_ip_output = public_ip.stdout

    ping_server = subprocess.run(["ping", "-c", "1", "192.168.5.200"], text=True, capture_output=True)
    ping_server_output = ping_server.stdout

    # Meterle ps aux

    # SYS INFO
    porcentaje_mem = psutil.cpu_percent(interval=1)
    memoria = psutil.virtual_memory()
    memoria_usada = memoria.used / 1024**2 # Conversión de Bytes a MB
    disco = psutil.disk_usage("/")
    disco_usado = disco.used / 1024**2 # Conversión de Bytes a MB

    # :.2f => Aceptamos 2 decimales
    info =f"""
    Reporte diario de Prometeus

    Sistema
    Uso de CPU: {porcentaje_mem:.2f}%
    Memoria: {memoria_usada:.2f} Mb
    Uso del Disco: {disco_usado:.2f} Mb

    Ping al server
    {ping_server_output}

    Información de contenedores Docker
    Contenedores: {docker_info_output}

    IP privada
    ip: {private_ip_output}

    IP pública
    ip: {public_ip_output}

    """

    mensaje = MIMEText(info)
    mensaje["Subject"] = "Reporte diario de Prometeus"
    mensaje["From"] = remitente
    mensaje["To"] = destinatario

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(remitente, password)
            server.sendmail(remitente, destinatario, mensaje.as_string())
        print("Correo envíado correctamente")
    except Exception as e:
        print(f"Ha habido un error al enviar el correo {e}")
