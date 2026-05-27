#!/usr/bin/env python3
"""
Red Society - Academia de Tecnologías de la Información
Módulo Educativo: Análisis de Estructuras de URLs y Ofuscación (RFC 3986)
Proyecto: NebulaURL (Simulador de Enmascaramiento Ético)
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

# Paleta de colores ANSI - Lila Cósmico y Celeste Elíptico
LILA = '\033[38;5;141m'       
CELESTE = '\033[38;5;81m'      
RED = '\033[31m'
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
    print(f"    {CELESTE}          N  E  B  U  L  A    U  R  L              {RESET}")
    print(f"    {LILA}=================================================={RESET}")
    print(f"    {CELESTE}╰➤ Academia    : {RESET}Red Society")
    print(f"    {CELESTE}╰➤ Laboratorio : {RESET}Analizador Sintáctico RFC 3986")
    print(f"    {CELESTE}╰➤ Versión     : {RESET}{VERSION}")
    print(f"    {CELESTE}╰➤ Ámbito      : {RESET}Fines Educativos / Auditoría Autorizada\n")
    
    # Deslinde de responsabilidad
    print(f"{RED}    ------------ DESLINDE DE RESPONSABILIDAD ------------")
    print("    Este script ha sido diseñado exclusivamente con fines pedagógicos")
    print("    para demostrar fallas de percepción visual en la sintaxis HTTP.")
    print(f"    El autor no promueve ni se responsabiliza por su mal uso.{RESET}\n")

def validar_url_objetivo(url):
    """Valida que la URL de entrada tenga un formato web estructurado."""
    patron = re.compile(r'^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(:\d{1,5})?(/.*)?$')
    if not patron.match(url):
        raise ValueError("Formato de URL inválido. Debe incluir http:// o https://")

def validar_dominio_simulado(dominio):
    """Asegura que el dominio de simulación no contenga caracteres extraños."""
    patron = re.compile(r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    if not patron.match(dominio):
        raise ValueError("Dominio simulado inválido. Ejemplo correcto: gmail.com")

def limpiar_palabras_clave(texto):
    """Verifica la longitud y formato de las etiquetas de texto."""
    texto_limpio = texto.strip()
    if " " in texto_limpio:
        raise ValueError("Las palabras clave no deben contener espacios. Use guiones '-'")
    if len(texto_limpio) > 20:
        raise ValueError("Las palabras clave no deben exceder los 20 caracteres.")
    return texto_limpio

def enmascarar_cadena(dominio, etiqueta, url_acortada):
    """
    Aplica la lógica del RFC 3986 interpretando el texto previo al '@'
    como parámetros de autenticación de usuario.
    """
    url_parseada = urlparse(url_acortada)
    return f"{url_parseada.scheme}://{dominio}-{etiqueta}@{url_parseada.netloc}{url_parseada.path}"

def main():
    mostrar_banner()
    
    # Bloque de captura y validación de datos
    while True:
        try:
            enlace_real = input(f"{CELESTE}[?] Ingrese la URL real del laboratorio (ej. Ngrok): {RESET}").strip()
            validar_url_objetivo(enlace_real)
            break
        except ValueError as err:
            print(f"{RED}[!] {err}{RESET}")

    while True:
        try:
            dominio_falso = input(f"{LILA}[?] Ingrese el dominio de referencia (ej. whatsapp.com): {RESET}").strip()
            validar_dominio_simulado(dominio_falso)
            break
        except ValueError as err:
            print(f"{RED}[!] {err}{RESET}")

    print(f"\n{LILA}[*] Conectando con los proveedores de acortamiento de NebulaURL...{RESET}\n")
    
    # Inicialización del motor de acortamiento
    instancia_short = pyshorteners.Shortener()
    servidores = [
        ("TinyURL", instancia_short.tinyurl),
        ("DaGd", instancia_short.dagd),
        ("ClckRu", instancia_short.clckru)
    ]

    # Estructura de tabla limpia y elegante en consola
    print(f"{LILA}┌──────────────────────┬─────────────────────────────────────────────────────────────┐")
    print(f"│ {CELESTE}Simulated Domain     {LILA}│ {CELESTE}Resulting Link (NebulaURL)                                  {LILA}│")
    print(f"├──────────────────────┼─────────────────────────────────────────────────────────────┤{RESET}")
    
    enlaces_generados = 0

    for nombre, servicio in servidores:
        try:
            url_corta = servicio.short(enlace_real)
            resultado_final = enmascarar_cadena(dominio_falso, acento_etiqueta, url_corta)
            
            # Ajuste de espacios exacto para Kali
            col_api = f"[API: {nombre}.com]".ljust(20)
            print(f"{LILA}│{RESET} {col_api} {LILA}│{RESET} {resultado_final}")
            enlaces_generados += 1
        except Exception:
            continue

    print(f"{LILA}└──────────────────────┴─────────────────────────────────────────────────────────────┘{RESET}")

    if enlaces_generados == 0:
        print(f"\n{RED}[!] Todos los proveedores externos rechazaron la URL debido a políticas de restricción de dominios dev/app.{RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{RED}[!] Ejecución interrumpida por el usuario.{RESET}")
        sys.exit(0)
