# Ejercicio 9.
Crear un fichero JSON con las categorías y los productos:

Entrada:

```xml
<store>
  <category name="Electronics">
    <product>
      <name>Laptop</name>
      <price>1000</price>
    </product>
    <product>
      <name>Smartphone</name>
      <price>700</price>
    </product>
  </category>
  <category name="Books">
    <product>
      <name>1984</name>
      <price>15.99</price>
    </product>
    <product>
      <name>Brave New World</name>
      <price>12.49</price>
    </product>
  </category>
</store>
```

Salida:

```xml
{
  "Electronics": [
    {
      "name": "Laptop",
      "price": 1000
    },
    {
      "name": "Smartphone",
      "price": 700
    }
  ],
  "Books": [
    {
      "name": "1984",
      "price": 15.99
    },
    {
      "name": "Brave New World",
      "price": 12.49
    }
  ]
}
```

Ejercicio:

```xml
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
    <xsl:text>{</xsl:text>
    <xsl:for-each select="store/category">
      <xsl:text>"</xsl:text>
      <xsl:value-of select="@name" />
      <xsl:text>": [</xsl:text>
      <xsl:for-each select="product">
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
      <xsl:if test="position() != last()">
        <xsl:text>, </xsl:text>
      </xsl:if>
    </xsl:for-each>
    <xsl:text>}</xsl:text>
  </xsl:template>
</xsl:stylesheet>
```