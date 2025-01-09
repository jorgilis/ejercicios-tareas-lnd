# Ejercicio 10.
Crear un fichero JSON con los titulos de secciones y su contenido.

Entrada:

```xml
<document>
  <section>
    <title>Introduction</title>
    <content>Welcome to this tutorial.</content>
  </section>
  <section>
    <title>Chapter 1</title>
    <content>This is the first chapter.</content>
  </section>
</document>
```

Salida

```xml
[
  {
    "title": "Introduction",
    "content": "Welcome to this tutorial."
  },
  {
    "title": "Chapter 1",
    "content": "This is the first chapter."
  }
]
```

Ejercicio:

```xml
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
    <xsl:text>[</xsl:text>
    <xsl:for-each select="document/section">
      <xsl:text>{</xsl:text>
      <xsl:text>"title": "</xsl:text>
      <xsl:value-of select="title" />
      <xsl:text>", "content": "</xsl:text>
      <xsl:value-of select="content" />
      <xsl:text>"}</xsl:text>
      <xsl:if test="position() != last()">
        <xsl:text>, </xsl:text>
      </xsl:if>
    </xsl:for-each>
    <xsl:text>]</xsl:text>
  </xsl:template>
</xsl:stylesheet>

```