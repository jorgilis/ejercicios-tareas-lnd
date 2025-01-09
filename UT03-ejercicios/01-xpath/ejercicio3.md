# Ejercicio 3. Biblioteca Digital.
```
<library>
  <book id="301">
    <title>The Catcher in the Rye</title>
    <author>J.D. Salinger</author>
    <genre>Fiction</genre>
    <available>true</available>
  </book>
  <book id="302">
    <title>To Kill a Mockingbird</title>
    <author>Harper Lee</author>
    <genre>Fiction</genre>
    <available>false</available>
  </book>
  <book id="303">
    <title>The Great Gatsby</title>
    <author>F. Scott Fitzgerald</author>
    <genre>Fiction</genre>
    <available>true</available>
  </book>
  <book id="304">
    <title>1984</title>
    <author>George Orwell</author>
    <genre>Dystopian</genre>
    <available>true</available>
  </book>
  <book id="305">
    <title>Moby Dick</title>
    <author>Herman Melville</author>
    <genre>Adventure</genre>
    <available>false</available>
  </book>
</library>
```

Pregunta 1. Selecciona todos los títulos de los libros:
```xpath
//title/text()
```

Pregunta 2. Selecciona todos los libros disponibles (con available="true"):
```xpath
//book[available='true']/title/text()
```

Pregunta 3. Selecciona el autor del libro "1984":
```xpath
//book[title='1984']/author/text()
```

Pregunta 4. Selecciona todos los géneros de libros únicos:
```xpath
distinct-values(//genre/text())
```

Pregunta 5. Cuenta cuántos libros están disponibles:
```xpath
count(//book[available='true'])
```

Pregunta 6. Selecciona los títulos de los libros que no están disponibles:
```xpath
//book[available='false']/title/text()
```

Pregunta 7. Selecciona los autores cuyos libros están disponibles:
```xpath
//book[available='true']/author/text()
```

Pregunta 8. Selecciona el ID del libro "The Great Gatsby":
```xpath
//book[title='The Great Gatsby']/@id
```

Pregunta 9. Selecciona todos los libros del género "Fiction":
```xpath
//book[genre='Fiction']/title/text()
```

Pregunta 10. Selecciona los títulos de los libros cuyo autor es "Herman Melville":
```xpath
//book[author='Herman Melville']/title/text()