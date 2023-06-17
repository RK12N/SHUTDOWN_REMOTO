import subprocess

comado = "shutdown -i"
resultado = subprocess.run(comado,shell=True,capture_output=True,text=True)


if resultado.returncode == 0:
    print("El comando se ejecuto correctamente")
    salida = resultado.stdout
    print("Salidad")
    print(salida)

else:
    print("Ocurrio un error al ejecutar el comando")
    error = resultado.stderr
    print("Error")
    print(error)
