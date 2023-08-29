import login 
import cachipun

print("bienvenidos al juego de cachipun")

if login.iniciar_sesion():
        cachipun.cachipun()
else:
        print("vuelve a ingresar")