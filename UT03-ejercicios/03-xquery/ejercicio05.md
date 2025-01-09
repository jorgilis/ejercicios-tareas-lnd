# Ejercicio 5. 

Archivo `pedidos.xml`:

```xml
<pedidos>
  <pedido id="1" cliente="Juan">
    <producto>Televisor</producto>
    <cantidad>1</cantidad>
    <precio>400</precio>
  </pedido>
  <pedido id="2" cliente="María">
    <producto>Teléfono</producto>
    <cantidad>2</cantidad>
    <precio>200</precio>
  </pedido>
  <pedido id="3" cliente="Pedro">
    <producto>Ratón</producto>
    <cantidad>5</cantidad>
    <precio>25</precio>
  </pedido>
  <pedido id="4" cliente="Ana">
    <producto>Teclado</producto>
    <cantidad>3</cantidad>
    <precio>30</precio>
  </pedido>
</pedidos>
```

Ejercicio 1. Devuelve los nombres de los clientes.
```xquery
for $pedido in doc("pedidos.xml")/pedidos/pedido
return $pedido/@cliente
```

Ejercicio 2. Devuelve los productos con precio total (cantidad × precio).
```xquery
for $pedido in doc("pedidos.xml")/pedidos/pedido
let $total := $pedido/cantidad * $pedido/precio
return <pedido>
	<nombre>{$pedido/producto}</nombre>
    <total>{$total}</total>
</pedido>
```

Ejercicio 3. Filtra los pedidos cuyo precio total sea mayor a 100.
```xquery
for $pedido in doc("pedidos.xml")/pedidos/pedido
let $total := $pedido/cantidad * $pedido/precio
where $total > 100
return $pedido
```

Ejercicio 4. Calcula el precio promedio de todos los pedidos.
```xquery
let $precios := doc("pedidos.xml")/pedidos/pedido/precio
return avg($precios)
```

Ejercicio 5. Devuelve el pedido más caro.
```xquery
for $pedido in doc("pedidos.xml")/pedidos/pedido
where $pedido/precio = max(//precio)
return $pedido
```

Ejercicio 6. Ordena los pedidos por cliente alfabéticamente.
```xquery
for $pedido in doc("pedidos.xml")/pedidos/pedido
order by $pedido/@cliente ascending
return $pedido
```

Ejercicio 7. Calcula el precio total de todos los pedidos.
```xquery
let $precios := doc("pedidos.xml")/pedidos/pedido/precio
return sum($precios)
```

Ejercicio 8. Devuelve los nombres de los clientes que compraron más de 3 unidades.
```xquery
for $pedido in doc("pedidos.xml")/pedidos/pedido
where $pedido/cantidad > 3
return $pedido/@cliente
```

Ejercicio 9. Devuelve los productos y sus precios con un descuento del 15% (usa `let`).
```xquery
for $pedido in doc("pedidos.xml")/pedidos/pedido
let $descuento := $pedido/precio * 0.85
return <pedido>
    <producto>{$pedido/producto}</producto>
    <descuento>{$descuento}</descuento>
</pedido>
```

Ejercicio 10. Cuenta el número total de pedidos.
```xquery
let $pedido := doc("pedidos.xml")/pedidos/pedido
return count($pedidos)
```