# Ejercicio 2. 

Archivo `tienda.xml`:

```xml
<tienda>
  <producto id="1" categoria="Computadoras">
    <nombre>Portátil</nombre>
    <marca>HP</marca>
    <precio moneda="USD">800</precio>
  </producto>
  <producto id="2" categoria="Accesorios">
    <nombre>Monitor</nombre>
    <marca>Dell</marca>
    <precio moneda="USD">200</precio>
  </producto>
  <producto id="3" categoria="Accesorios">
    <nombre>Ratón</nombre>
    <marca>Logitech</marca>
    <precio moneda="USD">25</precio>
  </producto>
  <producto id="4" categoria="Computadoras">
    <nombre>Escritorio</nombre>
    <marca>Lenovo</marca>
    <precio moneda="USD">600</precio>
  </producto>
  <producto id="5" categoria="Impresoras">
    <nombre>Impresora</nombre>
    <marca>Canon</marca>
    <precio moneda="USD">150</precio>
  </producto>
</tienda>
```

Pregunta 1. Devuelve los nombres de todos los productos.
```xquery
for $producto in doc("tienda.xml")/tienda/producto
return $producto/nombre
```

Pregunta 2. Devuelve los productos de la categoría "Accesorios".
```xquery
for $producto in doc("tienda.xml")/tienda/producto
where $producto/@categoria = "Accesorios"
return $producto
```

Pregunta 3. Calcula el precio total de todos los productos.
```xquery
let $precios := doc("tienda.xml")/tienda/producto/precio
return sum($precios)
```

Pregunta 4. Encuentra productos con un precio mayor a 500 USD.
```xquery
for $producto in doc("tienda.xml")/tienda/producto
where $producto/precio > 500
return $producto
```

Pregunta 5. Devuelve los productos y sus precios con un descuento del 10%.
```xquery
for $producto in doc("tienda.xml")/tienda/producto
let $descuento := $producto/precio * 0.9
return <producto>
	<nombre>{$producto/nombre}</nombre>
	<descuento>{$descuento}</descuento>
</producto>
```

Pregunta 6. Lista los productos ordenados por precio de menor a mayor.
```xquery
for $producto in doc("tienda.xml")/tienda/producto
order by $producto/precio ascending
return $producto
```

Pregunta 7. Devuelve los productos de la marca "HP".
```xquery
for $producto in doc("tienda.xml")/tienda/producto
where $producto/marca = "HP"
return $producto
```

Pregunta 8. Devuelve los nombres y categorías de los productos como elementos `<item>`.
```xquery
for $producto in doc("tienda.xml")/tienda/producto
return <item>
    <nombre>{$producto/nombre}</nombre>
    <categoria>{$producto/@categoria}</categoria>
</item>
```

Pregunta 9. Encuentra el producto más barato.
```xquery
for $producto in doc("tienda.xml")/tienda/producto
where $producto/precio = min(//precio)
return $producto
```

Pregunta 10. Calcula el precio promedio de los productos en la categoría "Computadoras".
```xquery
let $producto := doc("tienda.xml")/tienda/producto[@categoria="Computadoras"]
let $promedio := $producto/precio
return avg($promedio)
```