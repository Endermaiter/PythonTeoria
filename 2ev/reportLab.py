from reportlab.pdfgen import canvas

aux =  canvas.Canvas("reportLab.pdf")

aux.drawString(0, 0, "Posicion orixe(X, Y) = (0,0)")
aux.drawString(50, 100, "Posicion (X, Y) = (50,100)")
aux.drawString(150, 500, "Posicion (X, Y) = (100,500)")

aux.drawImage("/home/dam2a/Imágenes/Marta.jpg", 200,200,225,225)

aux.showPage()
aux.save()