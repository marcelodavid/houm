# houm

Backend Tech Lead Challenge
License: MIT

# Problema

En Houm tenemos un gran equipo de Houmers que muestran las propiedades y solucionan todos los problemas que podrían ocurrir en ellas. Ellos son parte fundamental de nuestra operación y de la experiencia que tienen nuestros clientes. Es por esta razón que queremos incorporar ciertas métricas para monitorear cómo operan, mejorar la calidad de servicio y para asegurar la seguridad de nuestros Houmers.


# Requisitos

## Crear un servicio REST que:

    1. Permita que la aplicación móvil mande las coordenadas del Houmer
    2. Para un día retorne todas las coordenadas de las propiedades que visitó y cuanto tiempo se quedó en cada una
    3. Para un día retorne todos los momentos en que el houmer se trasladó con una velocidad superior a cierto parámetro

Es necesario [Docker](https://get.docker.com/) para levantar los servicios.

```
curl -fsSL https://get.docker.com -o get-docker.sh
cmod + x get-docker.sh
sh get-docker.sh
```

[docker-compose](https://docs.docker.com/compose/install/) para componer los microservicios

## Como ejecutar el codigo localmente
### Se orquesta y contruye los microservicios, los mas importantes:
1. Django
2. Postgresql con PostGis
3. Redis

```bash
export COMPOSE_FILE=loca.yml

# build de los servivios
docker-compose build

# Una vez contruida todas las imagenes
docker-compose up -d
```

### Creamos un superusuario
```bash
export COMPOSE_FILE=local.yml
docker-compose run --rm django python manage.py createsuperuser
```

### Ver el estado de los servicios
```
docker-compose ps
```
## Pruebas

Lo necesario para probar las APIs son las propiedades que recorren los houmers y la creacion de houmers.
Para eso empleamos el [admin](http://localhost:8000/admin/) que nos facilita Django

1. Registramos las propiedades

![Muestra Carga de Propiedad](https://github.com/marcelodavid/houm/blob/master/propiedad.png?raw=true)
prop
> Puede utilizar la colecion de postman para comenzar con las pruebas