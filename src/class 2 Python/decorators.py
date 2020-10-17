def Anunciar(f):
    def wrapper():
        print("ejecutando la funcion")
        f()
        print("se termino la funcion")
    return wrapper

@Anunciar
def hello():
    print("Hello, World!")

hello()
