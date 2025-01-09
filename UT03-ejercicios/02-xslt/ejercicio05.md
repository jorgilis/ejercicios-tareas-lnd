# Ejercicio 5.
Generar un fichero HTML con una lista de navegación `<nav>`.

Entrada:

```xml
<menu>
  <item>Home</item>
  <item>About</item>
  <item>Contact</item>
</menu>
```

Salida:

```xml
<nav>
  <ul>
    <li>Home</li>
    <li>About</li>
    <li>Contact</li>
  </ul>
</nav>
```

Ejercicio:

```xml
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:output method="html" indent="yes"/>
	<xsl:template match="/">
		<nav>
			<ul>
				<xsl:for-each select="menu/item">
					<li>
						<xsl:value-of select="."/>
					</li>
				</xsl:for-each>
			</ul>
		</nav>
	</xsl:template>
</xsl:stylesheet>
```