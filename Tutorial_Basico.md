

# 1. Preparando el entorno

## 1.1 Instalando WSL2

Fuente: [[https://learn.microsoft.com/es-es/windows/wsl/install]]

Abrir la PowerShell y verificar si lo tenemos instalado:
```PowerShell
PS C:\User\gucr6> wsl --list
```

Si ya lo tiene instalado debe tener una salida con las distribuciones de WSL ya instaladas. Caso contrario listamos las disponibles online:
```PowerShell
PS C:\User\gucr6> wsl --list --online
```

Nos aparecerá una salida como la siguiente:


Instalamos la versión deseada, en nuestro caso para facilitar la descarga y tener lo mínimo necesario la distro Debian:

```PowerShell
PS C:\User\gucr6> wsl --install Debian
```

Iniciará la descarga e instalación, luego nos pedirá definir un usuario y su respectiva password:





