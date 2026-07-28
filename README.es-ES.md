## fast-api-template

[![Python](https://img.shields.io/badge/Python-3.10+-yellow?style=for-the-badge&logo=python&logoColor=white&labelColor=101010)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-00a393?style=for-the-badge&logo=fastapi&logoColor=white&labelColor=101010)](https://fastapi.tiangolo.com)

### 1. Introducción del Proyecto

Este proyecto está basado en [FastAPI](https://fastapi.tiangolo.com/zh/tutorial/first-steps/).
El objetivo es aprender a utilizar el framework FastAPI y construir una plantilla de proyecto que facilite la creación de nuevos proyectos en el futuro. Espero que este proyecto sea de ayuda para los desarrolladores que quieran aprender y utilizar FastApi.

> <span style="color: red; ">@Nota:
> Debido a que los lenguajes que utilizo habitualmente en mi trabajo son PHP y Go, las normas de codificación en el framework no siguen estrictamente las especificaciones oficiales de Python, especialmente en los nombres de variables y funciones~</span>

- [Documentación de fastapi en chino](https://fastapi.tiangolo.com/zh/tutorial/first-steps/)

### 2. Estructura del Directorio

> <span style="color: red; ">@Nota: El siguiente directorio es solo referencial; habrá algunos ajustes mientras el proyecto siga en desarrollo.</span>

```shell
├── app
│   ├── __init__.py
│   ├── config  # Relacionado con la configuración
│   │   └── __init__.py
│   ├── constant  # Relacionado con constantes
│   │   └── __init__.py
│   ├── dao # Encapsulación de métodos de consulta de datos
│   │   ├── models # Archivos de modelos de datos, corresponden a la estructura de tablas
│   │   └── __init__.py
│   ├── dependencies  # Encapsulación de funciones de dependencia
│   │   └── __init__.py
│   ├── errors  # Manejo de excepciones
│   │   └── __init__.py
│   ├── middleware # Middleware
│   │   └── __init__.py
│   ├── router # Rutas (también pueden entenderse como controladores)
│   │   ├── __init__.py
│   │   ├── admin_router.py # Interfaces de administración
│   │   └── demo_router.py # Interfaces de demostración
│   ├── types # Modelos de Pydantic para parámetros de entrada y salida
│   │   ├── __init__.py
│   │   ├── request # Modelos de entrada
│   │   └── response # Modelos de salida
│   ├── service # Implementación de la lógica de negocio específica
│   │   ├── __init__.py
│   └── utils # Clases de utilidad
│       ├── __init__.py
│       └── str_util.py
├── bin # Scripts relacionados
│   ├── genmodels.sh # Script para generar modelos
│   └── updateRequirements.sh # Script para actualizar dependencias del proyecto
├── logs # Directorio de logs
│   └── app.log
├── static # Directorio de recursos estáticos
│   ├── a.txt
│   └── test.jpg
├── requirements.txt # Archivo de dependencias
├── README.md  # Introducción del proyecto
├── main.py # Archivo de entrada
└── tests # Directorio de pruebas unitarias
    ├── __init__.py
    └── local_test.py
```

### 3. Inicio del Proyecto

#### 3.1 Instalación de dependencias

```shell
➜ pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

#### 3.2 Inicio del servicio

```sh
# Inicio: Se puede especificar el archivo de configuración de entorno test(.env.test) o prod(.env.prod)
➜  ./server.sh start --env=test
Preparando para iniciar la aplicación...
Ejecutando script: python main.py  --env=test
Obteniendo archivo de configuración:  .env.test
Imprimiendo configuración del proyecto: ...
INFO:     Started server process [36836]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8082 (Press CTRL+C to quit)

# Detener
➜  ./server.sh stop 

# Reiniciar
➜  ./server.sh restart 
```

### 4. Estado del Proyecto

En proceso de aprendizaje y desarrollo continuo...

### 5. Historial del Proyecto

- [Python Frameworks (1): FastApi - Guía rápida de inicio](https://mp.weixin.qq.com/s/AY_MGluXAgr27m2nPByJFw)
- [Python Frameworks (2): FastApi - Recepción y validación de parámetros](https://mp.weixin.qq.com/s/J2_gJxJk2VLfMXgoH1l8Cw)
- [Python Frameworks (3): FastApi - Modelos de respuesta](https://mp.weixin.qq.com/s/okmkZXWZ3qwS1cnAceky0w)
- [Python Frameworks (4): FastApi - Manejo de errores](https://mp.weixin.qq.com/s/W6TxoQ_i-CUCKRhorZReaw)
- [Python Frameworks (5): FastApi - Uso de Middleware](https://mp.weixin.qq.com/s/2MFPnly7pv_dhKT3zGw3VA)
- [Python Frameworks (6): FastApi - Gestión de configuración](https://mp.weixin.qq.com/s/3TQYLGebfsEmZt_FQBIV1Q)
- [Python Frameworks (7): FastApi - Dependencias](https://mp.weixin.qq.com/s/UvTytHAkC2bue-1ee6Ib1w)
- [Python Frameworks (8): FastApi - Manejo de archivos](https://mp.weixin.qq.com/s/zOxkbJkDoQCA0fCkWGF00Q)
