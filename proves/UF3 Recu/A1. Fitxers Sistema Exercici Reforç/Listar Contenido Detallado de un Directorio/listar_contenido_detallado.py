import os
import stat
import time

def obtener_info_archivo(archivo):
    info = os.stat(archivo)
    permisos = stat.filemode(info.st_mode)
    mtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(info.st_mtime))
    tamaño = info.st_size
    return permisos, mtime, tamaño

def listar_contenido_detallado(directorio):
    contenido = os.listdir(directorio)
    print("Contenido detallado del directorio:")
    for item in contenido:
        ruta_completa = os.path.join(directorio, item)
        if os.path.isfile(ruta_completa):
            permisos, mtime, tamaño = obtener_info_archivo(ruta_completa)
            print(f"Nombre: {item}, Tamaño: {tamaño} bytes, Última modificación: {mtime}, Permisos: {permisos}")
        elif os.path.isdir(ruta_completa):
            info = os.stat(ruta_completa)
            permisos = stat.filemode(info.st_mode)
            mtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(info.st_mtime))
            espacio_libre = info.f_bsize * info.f_bavail
            print(f"Nombre: {item}, Espacio libre: {espacio_libre} bytes, Última modificación: {mtime}, Permisos: {permisos}")

