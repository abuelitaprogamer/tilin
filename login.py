def iniciar_sesion():
    usuario="marcelo"
    contraseña="perdic"

    nombre_usuario=input("ingrese su nombre de usuario: ")
    contra=input("ingrese su contraseña: ") 

    if usuario == nombre_usuario and contraseña == contra:
      print("inicio de sesion exitoso puedes ingresar", nombre_usuario)
      return True 
    else:
       print("inicio de sesion fallida ingrese nuevamente")
       return False
if __name__ == "__main__":
   iniciar_sesion()