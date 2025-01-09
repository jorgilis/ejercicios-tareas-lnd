# Ejercicio 4. 

Archivo `estudiantes.xml`:

```xml
<estudiantes>
  <estudiante id="1" carrera="Ingeniería">
    <nombre>Juan</nombre>
    <edad>20</edad>
    <nota>8.5</nota>
  </estudiante>
  <estudiante id="2" carrera="Derecho">
    <nombre>María</nombre>
    <edad>22</edad>
    <nota>9.0</nota>
  </estudiante>
  <estudiante id="3" carrera="Medicina">
    <nombre>Pedro</nombre>
    <edad>19</edad>
    <nota>7.5</nota>
  </estudiante>
  <estudiante id="4" carrera="Ingeniería">
    <nombre>Ana</nombre>
    <edad>21</edad>
    <nota>8.8</nota>
  </estudiante>
</estudiantes>
```

Pregunta 1. Devuelve los nombres de los estudiantes.
```xquery
for $estudiante in doc("estudiantes.xml")/estudiantes/estudiante
return $estudiante/nombre
```

Pregunta 2. Filtra los estudiantes con una nota mayor a 8.
```xquery
for $estudiante in doc("estudiantes.xml")/estudiantes/estudiante
where $estudiante/nota > 8
return $estudiante
```

Pregunta 3. Devuelve los nombres y las carreras de los estudiantes.
```xquery
for $estudiante in doc("estudiantes.xml")/estudiantes/estudiante
return ($estudiante/nombre) | ($estudiante/@carrera)
```

Pregunta 4. Calcula la nota promedio de los estudiantes (usa let).
```xquery
let $notas := doc("estudiantes.xml")/estudiantes/estudiante/nota
return avg($notas)
```

Pregunta 5. Devuelve los estudiantes de la carrera "Ingeniería".
```xquery 
for $estudiante in doc("estudiantes.xml")/estudiantes/estudiante
where $estudiante/@carrera = "Ingeniería"
return $estudiante
```

Pregunta 6. Ordena a los estudiantes por edad.
```xquery
for $estudiante in doc("estudiantes.xml")/estudiantes/estudiante
order by $estudiante/edad 
return $estudiante
```

Pregunta 7. Devuelve el estudiante más joven.
```xquery
for $estudiante in doc("estudiantes.xml")/estudiantes/estudiante
where $estudiante/edad = min(//edad)
return $estudiante
```

Pregunta 8. Devuelve los nombres y las notas incrementadas en 0.5.
```xquery
for $estudiante in doc("estudiantes.xml")/estudiantes/estudiante
let $nota := $estudiante/nota + 0.5
return <estudiante>
    <nombre>{$estudiante/nombre}</nombre>
    <nota>{$nota}</nota>
</estudiante>
```

Pregunta 9. Devuelve los estudiantes cuya nota es mayor a 8 y pertenecen a Ingeniería.
```xquery
for $estudiante in doc("estudiantes.xml")/estudiantes/estudiante
where $estudiante/@carrera = "Ingeniería" and $estudiante/nota > 8
return $estudiante
```

Pregunta 10. Cuenta cuántos estudiantes hay en total.
```xquery
let $estudiantes := doc("estudiantes.xml")/estudiantes/estudiante
return count($estudiantes)
```