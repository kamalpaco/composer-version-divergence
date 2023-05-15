# Proyecto de Visualización de Dependencias con Composer

Este proyecto tiene como objetivo visualizar la divergencia de versiones de las dependencias en archivos `composer.json` de diferentes proyectos.

## Requisitos previos

Asegúrate de tener instalado Docker y Docker Compose en tu sistema antes de continuar.

- Docker: [Instrucciones de instalación](https://docs.docker.com/get-docker/)
- Docker Compose: [Instrucciones de instalación](https://docs.docker.com/compose/install/)

## Configuración del entorno de desarrollo

Sigue estos pasos para configurar el entorno de desarrollo:

1. Clona este repositorio en tu máquina local:
git clone https://github.com/tu-usuario/composer-dependency-visualization.git

2. Navega al directorio del proyecto:
> cd composer-dependency-visualization

## Iniciando el entorno de desarrollo
Una vez que hayas configurado el entorno de desarrollo, puedes seguir estos pasos para iniciar el contenedor y comenzar a desarrollar:

1. Incluye los ficheros composer.json a evaluar en el directorio "projects"

2. Ejecuta el siguiente comando para construir la imagen del contenedor y levantar los servicios:

> docker-compose up

Esto instalará las dependencias de Python y levantará el contenedor.

## Contribución
Si deseas contribuir a este proyecto, sigue estos pasos:

1. Realiza un fork de este repositorio.

2. Crea una rama (git checkout -b feature/nueva-caracteristica) para tu contribución.

3. Realiza los cambios y realiza confirmaciones (git commit -am 'Agrega nueva característica').

4. Sube tus cambios a tu repositorio remoto (git push origin feature/nueva-caracteristica).

5. Abre una solicitud de extracción en este repositorio.


## Licencia
Este proyecto está licenciado bajo la Licencia MIT.