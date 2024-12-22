## Requisitos:
pip install cryptography

## Descripcion:
codigo simple para encriptar y desencriptar datos que hayan sido creados con este script.

Cuando se ejecuta por primera vez, este script genera una llave para desencriptar. Y si guardas la instancia en un archivo binario u otro, entosces estaras usando la misma llave para desencriptar.

## Llaves:
Si generas una llave nueva e intentas desencriptar algun archivo que ya hayas encriptado con este script, pues te devolvera un mensaje de que no se pudo desencriptar por que la llave es diferente.

Pero no te precupes, dado que las llaves creadas se guardan en una lista en un archivo pickle y se encuentra ubicado en la carpeta temporal de tu sistema. En especifico "binaries/keys.pkl".

Puedes cargar las llaves usando el metodo .confirm(show = True) de la instancia creada, y luego cambiar el valor de la variable de la instancia .key = "llave" por otra de las llaves cargadas hasta que des con la indicada.

## Info:
Para mas detalles, en el script hay un ejemplo de uso.

## Metodos:
Para crear los binarios:  
.generate_bn()

Parar cargar los binarios:  
.load_bn()

Para cargar las llaves:  
.confirm()
