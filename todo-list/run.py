from todor import create_app

#Punto de entrada de la app -> el archivo solo se ejecuta si lo llamamos por su nombre directamente
if __name__ == '__main__':
    #Obtenemos app de flask con toda la configuracion desde todor/__init__.py
    app = create_app()
    app.run()