#!/usr/bin/env python3
"""
Red Society - Academia de Tecnologías de la Información
Módulo Educativo: Análisis de Estructuras de URLs y Ofuscación (RFC 3986)
Propósito: Demostración técnica de manipulación de parámetros de autenticación en HTTP.
"""

import re
import sys
from urllib.parse import urlparse

# Intentar importar las dependencias necesarias
try:
    import pyshorteners
except ImportError:
    print("[!] Error: Se requiere la librería 'pyshorteners'.")
    print("    Instálalas ejecutando: pip3 install pyshorteners")
    sys.exit(1)

# Paleta de colores para la interfaz de la consola
RED = '\033[31m'
GREEN = '\033[32m'
CYAN = '\033[36m'
YELLOW = '\033[33m'
LILA = '\033[35m'
CELESTE = '\033[36m'
RESET = '\033[0m'

VERSION = '1.0.0'

def mostrar_banner():
    """Genera la elipse de alta densidad completa usando bloques sólidos sin texto central"""
    print(f"""
{LILA}                        ░░▒▒▓▓██████▓▓▒▒░░
{LILA}                 ░░▒▒▓▓████████████████████▓▓▒▒░░
{LILA}              ░▒▓████████████████████████████████▓▒░
{LILA}           ░▒▓██████████{CELESTE}████████████████{LILA}██████████▓▒░
{LILA}          ▒▓████████{CELESTE}████████████████████████{LILA}████████▓▒
{LILA}         ▒▓██████{CELESTE}████████████▓▓▓▓▓▓████████████{LILA}██████▓▒
{LILA}        ░▓█████{CELESTE}██████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████████{LILA}████▓░
{LILA}        ░▓█████{CELESTE}██████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████████{LILA}████▓░
{LILA}        ░▓█████{CELESTE}██████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████████{LILA}████▓░
{LILA}         ▒▓██████{CELESTE}████████████▓▓▓▓▓▓████████████{LILA}██████▓▒
{LILA}          ▒▓████████{CELESTE}████████████████████████{LILA}████████▓▒
{LILA}           ░▒▓██████████{CELESTE}████████████████{LILA}██████████▓▒░
{LILA}              ░▒▓████████████████████████████████▓▒░
{LILA}                 ░░▒▒▓▓████████████████████▓▓▒▒░░
{LILA}                        ░░▒▒▓▓██████▓▓▒▒░░
    """)
    
    # Rótulo del software institucional
    print(f"    {LILA}=================================================={RESET}")
    print(f"    {CELESTE}          N  E  B  U  L  A   U  R  L              {RESET}")
    print(f"    {LILA}=================================================={RESET}")
    print(f"    {CELESTE}╰➤ Academia    : {RESET}Red Society")
    print(f"    {CELESTE}╰➤ Laboratorio : {RESET}Analizador Sintáctico RFC 3986")
    print(f"    {CELESTE}╰➤ Versión     : {RESET}{VERSION}")
    print(f"    {CELESTE}╰➤ Ámbito      : {RESET}Fines Educativos / Auditoría Autorizada\n")
    
    # Deslinde de responsabilidad
    print(f"{RED}    ------------ DESLINDE DE RESPONSABILIDAD ------------")
    print("    Este script ha sido diseñado exclusivamente con fines pedagogicos")
    print("    para demostrar fallas de percepcion visual en la sintaxis HTTP.")
    print(f"    El autor no promueve ni se responsabiliza por su mal uso.{RESET}\n")

def validar_url_objetivo(url):
    """Valida que la URL de entrada tenga un formato web estruturado."""
    patron = re.compile(r'^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(:\d{1,5})?(/.*)?$')
    if not patron.match(url):
        raise ValueError("Formato de URL invalido. Debe incluir http:// o https://")

def validar_dominio_simulado(dominio):
    """Asegura que el dominio de simulacion no contenga caracteres extranos o espacios."""
    patron = re.compile(r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    if not patron.match(dominio):
        raise ValueError("Dominio simulado invalido. Ejemplo correcto: whatsapp.com")

def limpiar_ingenieria_social(texto):
    """Verifica que el argumento de ingeniería social no contenga espacios ni caracteres raros."""
    texto_limpio = texto.strip()
    if " " in texto_limpio:
        raise ValueError("El texto de ingeniería social no debe contener espacios. Usa guiones '-'")
    if len(texto_limpio) > 25:
        raise ValueError("El texto descriptivo no debe exceder los 25 caracteres.")
    return texto_limpio

def enmascarar_cadena(dominio, texto_is, url_acortada):
    """
    Aplica la logica del RFC 3986 interpretando el texto previo al '@'
    como parametros de autenticacion de usuario.
    """
    url_parseada = urlparse(url_acortada)
    # Estructura corregida: esquema://dominio_simulado-texto_is@host_real/ruta
    return f"{url_parseada.scheme}://{dominio}-{texto_is}@{url_parseada.netloc}{url_parseada.path}"

def main():
    mostrar_banner()
    
    # Bloque de captura y validacion de datos (3 Preguntas Completas)
    while True:
        try:
            enlace_real = input(f"{GREEN}[?] Ingrese la URL real del laboratorio (ej. Ngrok): {RESET}").strip()
            validar_url_objetivo(enlace_real)
            break
        except ValueError as err:
            print(f"{RED}[!] {err}{RESET}")

    while True:
        try:
            dominio_falso = input(f"{YELLOW}[?] Ingrese el dominio de referencia (ej. whatsapp.com): {RESET}").strip()
            validar_dominio_simulado(dominio_falso)
            break
        except ValueError as err:
            print(f"{RED}[!] {err}{RESET}")

    while True:
        try:
            texto_is = input(f"{CYAN}[?] Ingrese el texto de ingeniería social (ej. login-secure): {RESET}").strip()
            texto_is = limpiar_ingenieria_social(texto_is)
            break
        except ValueError as err:
            print(f"{RED}[!] {err}{RESET}")

    print(f"\n{YELLOW}[*] Conectando con los proveedores de acortamiento de NebulaURL...{RESET}\n")
    
    # Dibujar la cabecera de la tabla ajustada para visualizar el texto completo
    print(f"{CYAN}{'-'*30}┬{'-'*65}{RESET}")
    print(f" {CYAN}Simulated Context / Domain{RESET}     │ {CYAN}Resulting Link (NebulaURL){RESET}")
    print(f"{CYAN}{'-'*30}┼{'-'*65}{RESET}")

    # Inicializacion del motor de acortamiento
    instancia_short = pyshorteners.Shortener()
    servidores = [
        ("TinyURL", instancia_short.tinyurl),
        ("DaGd", instancia_short.dagd),
        ("ClckRu", instancia_short.clckru)
    ]

    enlaces_generados = 0

    for nombre, servicio in servidores:
        try:
            url_corta = servicio.short(enlace_real)
            # Pasamos las tres variables para construir de forma segura el enlace interactivo
            resultado_final = enmascarar_cadena(dominio_falso, texto_is, url_corta)
            
            contexto_visual = f"{dominio_falso}-{texto_is}"
            print(f" {contexto_visual:<28} │ {GREEN}{resultado_final}{RESET}")
            enlaces_generados += 1
        except Exception:
            continue

    print(f"{CYAN}{'-'*30}┴{'-'*65}{RESET}\n")

    if enlaces_generados == 0:
        print(f"{RED}[!] Error técnico: No se pudo conectar con las APIs de acortamiento. Verifique su conexión.{RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{RED}[!] Ejecución interrumpida por el usuario.{RESET}")
        sys.exit(0)
