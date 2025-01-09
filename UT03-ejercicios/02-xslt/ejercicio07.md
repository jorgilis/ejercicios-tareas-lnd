# Ejercicio 7.
Crear un fichero JSON con los productos y sus respectivos precios.

Entrada:

```xml
<products>
  <product>
    <name>Laptop</name>
    <price>1000</price>
  </product>
  <product>
    <name>Mouse</name>
    <price>25</price>
  </product>
</products>
```

Salida:

```xml
[
  {
    "name": "Laptop",
    "price": 1000
  },
  {
    "name": "Mouse",
    "price": 25
  }
]
```

Ejercicio:

```xml
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
    <xsl:text>[</xsl:text>
    <xsl:for-each select="products/product">
      <xsl:text>{"name": "</xsl:text>
      <xsl:value-of select="name" />
      <xsl:text>", "price": </xsl:text>
      <xsl:value-of select="price" />
      <xsl:text>}</xsl:text>
      <xsl:if test="position() != last()">
        <xsl:text>, </xsl:text>
      </xsl:if>
    </xsl:for-each>
    <xsl:text>]</xsl:text>
  </xsl:template>
</xsl:stylesheet>
```