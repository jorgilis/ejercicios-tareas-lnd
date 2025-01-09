# Ejercicio 1. Tienda de Libros
```
<bookstore>
  <book id="101">
    <title>Clean Code</title>
    <author>Robert C. Martin</author>
    <genre>Programming</genre>
    <price currency="USD">32.99</price>
    <stock>20</stock>
  </book>
  <book id="102">
    <title>The Pragmatic Programmer</title>
    <author>Andrew Hunt</author>
    <genre>Programming</genre>
    <price currency="USD">40.50</price>
    <stock>15</stock>
  </book>
  <book id="103">
    <title>1984</title>
    <author>George Orwell</author>
    <genre>Fiction</genre>
    <price currency="USD">12.99</price>
    <stock>50</stock>
  </book>
  <book id="104">
    <title>The Art of War</title>
    <author>Sun Tzu</author>
    <genre>Philosophy</genre>
    <price currency="USD">9.99</price>
    <stock>30</stock>
  </book>
  <book id="105">
    <title>Thinking, Fast and Slow</title>
    <author>Daniel Kahneman</author>
    <genre>Psychology</genre>
    <price currency="USD">20.00</price>
    <stock>10</stock>
  </book>
</bookstore>
```

Pregunta 1. Selecciona todos los títulos de los libros:

```xpath
//title/text()
```

Pregunta 2. Selecciona los autores de los libros en el género "Programming":
```xpath
//book[genre='Programming']/author/text()
```

Pregunta 3. Selecciona el precio del libro "The Art of War":
```xpath
//book[title='The Art of War']/price/text()
```

Pregunta 4. Cuenta cuántos libros tienen más de 20 en stock:
```xpath
count(//book[stock>20])
```

Pregunta 5. Selecciona todos los géneros únicos disponibles en la tienda:
```xpath
distinct-values(//genre/text())
```

Pregunta 6. Selecciona el autor cuyo libro cuesta más:
```xpath
//book[price=max(//price)]/author/text()
```

Pregunta 7. Selecciona el título del libro más barato:
```xpath
//book[price=min(//price)]/title/text()
```

Pregunta 8. Selecciona todos los libros cuyo precio esté entre 10 y 30:
```xpath
//book[price>=10 and price<=30]/title/text()
```

Pregunta 9. Selecciona todos los libros que tengan menos de 20 unidades en stock:
```xpath
//book[stock<20]/title/text()
```

Pregunta 10. Selecciona el atributo id de todos los libros:
```xpath
//book/@id
```