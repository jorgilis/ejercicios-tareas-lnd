# Ejercicio 1. 

Archivo `biblioteca.xml`:

```xml
<biblioteca>
  <libro id="1" genero="Ficción">
    <titulo>1984</titulo>
    <autor pais="Reino Unido">George Orwell</autor>
    <precio moneda="USD">19.99</precio>
  </libro>
  <libro id="2" genero="Ciencia Ficción">
    <titulo>Brave New World</titulo>
    <autor pais="Reino Unido">Aldous Huxley</autor>
    <precio moneda="USD">14.99</precio>
  </libro>
  <libro id="3" genero="Distopía">
    <titulo>Fahrenheit 451</titulo>
    <autor pais="EE.UU.">Ray Bradbury</autor>
    <precio moneda="USD">12.50</precio>
  </libro>
  <libro id="4" genero="Ficción">
    <titulo>To Kill a Mockingbird</titulo>
    <autor pais="EE.UU.">Harper Lee</autor>
    <precio moneda="USD">18.99</precio>
  </libro>
  <libro id="5" genero="Ficción">
    <titulo>The Great Gatsby</titulo>
    <autor pais="EE.UU.">F. Scott Fitzgerald</autor>
    <precio moneda="USD">10.99</precio>
  </libro>
</biblioteca>
```


Pregunta 1. Devuelve todos los títulos de los libros.
```xquery
for $libro in //libro
return $libro/titulo/text()
```

Pregunta 2. Devuelve los títulos de libros cuyo precio es mayor a 15.
```xquery
for $libro in //libro[precio > 15]
return $libro/titulo/text()
```

Pregunta 3. Lista los autores y sus países de origen.
```xquery
for $libro in //libro
return concat($libro/autor/text(), ' - ', $libro/autor/@pais)
```

Pregunta 4. Calcula el precio promedio de los libros.
```xquery
let $precios := //libro/precio
return avg($precios)
```

Pregunta 5. Devuelve los títulos ordenados alfabéticamente.
```xquery
for $titulo in //libro/titulo
order by $titulo
return $titulo/text()
```

Pregunta 6. Devuelve los títulos y precios de los libros en formato XML.
```xquery
for $libro in //libro
return <libro><titulo>{$libro/titulo/text()}</titulo><precio>{$libro/precio/text()}</precio></libro>
```

Pregunta 7. Encuentra libros del género "Ficción".
```xquery
for $libro in //libro[@genero='Ficción']
return $libro/titulo/text()
```

Pregunta 8. Devuelve los libros cuyo autor sea de "EE.UU.".
```xquery
for $libro in //libro[autor/@pais='EE.UU.']
return $libro/titulo/text()
```

Pregunta 9. Lista los libros y su precio total (precio + 5 USD de impuesto).
```xquery
for $libro in //libro
return concat($libro/titulo/text(), ' - ', $libro/precio/text() + 5)
```

Pregunta 10. Devuelve el libro más caro en el catálogo.
```xquery
let $maxPrecio := max(//libro/precio)
for $libro in //libro[precio = $maxPrecio]
return $libro/titulo/text()
```