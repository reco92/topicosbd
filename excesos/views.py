from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from excesos.models import Aniototal,Aniodepartamento, Factexcesovelocidad,Jerarquia,Grafico
from django.db import connection
from django.http import HttpResponse
from excesos.forms import JerarquiaForm



inicializador = True


def indice_principal(request):
	
	if request.method == 'POST':
		
		import numpy as np
		import matplotlib.pyplot as plt

		print 'realizando cambios'
		
		cursor = connection.cursor()
		consulta = 'select A.JeraNombreTabla,B.DimNombreTabla,B.DimNombreColumna,B.DimNombrePK from Jerarquia A INNER JOIN Dimension B ON A.DimID = B.DimID where A.JeraID = ' + str(request.POST['jerarquia'])
		cursor.execute(consulta)
		parametros = cursor.fetchone()
		consulta = 'SELECT B.' + parametros[0] + ',count(*) FROM FactExcesoVelocidad A INNER JOIN ' + parametros[1] + ' B ON A.' + parametros[2] + '= B.'+ parametros[3] + ' GROUP by B.' + parametros[0]
		print consulta

		cursor.execute(consulta)

		print 'hice la consulta'
		valores = cursor.fetchall()
		cursor.close()
		#---
		#cursor = connection.cursor()

		#agrupado = 'B.Year'
		#consulta = 'SELECT B.Year_Name,count(*) FROM FactExcesoVelocidad A INNER JOIN DimTime B ON A.MEC_FECCOMUNDW = B.PK_Date GROUP by B.Year,B.Year_Name'

		#cursor.execute(consulta)#,agrupado,agrupado])
		#cursor.execute('SELECT %s_Name,count(*) FROM FactExcesoVelocidad A INNER JOIN DimTime B ON A.MEC_FECCOMUNDW = B.PK_Date GROUP by B.Year,B.Year_Name',[agrupado])#,agrupado,agrupado])
		#valores = cursor.fetchall()

		#if inicializador == True :
		#	inicializador = False
		#	fig = plt.figure()
		plt.clf()
		vecx = []
		vecy = []
		for i in valores:
			print i

		for i in valores:
			vecx.append(i[0])
			vecy.append(i[1])
		print '1111111'

			#print i.total

		fig = plt.figure()
		print '221231231'
		posx = []
		cont = 1
		while cont <= len(vecy):
			print cont
			posx.append(cont*  100)
			cont+=1

		print '2222222'
		
		plt.plot(posx,vecy,'r')
		print '3333333'
		plt.ylabel('excesos')
		plt.legend()
		plt.xticks(posx,vecx,size='small',color='r',rotation=15,fontsize = 10)
		plt.axis([-1, max(posx) + 100, 0, (max(vecy)*1.1)])
		
		#ax.xaxis.set_label_coords(1.05, -0.025)
		#plt.show()
		fig.set_size_inches(12.5,8.5)

		#nuevoGraf = Grafico(grafnombre ='Excesos',graftipo = 'Lineas',grafsql=consulta,cuboid=1)
		#nuevoGraf.save()
		
		
		fig.savefig('excesos/static/imagenes/graf.png')
		
		fig.clear()
		plt.close(fig)
		

		#print dictJerarquias
		form = JerarquiaForm()
		#imagen = 'excesos/static/imagenes/graf.png'
		contexto = {'formulario':form}
		print 'finalizando cambios'
		
		return render_to_response('index.html',contexto,context_instance =RequestContext(request))
	else:
		#fig = plt.figure()
		form = JerarquiaForm()
		contexto = {'formulario':form}
		return render_to_response('index.html',contexto,context_instance =RequestContext(request))

    #return HttpResponse("Hello, world. You're at the poll index.")

def nuevo_grafico(request):
	cursor = connection.cursor()
	consulta = 'select A.JeraNombreTabla,B.DimNombreTabla,B.DimNombreColumna,B.DimNombrePK from Jerarquia A INNER JOIN Dimension B ON A.DimID = B.DimID where A.JeraID = ' + recibido
	cursor.execute(consulta)
	parametros = cursor.fetchone()
	consulta = 'SELECT B.' + parametros[0] + ',count(*) FROM FactExcesoVelocidad A INNER JOIN ' + parametros[1] + ' B ON A.' + parametros[2] + '= B.'+ parametros[3] + ' GROUP by B.' + parametros[0]

	cursor.execute(consulta)
	valores = cursor.fetchall()
	
	vecx = []
	vecy = []

	for i in valores:
		vecx[i].append(i[0])
		valores[i].append(i[0])
	fig = plt.figure()

