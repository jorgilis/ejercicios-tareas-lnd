# Ejercicio 4.
Generar un fichero HTML donde se resalten los productos con precio mayor a 500 en negrita `<b>`

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
<p><b>Laptop</b> - $1000</p>
<p>Mouse - $25</p>
```

Ejercicio:

```xml
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
    <xsl:output method="html" indent="yes"/>
    <xsl:template match="/">
        <html>
            <body>
                <xsl:for-each select="products/product">
                <xsl:choose>
                    <xsl:when test="price > 500">
                        <p>
                            <b><xsl:value-of select="name"/></b> - $<xsl:value-of select="price"/>
                        </p>
                    </xsl:when>
                    <xsl:otherwise>
                        <p><xsl:value-of select="name"/> - $<xsl:value-of select="price"/></p>
                    </xsl:otherwise>
                </xsl:choose>
                </xsl:for-each>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
```
