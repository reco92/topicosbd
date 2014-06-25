from django import forms
from django.forms.fields import ChoiceField

class JerarquiaForm (forms.Form):

	data =( (1,'Matricula'),
			(2,'NombreCliente'),
			(3,	'Anio'),
			(4,	'Trimestre'),
			(5,	'Mes'),
			(7,	'Semana'),
			(8,	'DiaAnio'),
			(9,	'DiaTrimestre'),
			(10,'DiaMes'),
			(11	,'DiaSemana'),
			(12	,'SemanaAnio'),
			(13	,'MesAnio'),
			(14	,'MesTrimestre'),
			(15	,'TrimestreAnio'),
			(18	,'Departamento'),
			(19	,'Provincia'),
			(21	,'CapitalProvincia'),
			(22	,'Distrito'),
			(23	,'TipoVia'),
			(24	,'NombreVia'),
			(25	,'CuadraVia'),
			(26	,'PuntoReferencia'),
			(27	,'PuntoVia'),
			(28	,'Cerco'))

	jerarquia = forms.ChoiceField(choices=data,label='Jerarquia')

	#def __init__(self, custom_choices=None, *args, **kwargs):
    #	super(JerarquiaForm, self).__init__(*args, **kwargs)
    #	if custom_choices:
    #		self.fields['jerarquia'].choices = custom_choices
	

