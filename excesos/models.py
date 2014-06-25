from __future__ import unicode_literals

from django.db import models

#-------------------- TABLAS METADADA ----------------------
class Cubo(models.Model):
    cuboid = models.AutoField(primary_key=True,db_column='CuboID') # Field name made lowercase.
    cubonombre = models.CharField(db_column='CuboNombre', max_length=60) # Field name made lowercase.
    cubonombretabla = models.CharField(db_column='CuboNombreTabla', max_length=60) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Cubo'

class Dimension(models.Model):
    dimid = models.AutoField(primary_key=True,db_column='DimID') # Field name made lowercase.
    dimnombre = models.CharField(db_column='DimNombre', max_length=60) # Field name made lowercase.
    dimnombretabla = models.CharField(db_column='DimNombreTabla', max_length=60) # Field name made lowercase.
    dimnombrecolumna = models.CharField(db_column='DimNombreColumna', max_length=60) # Field name made lowercase.
    dimnombrepk = models.CharField(db_column='DimNombrePK', max_length=60) # Field name made lowercase.
    cuboid = models.ForeignKey(Cubo, db_column='CuboID') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Dimension'

class Ejehorizontal(models.Model):
    ejhoid = models.AutoField(primary_key=True,db_column='EjHoID') # Field name made lowercase.
    jeraid = models.ForeignKey('Jerarquia', db_column='JeraID') # Field name made lowercase.
    grafid = models.ForeignKey('Grafico', db_column='GrafID') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'EjeHorizontal'

class Ejevertical(models.Model):
    ejveid = models.AutoField(primary_key=True,db_column='EjVeID') # Field name made lowercase.
    mediid = models.ForeignKey('Medida', db_column='MediID') # Field name made lowercase.
    grafid = models.ForeignKey('Grafico', db_column='GrafID') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'EjeVertical'

class Grafico(models.Model):
    grafid = models.AutoField(primary_key=True,db_column='GrafID') # Field name made lowercase.
    grafnombre = models.CharField(db_column='GrafNombre', max_length=60) # Field name made lowercase.
    graftipo = models.CharField(db_column='GrafTipo', max_length=60) # Field name made lowercase.
    grafsql = models.CharField(db_column='GrafSQL', max_length=200, blank=True) # Field name made lowercase.
    grafnombretabla = models.CharField(db_column='GrafNombreTabla', max_length=60, blank=True) # Field name made lowercase.
    grafnombreimagen = models.CharField(db_column='GrafNombreImagen', max_length=64, blank=True) # Field name made lowercase.
    cuboid = models.ForeignKey(Cubo, db_column='CuboID') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Grafico'

class Jerarquia(models.Model):
    jeraid = models.AutoField(primary_key=True,db_column='JeraID') # Field name made lowercase.
    jeranombre = models.CharField(db_column='JeraNombre', max_length=60) # Field name made lowercase.
    jeranombretabla = models.CharField(db_column='JeraNombreTabla', max_length=60) # Field name made lowercase.
    dimid = models.ForeignKey(Dimension, db_column='DimID') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Jerarquia'

class Medida(models.Model):
    mediid = models.AutoField(primary_key=True,db_column='MediID') # Field name made lowercase.
    medinombre = models.CharField(db_column='MediNombre', max_length=60) # Field name made lowercase.
    medinombretabla = models.CharField(db_column='MediNombreTabla', max_length=60) # Field name made lowercase.
    cuboid = models.ForeignKey(Cubo, db_column='CuboID') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Medida'

#------------------------------------------------

class Alemanacopy(models.Model):
    a_o = models.FloatField(db_column='A\xf1o', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    mes = models.FloatField(db_column='Mes', blank=True, null=True) # Field name made lowercase.
    local = models.CharField(db_column='LOCAL', max_length=255, blank=True) # Field name made lowercase.
    tipodoc = models.CharField(db_column='TipoDoc', max_length=255, blank=True) # Field name made lowercase.
    codigo = models.FloatField(db_column='Codigo', blank=True, null=True) # Field name made lowercase.
    producto = models.CharField(db_column='Producto', max_length=255, blank=True) # Field name made lowercase.
    cantidad = models.FloatField(db_column='Cantidad', blank=True, null=True) # Field name made lowercase.
    total = models.FloatField(db_column='Total', blank=True, null=True) # Field name made lowercase.
    indtotal = models.FloatField(db_column='IndTotal', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'AlemanaCOPY'

class Alemanadates(models.Model):
    fec = models.DateTimeField(db_column='FEC', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'AlemanaDates'

class AlemanaMicrostrategy(models.Model):
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True) # Field name made lowercase.
    tienda = models.CharField(db_column='Tienda', max_length=50, blank=True) # Field name made lowercase.
    tipodoc = models.CharField(db_column='TipoDoc', max_length=50, blank=True) # Field name made lowercase.
    producto = models.CharField(db_column='Producto', max_length=100, blank=True) # Field name made lowercase.
    cantidad = models.IntegerField(db_column='Cantidad', blank=True, null=True) # Field name made lowercase.
    total = models.FloatField(db_column='Total', blank=True, null=True) # Field name made lowercase.
    indtotal = models.FloatField(db_column='IndTotal', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Alemana_Microstrategy'

class Aniodepartamento(models.Model):
    anio = models.IntegerField(db_column='Anio') # Field name made lowercase.
    sdpto = models.CharField(db_column='sDpto', max_length=100, blank=True) # Field name made lowercase.
    total = models.IntegerField(db_column='Total') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'AnioDepartamento'
    def __unicode__(self):
        return str(self.anio) + ' ' + self.sdpto + ' ' + str(self.total)

class Aniodistrito(models.Model):
    anio = models.IntegerField(db_column='Anio') # Field name made lowercase.
    sdistr = models.CharField(db_column='sDistr', max_length=100, blank=True) # Field name made lowercase.
    total = models.IntegerField(db_column='Total') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'AnioDistrito'

class Anioprovincia(models.Model):
    anio = models.IntegerField(db_column='Anio') # Field name made lowercase.
    sprovi = models.CharField(db_column='sProvi', max_length=100, blank=True) # Field name made lowercase.
    total = models.IntegerField(db_column='Total') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'AnioProvincia'

class Aniototal(models.Model):
    anio = models.IntegerField(db_column='Anio') # Field name made lowercase.
    total = models.IntegerField(db_column='Total') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'AnioTotal'
    def __unicode__(self):
        return str(self.anio) + ' ' + str(self.total)

class Copia(models.Model):
    proyecto = models.CharField(db_column='Proyecto', max_length=255, blank=True) # Field name made lowercase.
    tipo_de_costo = models.CharField(db_column='Tipo de Costo', max_length=255, blank=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    centro_de_costo = models.CharField(db_column='Centro de Costo', max_length=255, blank=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    partida_de_costo = models.CharField(db_column='Partida de Costo', max_length=255, blank=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    tipo = models.CharField(db_column='Tipo', max_length=255, blank=True) # Field name made lowercase.
    costo = models.FloatField(db_column='Costo', blank=True, null=True) # Field name made lowercase.
    ds_mes = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'COPIA'

class Dimreferenciasdw(models.Model):
    idreferencia = models.AutoField(primary_key=True,db_column='idReferencia') # Field name made lowercase.
    sdpto = models.CharField(db_column='sDpto', max_length=110, blank=True) # Field name made lowercase.
    sprovi = models.CharField(db_column='sProvi', max_length=100, blank=True) # Field name made lowercase.
    scapprovi = models.CharField(db_column='sCapProvi', max_length=100, blank=True) # Field name made lowercase.
    sdistr = models.CharField(db_column='sDistr', max_length=100, blank=True) # Field name made lowercase.
    stipvia = models.CharField(db_column='sTipVia', max_length=2, blank=True) # Field name made lowercase.
    snomvia = models.CharField(db_column='sNomVia', max_length=100, blank=True) # Field name made lowercase.
    scuadvia = models.CharField(db_column='sCuadVia', max_length=10, blank=True) # Field name made lowercase.
    spoiref = models.CharField(db_column='sPoiRef', max_length=100, blank=True) # Field name made lowercase.
    spoivia = models.CharField(db_column='sPoiVia', max_length=100, blank=True) # Field name made lowercase.
    scerco = models.CharField(db_column='sCerco', max_length=100, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'DimReferenciasDW'

class Dimtime(models.Model):
    pk_date = models.DateField(db_column='PK_Date') # Field name made lowercase.
    date_name = models.CharField(db_column='Date_Name', max_length=50, blank=True) # Field name made lowercase.
    year = models.DateTimeField(db_column='Year', blank=True, null=True) # Field name made lowercase.
    year_name = models.CharField(db_column='Year_Name', max_length=50, blank=True) # Field name made lowercase.
    trimester = models.DateTimeField(db_column='Trimester', blank=True, null=True) # Field name made lowercase.
    trimester_name = models.CharField(db_column='Trimester_Name', max_length=50, blank=True) # Field name made lowercase.
    month = models.DateTimeField(db_column='Month', blank=True, null=True) # Field name made lowercase.
    month_name = models.CharField(db_column='Month_Name', max_length=50, blank=True) # Field name made lowercase.
    week = models.DateTimeField(db_column='Week', blank=True, null=True) # Field name made lowercase.
    week_name = models.CharField(db_column='Week_Name', max_length=50, blank=True) # Field name made lowercase.
    day_of_year = models.IntegerField(db_column='Day_Of_Year', blank=True, null=True) # Field name made lowercase.
    day_of_year_name = models.CharField(db_column='Day_Of_Year_Name', max_length=50, blank=True) # Field name made lowercase.
    day_of_trimester = models.IntegerField(db_column='Day_Of_Trimester', blank=True, null=True) # Field name made lowercase.
    day_of_trimester_name = models.CharField(db_column='Day_Of_Trimester_Name', max_length=50, blank=True) # Field name made lowercase.
    day_of_month = models.IntegerField(db_column='Day_Of_Month', blank=True, null=True) # Field name made lowercase.
    day_of_month_name = models.CharField(db_column='Day_Of_Month_Name', max_length=50, blank=True) # Field name made lowercase.
    day_of_week = models.IntegerField(db_column='Day_Of_Week', blank=True, null=True) # Field name made lowercase.
    day_of_week_name = models.CharField(db_column='Day_Of_Week_Name', max_length=50, blank=True) # Field name made lowercase.
    week_of_year = models.IntegerField(db_column='Week_Of_Year', blank=True, null=True) # Field name made lowercase.
    week_of_year_name = models.CharField(db_column='Week_Of_Year_Name', max_length=50, blank=True) # Field name made lowercase.
    month_of_year = models.IntegerField(db_column='Month_Of_Year', blank=True, null=True) # Field name made lowercase.
    month_of_year_name = models.CharField(db_column='Month_Of_Year_Name', max_length=50, blank=True) # Field name made lowercase.
    month_of_trimester = models.IntegerField(db_column='Month_Of_Trimester', blank=True, null=True) # Field name made lowercase.
    month_of_trimester_name = models.CharField(db_column='Month_Of_Trimester_Name', max_length=50, blank=True) # Field name made lowercase.
    trimester_of_year = models.IntegerField(db_column='Trimester_Of_Year', blank=True, null=True) # Field name made lowercase.
    trimester_of_year_name = models.CharField(db_column='Trimester_Of_Year_Name', max_length=50, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'DimTime'

class Dimunidadclientedw(models.Model):
    uni_codigo = models.IntegerField(db_column='UNI_CODIGO') # Field name made lowercase.
    uni_matricula = models.CharField(db_column='UNI_MATRICULA', max_length=9, blank=True) # Field name made lowercase.
    cli_nombre = models.CharField(db_column='CLI_NOMBRE', max_length=160, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'DimUnidadClienteDW'

class Factexcesovelocidad(models.Model):
    uni_codigodw = models.ForeignKey(Dimunidadclientedw, db_column='UNI_CODIGODW', blank=True, null=True) # Field name made lowercase.
    mec_feccomundw = models.DateField(db_column='MEC_FECCOMUNDW', blank=True, null=True) # Field name made lowercase.
    mec_velocidad = models.SmallIntegerField(db_column='MEC_VELOCIDAD', blank=True, null=True) # Field name made lowercase.
    idreferencia = models.ForeignKey(Dimreferenciasdw, db_column='idReferencia', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'FactExcesoVelocidad'

class OwMicrostrategy(models.Model):
    proyecto = models.CharField(db_column='Proyecto', max_length=255, blank=True) # Field name made lowercase.
    tipocosto = models.CharField(db_column='TipoCosto', max_length=255, blank=True) # Field name made lowercase.
    centrocosto = models.CharField(db_column='CentroCosto', max_length=255, blank=True) # Field name made lowercase.
    partidacosto = models.CharField(db_column='PartidaCosto', max_length=255, blank=True) # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=255, blank=True) # Field name made lowercase.
    costo = models.FloatField(db_column='Costo', blank=True, null=True) # Field name made lowercase.
    ds_mes = models.DateTimeField(blank=True, null=True)
    subfamilia = models.CharField(db_column='SubFamilia', max_length=100, blank=True) # Field name made lowercase.
    producto = models.CharField(db_column='Producto', max_length=100, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'OW_Microstrategy'

class OwProductos(models.Model):
    partidacosto = models.CharField(db_column='PartidaCosto', max_length=100, blank=True) # Field name made lowercase.
    subfamilia = models.CharField(db_column='SubFamilia', max_length=100, blank=True) # Field name made lowercase.
    producto = models.CharField(db_column='Producto', max_length=255, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'OW_Productos'

class Prod(models.Model):
    sub_familia = models.CharField(db_column='SUB FAMILIA', max_length=255, blank=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    cod_pro = models.FloatField(db_column='COD# PRO', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    producto = models.CharField(db_column='PRODUCTO', max_length=255, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Prod'

class View1(models.Model):
    sdpto = models.CharField(db_column='sDpto', max_length=110, blank=True) # Field name made lowercase.
    sprovi = models.CharField(db_column='sProvi', max_length=100, blank=True) # Field name made lowercase.
    uni_matricula = models.CharField(db_column='UNI_MATRICULA', max_length=9, blank=True) # Field name made lowercase.
    cli_nombre = models.CharField(db_column='CLI_NOMBRE', max_length=160, blank=True) # Field name made lowercase.
    month_name = models.CharField(db_column='Month_Name', max_length=50, blank=True) # Field name made lowercase.
    week_name = models.CharField(db_column='Week_Name', max_length=50, blank=True) # Field name made lowercase.
    trimester_name = models.CharField(db_column='Trimester_Name', max_length=50, blank=True) # Field name made lowercase.
    day_of_month_name = models.CharField(db_column='Day_Of_Month_Name', max_length=50, blank=True) # Field name made lowercase.
    mec_velocidad = models.SmallIntegerField(db_column='MEC_VELOCIDAD', blank=True, null=True) # Field name made lowercase.
    year_name = models.CharField(db_column='Year_Name', max_length=50, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'View_1'

class View3(models.Model):
    expr1 = models.SmallIntegerField(db_column='Expr1', blank=True, null=True) # Field name made lowercase.
    cli = models.CharField(max_length=160, blank=True)
    uni_matricula = models.CharField(db_column='UNI_MATRICULA', max_length=9, blank=True) # Field name made lowercase.
    month_name = models.CharField(db_column='Month_Name', max_length=50, blank=True) # Field name made lowercase.
    year_name = models.CharField(db_column='Year_Name', max_length=50, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'View_3'

class View5(models.Model):
    snomvia = models.CharField(db_column='sNomVia', max_length=100, blank=True) # Field name made lowercase.
    sdpto = models.CharField(db_column='sDpto', max_length=110, blank=True) # Field name made lowercase.
    expr1 = models.SmallIntegerField(db_column='Expr1', blank=True, null=True) # Field name made lowercase.
    month_name = models.CharField(db_column='Month_Name', max_length=50, blank=True) # Field name made lowercase.
    year_name = models.CharField(db_column='Year_Name', max_length=50, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'View_5'

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)
    class Meta:
        managed = False
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')
    class Meta:
        managed = False
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'auth_permission'

class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        managed = False
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    empresa = models.CharField(max_length=50, blank=True)
    unidad = models.CharField(max_length=50, blank=True)
    ds_cliente = models.CharField(max_length=10, blank=True)
    class Meta:
        managed = False
        db_table = 'cliente'

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    class Meta:
        managed = False
        db_table = 'django_admin_log'

class DjangoContentType(models.Model):
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'django_session'

class Hechos(models.Model):
    id_tiempo = models.IntegerField(blank=True, null=True)
    id_region = models.IntegerField(blank=True, null=True)
    id_cliente = models.IntegerField(blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'hechos'

class Region(models.Model):
    id_region = models.AutoField(primary_key=True)
    ciudad = models.CharField(db_column='Ciudad', max_length=50, blank=True) # Field name made lowercase.
    provincia = models.CharField(db_column='Provincia', max_length=50, blank=True) # Field name made lowercase.
    distrito = models.CharField(db_column='Distrito', max_length=50, blank=True) # Field name made lowercase.
    via = models.CharField(db_column='Via', max_length=50, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'region'

class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'sysdiagrams'

class Tiempo(models.Model):
    id_date = models.AutoField(primary_key=True)
    a_o = models.CharField(db_column='A\xf1o', max_length=50, blank=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    mes = models.CharField(db_column='Mes', max_length=50, blank=True) # Field name made lowercase.
    dia = models.CharField(db_column='Dia', max_length=50, blank=True) # Field name made lowercase.
    ds_tiempo = models.CharField(max_length=50, blank=True)
    class Meta:
        managed = False
        db_table = 'tiempo'

class TopicosPallin(models.Model):
    dni_pallin = models.AutoField(primary_key=True,db_column='DNI_pallin') # Field name made lowercase.
    nombre_pallin = models.CharField(max_length=25)
    domingo = models.CharField(max_length=25)
    monto_pallin = models.CharField(max_length=160)
    class Meta:
        managed = False
        db_table = 'topicos_pallin'

class TopicosPerson(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    class Meta:
        managed = False
        db_table = 'topicos_person'

class VstRefXUnidad(models.Model):
    idreferencia = models.IntegerField(db_column='idReferencia', blank=True, null=True) # Field name made lowercase.
    sdpto = models.CharField(db_column='sDpto', max_length=110, blank=True) # Field name made lowercase.
    sprovi = models.CharField(db_column='sProvi', max_length=100, blank=True) # Field name made lowercase.
    scapprovi = models.CharField(db_column='sCapProvi', max_length=100, blank=True) # Field name made lowercase.
    sdistr = models.CharField(db_column='sDistr', max_length=100, blank=True) # Field name made lowercase.
    snomvia = models.CharField(db_column='sNomVia', max_length=100, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'vst_ref_x_unidad'
