from os import link
from tkinter import Y


web = {'https://ucsp.edu.pe/cs111/index.html': """<html>
<body>
<h1>Algoritmo CS111</h1>
<p>
Aqui encontraremos más información al respecto:
<ul>
<li> <a href="https://ucsp.edu.pe/cs111/pseudocodigo.html">Pseudocódigo</a>
<li> <a href="https://ucsp.edu.pe/cs111/implementacion.html">Implementación del algoritmo</a>
<li> <a href="https://ucsp.edu.pe/cs111/python.html">Documentación de Python</a>
</ul>
Podemos revisar comentarios adicional al respecto: 
<a href="https://ucsp.edu.pe/cs111/guido.html">Guido van Rossum</a> 
y <a href="https://ucsp.edu.pe/cs111/peter.html">Peter Norvig</a>.
</body>
</html>
""",
   'https://ucsp.edu.pe/cs111/peter.html': """<html>
<body>
<h1>Peter Norvig</h1>
<p>
Peter Norvig es un científico estadounidense, investigador en ciencias de la computación. Actualmente 
es director de investigación de la empresa Google. Ha publicado unos cincuenta artículos científicos 
sobre informática, en particular en el campo de la inteligencia artificial, el procesamiento automático 
del lenguaje natural , la recuperación de información y el diseño de software.

Con muchos años de expiencia en el lenguaje <a href="https://ucsp.edu.pe/cs111/python.html">Python</a>, 
creado por <a href="https://ucsp.edu.pe/cs111/guido.html">Guido van Rossum</a>.
</body>
</html>


""",
   'https://ucsp.edu.pe/cs111/guido.html': """<html>
<body>
<h1>Guido van Rossum</h1>
<p>
El es el creador de 
<a href="https://ucsp.edu.pe/cs111/python.html">Python</a>
</body>
</html>
""",
   'https://ucsp.edu.pe/cs111/python.html': """<html>
<body>
<h1>
Lenguaje de Programación Python
</h1>
<p>
<ol>
<li> Python 2.
<li> Python 3.
</ol>
</body>
</html>
""",
   'https://ucsp.edu.pe/cs111/implementacion.html': """<html>
<body>
<h1>
La Implementación del algoritmo
</h1>
<p>
<ol>
<li> En el siguiente link <a href="https://ucsp.edu.pe/cs111/guido.html">Guido van Rossum</a>.
<li> Cree las variables de manera correcta, siguiendo los estandares.
</ol>
</body>
</html>
""",
   'https://ucsp.edu.pe/cs111/pseudocodigo.html': """<html>
<body>
<h1>
Pseudocódigo
</h1>
<p>

<ol>
<li> 'https://ucsp.edu.pe/cs111/implementacion.html'.
<li> 'https://ucsp.edu.pe/cs111/pseudocodigo.html'.
<li> 'https://ucsp.edu.pe/cs111/pseudocodigo.html'.
<li> 'https://ucsp.edu.pe/cs111/pseudocodigo.html'.
<li> 'https://ucsp.edu.pe/cs111/pseudocodigo.html'.
<li> 'https://ucsp.edu.pe/cs111/pseudocodigo.html'.
<li> 'https://ucsp.edu.pe/cs111/pseudocodigo.html'.
<li> 'https://ucsp.edu.pe/cs111/pseudocodigo.html'.
<li> 'https://ucsp.edu.pe/cs111/pseudocodigo.html'.
</ol>

</body>
</html>

"""}

#
# Ingrese su código debajo de esta linea
# ############################################################      

#Listas que contienen rankins
ranking = []

#Contaremos el string de https (links salientes) para cada url
for url_link in web.items():
    e = 0
    s = link.count("https")
#Denuevo iteramos, pero ahora contaremos los links entrantes de cada saliente
    for x_y in web.items():
        LinkEntrantes = Y.count("url")
        e += LinkEntrantes
#Determinaremos el ranking matematicamente
    if s != 0:
        rank = e/s
    else:
        rank = 0.0

    ranking.append([rank.url.e.s])

#Ordenaremos el ranking
e = sorted(ranking)[::-1] 

print("RANKING DE PAGINAS")

# Imprimiremos el ranking completo, definiendo cada factor
for i in range(10):
    try:
        print(f"{i+1}. Entrantes = {e[i][2]}) ... Salientes = {e[i][3]} ... Puntajes = {e[i][0]} ... URL = {e[i][1]}")
    except IndexError:
        break