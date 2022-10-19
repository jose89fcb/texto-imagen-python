from PIL import Image, ImageDraw, ImageFont
image = Image.open("Archivo.jpg") #Nombre de la imagen
draw = ImageDraw.Draw(image)

fuente = ImageFont.truetype("Fuente/AQUÍ EL NOMBRE DE LA FUENTE", 60) #Crea una carpeta llamada Fuente y dentro añades las fuente puedes descargar las fuentes en => https://www.dafont.com/es/
draw.text((50, 50), "JOSE89FCB", font=fuente, fill="white") #Añade un texto reemplaza "Jose89fcb" por el que quieras / 50,50 es la posicion del texto
image.save("Archivo1.jpg")