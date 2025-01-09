# Ejercicio 3

Archivo `musica.xml`:

```xml
<catalogo>
  <album id="1" genero="Rock">
    <titulo>The Dark Side of the Moon</titulo>
    <artista>Pink Floyd</artista>
    <anio>1973</anio>
    <precio>20.00</precio>
  </album>
  <album id="2" genero="Pop">
    <titulo>Thriller</titulo>
    <artista>Michael Jackson</artista>
    <anio>1982</anio>
    <precio>18.00</precio>
  </album>
  <album id="3" genero="Rock">
    <titulo>Abbey Road</titulo>
    <artista>The Beatles</artista>
    <anio>1969</anio>
    <precio>25.00</precio>
  </album>
  <album id="4" genero="Jazz">
    <titulo>Kind of Blue</titulo>
    <artista>Miles Davis</artista>
    <anio>1959</anio>
    <precio>15.00</precio>
  </album>
</catalogo>
```

Pregunta 1. Devuelve todos los títulos de los álbumes.
```xquery
for $album in doc("musica.xml")/catalogo/album
return $album/titulo
```

Pregunta 2. Devuelve los álbumes cuyo precio es mayor a 18.
```xquery
for $album in doc("musica.xml")/catalogo/album
where $album/precio > 18
return $album
```

Pregunta 3. Lista los títulos y géneros de todos los álbumes.
```xquery
for $album in doc("musica.xml")/catalogo/album
return ($album/titulo) | ($album/@genero)
```

Pregunta 4. Calcula el precio promedio de los álbumes (usa `let`).
```xquery
let $promedio := doc("musica.xml")/catalogo/album/precio
return avg($promedio)
```

Pregunta 5. Encuentra los álbumes de género "Rock".
```xquery
for $album in doc("musica.xml")/catalogo/album
where $album/@genero = "Rock"
return $album
```

Pregunta 6. Ordena los álbumes por año de lanzamiento.
```xquery
for $album in doc("musica.xml")/catalogo/album
order by $album/anio ascending
return $album
```

Pregunta 7. Devuelve el álbum más caro.
```xquery
for $album in doc("musica.xml")/catalogo/album
where $album/precio = max(//precio)
return $album
```

Pregunta 8. Devuelve los títulos y los precios con un descuento del 20%.
```xquery
for $album in doc("musica.xml")/catalogo/album
let $descuento := $album/precio * 0.8
return <album>
	<titulo>{$album/titulo}</titulo>
    <descuento>{$descuento}</descuento>
</album>
```
Pregunta 9. Devuelve los álbumes lanzados antes de 1975.
```xquery
for $album in doc("musica.xml")/catalogo/album
where $album/anio < 1975
return $album
```

Pregunta 10. Calcula el precio total de todos los álbumes.
```xquery
let $precios := doc("musica.xml")/catalogo/album/precio
return sum($precios)
```