# Ejercicio 4. Catálogo de Música
```
<musicCatalog>
  <album id="101">
    <title>Thriller</title>
    <artist>Michael Jackson</artist>
    <genre>Pop</genre>
    <price currency="USD">15.99</price>
    <stock>50</stock>
  </album>
  <album id="102">
    <title>The Dark Side of the Moon</title>
    <artist>Pink Floyd</artist>
    <genre>Rock</genre>
    <price currency="USD">20.99</price>
    <stock>30</stock>
  </album>
  <album id="103">
    <title>Back in Black</title>
    <artist>AC/DC</artist>
    <genre>Rock</genre>
    <price currency="USD">18.50</price>
    <stock>25</stock>
  </album>
  <album id="104">
    <title>21</title>
    <artist>Adele</artist>
    <genre>Pop</genre>
    <price currency="USD">12.99</price>
    <stock>100</stock>
  </album>
  <album id="105">
    <title>Abbey Road</title>
    <artist>The Beatles</artist>
    <genre>Rock</genre>
    <price currency="USD">19.99</price>
    <stock>10</stock>
  </album>
</musicCatalog>
```

Pregunta 1. Selecciona todos los títulos de los álbumes:
```xpath
//title/text()
```

Pregunta 2. Selecciona los títulos de los álbumes del género "Rock":
```xpath
//album[genre='Rock']/title/text()
```

Pregunta 3. Selecciona el precio del álbum "21":
```xpath
//album[title='21']/price/text()
```

Pregunta 4. Cuenta cuántos álbumes tienen más de 20 en stock:
```xpath
count(//album[stock>20])
```

Pregunta 5. Selecciona los nombres de los artistas cuyos álbumes cuestan más de 18 USD:
```xpath
//album[price>18]/artist/text()
```

Pregunta 6. Selecciona el álbum más caro:
```xpath
//album[price=max(//price)]/title/text()
```

Pregunta 7. Selecciona el género del álbum "Thriller":
```xpath
//album[title='Thriller']/genre/text()
```

Pregunta 8. Selecciona el ID de todos los álbumes de la artista "Adele":
```xpath
//album[artist='Adele']/@id
```

Pregunta 9. Selecciona los álbumes con menos de 30 en stock:
```xpath
//album[stock<30]/title/text()
```

Pregunta 10. Selecciona todos los géneros únicos disponibles:
```xpath
distinct-values(//genre/text())
