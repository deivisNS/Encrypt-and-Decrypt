import pickle, os, tempfile
from cryptography.fernet import Fernet



class Crypt():

    # se crea la llave para desencriptar
    def __init__(self):
        
        self.key = Fernet.generate_key()

    
    # genera el archivo encriptado ( name > 'nombre con el que se guardara', data > 'datos a encriptar' )
    def generater_bn(self, name, data):

        try:

            cipher = Fernet(self.key)

            self.confirm(key = self.key)

            encrypt_data = cipher.encrypt(pickle.dumps(data))

            with open(f"./{name}.pkl", "wb") as file:

                file.write(encrypt_data)

            return "Binario Generado."
        
        except:

            return "Error al generar"
    

    # carga el archivo y lo desencripta ( name > 'nombre del archivo a desencriptar' )
    def load_bn(self, name):

        try:
                
            cipher = Fernet(self.key)

            with open(f"./{name}.pkl", "rb") as file:
                
                encrypt = file.read()

                decrypt = cipher.decrypt(encrypt)

                data = pickle.loads(decrypt)

            return data
        
        except:

            return "No se logro extraer la informacion, intente cambiar la clave."


    # proceso donde se guardan las llaves generadas
    # ( key > 'llave a guardar' )
    # ( show > 'si quieres cargar todas las llaves guardadas' )
    def confirm(self, key = None, show = False):

        if os.path.exists(f"{tempfile.gettempdir()}/binaries") == False:

            os.mkdir(f"{tempfile.gettempdir()}/binaries")

        if os.path.exists(f"{tempfile.gettempdir()}/binaries/keys.pkl") == False and show == False and key != None:

            with open(f"{tempfile.gettempdir()}/binaries/keys.pkl", "wb") as file:

                pickle.dump([key], file)

        else:

            try:
                    
                with open(f"{tempfile.gettempdir()}/binaries/keys.pkl", "rb") as file:

                    keys = pickle.load(file)

                if show == True:

                    return keys
                
                else:

                    if not key in keys and key != None:

                        keys.append(key)

                        with open(f"{tempfile.gettempdir()}/binaries/keys.pkl", "wb") as file:
                            
                            pickle.dump(keys, file)

                    else:

                        return "Es necesario una llave."

            except:

                return "El directorio o archivo, no se encuentran."

    

if __name__ == "__main__":

    # instancia
    crypt = Crypt()

    # generar el encriptado (se devolvera un mensaje)
    print(crypt.generater_bn("nadar", "hay que nadar."))

    # desencriptar un archivo creado (se devolvera un mensaje)
    print(crypt.load_bn("nadar"))


# si necesitas cargar las llaves creadas
"""
keys = crypt.confirm(show = True)

print(keys)

crypt.key = keys[0]
"""