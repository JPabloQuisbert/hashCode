# hashCode


Para abrir un archivo, procesar su contenido y estar seguros de cerrarlo empleamos  "with"

with open("file") as f:
    data = f.read()
    some code...