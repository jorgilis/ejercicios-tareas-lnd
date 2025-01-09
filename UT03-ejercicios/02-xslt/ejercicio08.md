# Ejercicio 8.
Crear un Objeto JSON con los nombres de usuarios.

Entrada:

```xml
<users>
  <user>
    <id>1</id>
    <name>John Doe</name>
    <email>john@example.com</email>
  </user>
  <user>
    <id>2</id>
    <name>Jane Smith</name>
    <email>jane@example.com</email>
  </user>
</users>
```

Salida:

```xml
[
  {
    "id": "1",
    "name": "John Doe",
    "email": "john@example.com"
  },
  {
    "id": "2",
    "name": "Jane Smith",
    "email": "jane@example.com"
  }
]
```

Ejercicio:

```xml
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
    <xsl:text>[</xsl:text>
    <xsl:for-each select="users/user">
      <xsl:text>{"id": "</xsl:text>
      <xsl:value-of select="id" />
      <xsl:text>", "name": "</xsl:text>
      <xsl:value-of select="name" />
      <xsl:text>", "email": "</xsl:text>
      <xsl:value-of select="email" />
      <xsl:text>"}</xsl:text>
      <xsl:if test="position() != last()">
        <xsl:text>, </xsl:text>
      </xsl:if>
    </xsl:for-each>
    <xsl:text>]</xsl:text>
  </xsl:template>
</xsl:stylesheet>
```