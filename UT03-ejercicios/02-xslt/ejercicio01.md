# Ejercicio 1.
Generar mediante XSLT una lista HTML desordenada `<ul>` con los nombres de las frutas. a partir del siguiente HTML.




Entrada:

```xml
<fruits>
  <fruit>Apple</fruit>
  <fruit>Banana</fruit>
  <fruit>Cherry</fruit>
</fruits>
```

Salida:

```xml
<ul>
  <li>Apple</li>
  <li>Banana</li>
  <li>Cherry</li>
</ul>
```

Ejercicio:

```xml
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:output method="html" indent="yes"/>
  <xsl:template match="/">
    <html>
        <body>
            <xsl:for-each select="fruits/fruit">
            <ul>
              <li><xsl:value-of select="."/></li>
            </ul>
            </xsl:for-each>
        </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
```