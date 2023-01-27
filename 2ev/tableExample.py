from reportlab.platypus import (SimpleDocTemplate,
                                PageBreak,
                                Image,
                                Spacer,
                                Paragraph,
                                Table,
                                TableStyle)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

doc = SimpleDocTemplate("tableExample.pdf", pageSize = 4)
op = []

datos = [('', 'Ventas','Compras'),
         ('Xaneiro',300,500),
         ('Febreiro',2354,6798),
         ('Marzo',2354,67980),
         ('Abril',4577,2355),
         ('Maio',2346,47568)]
table = Table(datos, colWidths=100, rowHeights=30)
table.setStyle([])
op.append(table)

doc.build(op)
