# Ejercicio 5. Inventario de Productos
```
<inventory>
  <product id="P001">
    <name>Chair</name>
    <category>Furniture</category>
    <price currency="USD">49.99</price>
    <stock>200</stock>
  </product>
  <product id="P002">
    <name>Table</name>
    <category>Furniture</category>
    <price currency="USD">129.99</price>
    <stock>50</stock>
  </product>
  <product id="P003">
    <name>Lamp</name>
    <category>Lighting</category>
    <price currency="USD">19.99</price>
    <stock>100</stock>
  </product>
  <product id="P004">
    <name>Desk</name>
    <category>Furniture</category>
    <price currency="USD">249.99</price>
    <stock>20</stock>
  </product>
  <product id="P005">
    <name>Ceiling Light</name>
    <category>Lighting</category>
    <price currency="USD">79.99</price>
    <stock>30</stock>
  </product>
</inventory>
```

Pregunta 1. Selecciona los nombres de todos los productos.
```xpath
//name/text()
```

Pregunta 2. Selecciona todos los productos de la categoría "Furniture".
```xpath
//product[category='Furniture']/name/text()
```

Pregunta 3. Selecciona el precio del producto "Lamp".
```xpath
//product[name='Lamp']/price/text()
```

Pregunta 4. Cuenta cuántos productos tienen más de 50 en stock.
```xpath
count(//product[stock>50])
```

Pregunta 5. Selecciona el producto más caro.
```xpath
//product[price=max(//price)]/name/text()
```

Pregunta 6. Selecciona los nombres de los productos con menos de 30 en stock.
```xpath
//product[stock<30]/name/text()
```

Pregunta 7. Selecciona todos los precios en USD.
```xpath
//price[@currency='USD']/text()
```

Pregunta 8. Selecciona el ID de todos los productos de la categoría "Lighting".
```xpath
//product[category='Lighting']/@id
```

Pregunta 9. Selecciona el precio del producto más barato.
```xpath
//product[price=min(//price)]/price/text()
```

Pregunta 10. Selecciona los nombres y precios de todos los productos ordenados por precio.
```xpath
//name/text() | //price/text()
```