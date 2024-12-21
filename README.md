## Descripcion:
codigo simple para encriptar y desencriptar datos que hayan sido creados con este script.

Cuando se ejecuta por primera vez, este script genera una llave para desencriptar. Y si guardas la instancia en un archivo binario u otro, entosces estaras usando la misma llave para desencriptar.

## Llaves:
Si generas una llave nueva e intentas desencriptar algun archivo que ya hayas encriptado con este script, pues te devolvera un mensaje de que no se pudo desencriptar por que la llave es diferente.

Pero no te precupes, dado que las llaves creadas se guardan en una lista en un archivo pickle llamado "keys.pkl", y se encuentra en la carpeta temporal de tu sistema.

Puedes cargar las llaves usando el metodo confirm(show = True)