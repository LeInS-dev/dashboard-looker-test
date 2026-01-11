#!/usr/bin/env python3
"""
Script para crear usuarios en el sistema de autenticación del dashboard Looker.
Genera hashes de contraseñas con bcrypt y los almacena en users.json.
"""

import bcrypt
import json
import os
from datetime import datetime
from getpass import getpass

USERS_FILE = "users.json"


def hash_password(password: str) -> str:
    """Genera un hash bcrypt de la contraseña."""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')


def verify_password(password: str, password_hash: str) -> bool:
    """Verifica una contraseña contra un hash."""
    return bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8'))


def load_users() -> dict:
    """Carga el archivo users.json si existe."""
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    return {"users": []}


def save_users(users_data: dict):
    """Guarda los usuarios en users.json."""
    with open(USERS_FILE, 'w') as f:
        json.dump(users_data, f, indent=2)
    # Establecer permisos restrictivos (solo lectura para el propietario)
    os.chmod(USERS_FILE, 0o600)


def user_exists(username: str, users_data: dict) -> bool:
    """Verifica si un usuario ya existe."""
    return any(user['username'] == username for user in users_data['users'])


def create_user(username: str = None, password: str = None, skip_confirmation: bool = False):
    """Crea un nuevo usuario interactivo o con parámetros.

    Args:
        username: Nombre de usuario (None para modo interactivo)
        password: Contraseña (None para modo interactivo)
        skip_confirmation: Si True, no pide confirmación de contraseña
    """
    users_data = load_users()

    # Solicitar username si no se proporcionó
    if not username:
        username = input("Nombre de usuario: ").strip()

    if not username:
        print("Error: El nombre de usuario no puede estar vacío.")
        return False

    # Verificar si el usuario ya existe
    if user_exists(username, users_data):
        print(f"Error: El usuario '{username}' ya existe.")
        return False

    # Solicitar password si no se proporcionó
    if not password:
        password = getpass("Contraseña: ")

    if not password:
        print("Error: La contraseña no puede estar vacía.")
        return False

    # Confirmar password solo si no se especifica skip_confirmation
    if not skip_confirmation:
        password_confirm = getpass("Confirmar contraseña: ")
        if password != password_confirm:
            print("Error: Las contraseñas no coinciden.")
            return False

    # Crear el usuario
    password_hash = hash_password(password)
    new_user = {
        "username": username,
        "password_hash": password_hash,
        "created_at": datetime.now().isoformat()
    }

    users_data['users'].append(new_user)
    save_users(users_data)

    print(f"\n✓ Usuario '{username}' creado exitosamente.")
    print(f"  Credenciales almacenadas en: {USERS_FILE}")
    return True


def list_users():
    """Lista todos los usuarios (sin mostrar contraseñas)."""
    users_data = load_users()

    if not users_data['users']:
        print("No hay usuarios registrados.")
        return

    print(f"\n{'Usuario':<20} {'Creado':<20}")
    print("-" * 40)
    for user in users_data['users']:
        created_date = user.get('created_at', 'N/A')[:19]
        print(f"{user['username']:<20} {created_date:<20}")


def main():
    """Función principal del script."""
    print("\n" + "=" * 50)
    print("  Gestión de Usuarios - Dashboard Looker")
    print("=" * 50 + "\n")

    # Verificar si existe el archivo users.json
    if not os.path.exists(USERS_FILE):
        print(f"Archivo {USERS_FILE} no encontrado.")
        print("Se creará automáticamente al agregar el primer usuario.\n")

    print("Opciones:")
    print("  1. Crear nuevo usuario")
    print("  2. Listar usuarios existentes")
    print("  3. Salir")

    opcion = input("\nSeleccione una opción [1-3]: ").strip()

    if opcion == "1":
        create_user()
    elif opcion == "2":
        list_users()
    elif opcion == "3":
        print("Saliendo...")
    else:
        print("Opción inválida.")


if __name__ == "__main__":
    # Si se pasan argumentos desde línea de comandos
    import sys
    if len(sys.argv) > 1:
        if sys.argv[1] == "create" and len(sys.argv) >= 4:
            username = sys.argv[2]
            password = sys.argv[3]
            create_user(username, password, skip_confirmation=True)
        elif sys.argv[1] == "list":
            list_users()
        else:
            print("Uso:")
            print("  Crear usuario: python create_user.py create <usuario> <contraseña>")
            print("  Listar usuarios: python create_user.py list")
            print("  Modo interactivo: python create_user.py")
    else:
        main()
