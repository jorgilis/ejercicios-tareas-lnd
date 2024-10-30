# Direcionamiento IP
El direccionamiento IP es un componente esencial en las redes de computadoras,permitiendo la identificación de dispositivos y la correcta entrega de datos. Las direcciones Ip se dividen en clases y tienen rasgos específicos según su uso.
## Clases de Direcciones IP
A continuación, se muestra una tabla con las clases de direcciones IP, sus rangos, máscaras de subred, rangos privados y el numero de hosts disponibles por cada clase:

| Clase | Rango de direcciones | Máscara de subred | Rango privado| Numero de hosts |
| --------- | --------- | --------- | -------- | --------|
| A | 0.0.0.0 - 127.255.255.255 | 255.0.0.0|10.0.0.0 - 10.255.255.255 | 16,777,214
| B | 128.0.0.0 - 191.255.255.255 | 255.255.0.0|172.16.0.0 - 172.31.255.255| 65,534
| C | 128.0.0.0 - 191.255.255.255 | 255.255.255.0|192.168.0.0 - 192.168.255.255 | 254
| D | 224.0.0.0 - 239.255.255.255 | No aplica|No aplica | Multicast (No asignado)
| E | 240.0.0.0 - 255.255.255.255 | No aplica|No aplica | Reservado (Bo asignado)
## Descripción de las clases
* __Clase A__: Usada principalmente para grandes redes, como empresas multinacionales. Soporta un gran número de dispositivos.
*  __Clase B__: Orientada a redes medianas, como instituciones educativas o grandes empresas.
*  __Clase C__: Utilizada para redes pequeñas, como oficinas o redes domésticas.
*  __Clase D__: Reservada para multicast.
*  __Clase E__: Reservada para usos futuros o experimentales.

Para más informacion sobre redes y direccionamiento IP, consulta la documentación y recursos adicionales disponibles en el material de estudio.