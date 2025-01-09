# Ejercicio 2. Tienda de Electrónica.
```
<electronics>
  <item id="201">
    <name>Smartphone</name>
    <brand>BrandX</brand>
    <price currency="USD">699.99</price>
    <stock>50</stock>
  </item>
  <item id="202">
    <name>Laptop</name>
    <brand>BrandY</brand>
    <price currency="USD">999.99</price>
    <stock>10</stock>
  </item>
  <item id="203">
    <name>Tablet</name>
    <brand>BrandX</brand>
    <price currency="USD">399.99</price>
    <stock>25</stock>
  </item>
  <item id="204">
    <name>Headphones</name>
    <brand>BrandZ</brand>
    <price currency="USD">199.99</price>
    <stock>100</stock>
  </item>
</electronics>
```

Pregunta 1. Selecciona todos los nombres de productos:
```xpath
//name/text()
```

Pregunta 2. Selecciona los productos de la marca "BrandX":
```xpath
//item[brand='BrandX']/name/text()
```

Pregunta 3. Selecciona el producto más barato:
```xpath
//item[price=min(//price)]/name/text()
```

Pregunta 4. Selecciona el producto más caro:
```xpath
//item[price=max(//price)]/name/text()
```

Pregunta 5. Selecciona los nombres y precios de productos con más de 30 unidades en stock:
```xpath
//item[stock>30]/name/text() | //item[stock>30]/price/text()
```

Pregunta 6. Selecciona el atributo currency de todos los precios:
```xpath
//price/@currency
```

Pregunta 7. Cuenta cuántos productos hay en stock con menos de 20 unidades:
```xpath
count(//item[stock<20])
```

Pregunta 8. Selecciona los nombres de todos los productos cuyo precio sea mayor a 500:
```xpath
//item[price>500]/name/text()
```

Pregunta 9. Selecciona los nombres de productos con el atributo id mayor a 202:
```xpath
//item[@id>202]/name/text()
```

Pregunta 10. Selecciona todos los nodos completos de productos con "BrandZ":
```xpath
//item[brand='BrandZ']