# Ejercicio 3.
Crear un fichero HTML con un encabezado en cada sección. Generar encabezados `<h2>` y párrafos `<p>` para cada sección.

Entrada:

```xml
<sections>
  <section>
    <title>Introduction</title>
    <content>Welcome to the tutorial.</content>
  </section>
  <section>
    <title>Chapter 1</title>
    <content>This is the first chapter.</content>
  </section>
</sections>
```

Salida:

```xml
<h2>Introduction</h2>
<p>Welcome to the tutorial.</p>
<h2>Chapter 1</h2>
<p>This is the first chapter.</p>
```

Ejercicio:

```xml
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
    <html>
      <body>
        <xsl:for-each select="sections/section">
          <h2>
            <xsl:value-of select="title" />
          </h2>
          <p>
            <xsl:value-of select="content" />
          </p>
        </xsl:for-each>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
```
