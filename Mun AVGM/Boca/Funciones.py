def highlight(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.7,
        'line_opacity': 0.7
    }


def content_tarjeta(row):
    texto = """
        <article class="popup" style="background-color:#FDF2E9; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body" style = "width:550px"; >
                <h5 align = "center"><span class="badge badge-danger">""" + str(row.MUNICIPIO) + """</span></h5>
                <h6 align = "center">Región: """ + str(row.REGION) + """</h6>

            """
    texto += """ 
        <div class="row">
            <div class="col-sm-6">          
                <table class="table table-hover table-sm " style=" font-family:sans-serif; font-size:9px;color:#FFFFFF; background-color:#D25B8A;">
                    <tr>
                        <th colspan="2" style="font-family:sans-serif; font-size:12px;color:#000000; background-color:#5DADE2;">INDICADORES SOCIODEMOGRÁFICOS</th>
                    </tr>
                    <tr>
                        <th>INDICADOR</th>
                        <th>VALOR</th>
                    </tr>
                    <tr>
                        <td>Tasa de Fecundidad Forzada</td>
                        <td style="font-family:sans-serif;background-color:""" + str(getTFF(row.TFF)) + """;">""" + str(
        row.TFF) + """</td>
                    </tr>
                    <tr>
                        <td>Tasa Específica de Fecundidad</td>
                        <td style="font-family:sans-serif;background-color:""" + str(getTEF(row.TEF)) + """;">""" + str(
        row.TEF) + """</td>
                    </tr>
                    <tr>
                        <td>% Embarazo adolescente</td>
                        <td style="font-family:sans-serif;background-color:""" + str(
        getPEMB_A(row.PEMB_A)) + """;">""" + str(
        row.PEMB_A) + """</td>
                    </tr>
                    <tr>
                        <td>Grado de Marginación</td>
                        <td style="font-family:sans-serif;background-color:""" + str(
        getG_MARG(row.G_MARG)) + """;">""" + str(
        row.G_MARG) + """</td>
                    </tr>
                    <tr>
                        <td>Grado de Rezago Social</td>
                        <td style="font-family:sans-serif;background-color:""" + str(
        getG_RS(row.G_RS)) + """;">""" + str(
        row.G_RS) + """</td>
                    </tr>
                    <tr>
                        <td>% Rezago Educativo</td>
                        <td style="font-family:sans-serif;background-color:""" + str(
        getPREZ_EDU(row.PREZ_EDU)) + """;">""" + str(
        row.PREZ_EDU) + """</td>
                    </tr>
                    <tr>
                        <td>% Pobreza</td>
                        <td style="font-family:sans-serif;background-color:""" + str(
        getPOBREZA(row.POBREZA)) + """;">""" + str(
        row.POBREZA) + """</td>
                    </tr>
                    <tr>
                        <td>% Pobreza Extrema</td>
                        <td style="font-family:sans-serif;background-color:""" + str(
        getPOBREZAE(row.POBREZAE)) + """;">""" + str(
        row.POBREZAE) + """</td>
                    </tr>
                    <tr>
                        <td>Grado Promedio de Escolaridad</td>
                        <td style="font-family:sans-serif;background-color:""" + str(
        getGP_ESCOL(row.GP_ESCOL)) + """;">""" + str(
        row.GP_ESCOL) + """</td>
                    </tr>
                    <tr>
                        <td>% Población Migrante</td>
                        <td style="font-family:sans-serif;background-color:""" + str(
        getPPOB_MIG(row.PPOB_MIG)) + """;">""" + str(
        row.PPOB_MIG) + """</td>
                    </tr>
                    <tr>
                        <td>% Población Indígena</td>
                        <td style="font-family:sans-serif;background-color:""" + str(
        getPPOB_IND(row.PPOB_IND)) + """;">""" + str(
        row.PPOB_IND) + """</td>
                    </tr>
                    <tr>
                        <td>% Población Inígena que Habla Español</td>
                        <td style="font-family:sans-serif;background-color:""" + str(
        getPPOBLIE(row.PPOBLIE)) + """;">""" + str(
        row.PPOBLIE) + """</td>
                    </tr>
                    <tr>
                        <td>% Población Indígena no Habla Español</td>
                        <td style="font-family:sans-serif;background-color:""" + str(
        getPPOBLINE(row.PPOBLINE)) + """;">""" + str(
        row.PPOBLINE) + """</td>
                    </tr>
                </table>
            </div>
                """


    texto += """
            <div class="col-sm-6">
                <table class="table table-hover table-sm " style=" font-family:sans-serif; font-size:9px;color:#FFFFFF; background-color:#D25B8A;">
                    <tr>
                        <th colspan="2" style="font-family:sans-serif; font-size:12px;color:#000000; background-color:#5DADE2;">INDICADORES INCIDENCIA DELICTIVA</th>
                    </tr>
                    <tr>
                        <th>INDICADOR</th>
                        <th>VALOR</th>
                    </tr>
                    <tr>
                        <td>Casos atendidos por IVM 2022</td>
                        <td style="font-family:sans-serif;background-color:""" + str(
        getIVM_2021(row.IVM_2022)) + """;">""" + str(
        row.IVM_2022) + """</td>
                    </tr>
                    <tr>
                        <td>Casos atendidos por Salud 2022</td>
                        <td style="font-family:sans-serif;background-color:""" + str(
        getSALUD_21(row.SALUD_22)) + """;">""" + str(
        row.SALUD_22) + """</td>
                    </tr>
                    <tr>
                        <td>Abuso Sexual</td>
                        <td style="font-family:sans-serif;background-color:""" + str(
        getabuso_sex(row.abuso_sex)) + """;">""" + str(
        row.abuso_sex) + """</td>
                    </tr>
                    <tr>
                        <td>Feminicidio</td>
                        <td style="font-family:sans-serif;background-color:""" + str(
        getfeminicidio(row.Feminicidio)) + """;">""" + str(
        row.Feminicidio) + """</td>
                    </tr>
                    <tr>
                        <td>Homicidio Culposo</td>
                        <td style="font-family:sans-serif;background-color:""" + str(
        gethomicidio_culposo(row.homicidio_culposo)) + """;">""" + str(
        row.homicidio_culposo) + """</td>
                    </tr>
                    <tr>
                        <td>Homicidio Doloso</td>
                        <td style="font-family:sans-serif;background-color:""" + str(
        gethomicidio_doloso(row.homicidio_doloso)) + """;">""" + str(
        row.homicidio_doloso) + """</td>
                    </tr>
                    <tr>
                        <td>Lesiones Culposas</td>
                        <td style="font-family:sans-serif;background-color:""" + str(
        getlesionesculposas(row.lesionesculposas)) + """;">""" + str(
        row.lesionesculposas) + """</td>
                    </tr>
                    <tr>
                        <td>Lesiones Dolosas</td>
                        <td style="font-family:sans-serif;background-color:""" + str(
        getlesiones_dolosas(row.lesiones_dolosas)) + """;">""" + str(
        row.lesiones_dolosas) + """</td>
                    </tr>
                     <tr>
                        <td>Narco menudeo</td>
                        <td style="font-family:sans-serif;background-color:""" + str(
        getnarcomenudeo(row.narcomenudeo)) + """;">""" + str(
        row.narcomenudeo) + """</td>
                    </tr>
                    <tr>
                        <td>Secuestro</td>
                        <td style="font-family:sans-serif;background-color:""" + str(
        getsecuestro(row.secuestro)) + """;">""" + str(
        row.secuestro) + """</td>
                    </tr>
                    <tr>
                        <td>Trata de Personas</td>
                        <td style="font-family:sans-serif;background-color:""" + str(
        gettrata(row.trata)) + """;">""" + str(
        row.trata) + """</td>
                    </tr>
                    <tr>
                        <td>Violación Simple</td>
                        <td style="font-family:sans-serif;background-color:""" + str(
        getviola_simple(row.viola_simple)) + """;">""" + str(
        row.viola_simple) + """</td>
                    </tr>
                    <tr>
                        <td>Violencia de Género</td>
                        <td style="font-family:sans-serif;background-color:""" + str(
        getviolen_genero(row.violen_genero)) + """;">""" + str(
        row.violen_genero) + """</td>
                    </tr>
                    </tr>
                    <tr>
                        <td>Violencia Familiar</td>
                        <td style="font-family:sans-serif;background-color:""" + str(
        getviolen_fam(row.violen_fam)) + """;">""" + str(
        row.violen_fam) + """</td>
                    </tr>
                </table>
            </div>
        </div>
    """
    if str(row.MUNICIPIO)=="VERACRUZ":
        print(texto)
    return texto

def content_unidades(NOMBRE, MUNICIPIO, LOCALIDAD, TIPO, DIRECCION):
    texto = """
        <article style="width: 400px;background-color:#39395B;border-radius: 5px; padding:20px">
        <div align=center><h4><span class="label label-primary">MUNICIPIO: """ + MUNICIPIO + """</span></h2><div>
        <div class='h5 text-left' id='pageHeaderTitle' style="color:#FFFFFF;font-family:sans-serif;"><strong>LOCALIDAD: </strong>""" + LOCALIDAD + """</div>
        <div class='h5 text-left' id='pageHeaderTitle' style="color:#FFFFFF;font-family:sans-serif;"><strong>NOMBRE DE LA UNIDAD MÉDICA: </strong>""" + NOMBRE + """</div>
        <div class='h5 text-left' id='pageHeaderTitle' style="color:#FFFFFF;font-family:sans-serif;"><strong>TIPO: </strong>""" + TIPO + """</div>
        <div class='h5 text-left' id='pageHeaderTitle' style="color:#FFFFFF;font-family:sans-serif;"><strong>DIRECCIÓN: </strong>""" + DIRECCION + """</div>
        """
    texto += """<div class="panel-body"><p style="color:white">Más información: </p> """ + + """
            </div>
        </article>
        """
    return texto


def getTFF(val):
    color = ""
    if 0.00 <= val <= 0.94:
        color = "#307330"  # verde oscuro
    elif 0.94 <= val <=2.33:
        color = "#6f9031"  # verde claro
    elif 2.33 <= val <=3.77:
        color = "#ffed00"  # amarillo
    elif 3.77 <= val <= 7.0:
        color = "#ef7b00"  # naranja
    if 7.0 <= val <=12.82:
        color = "#e30613"  # rojo
    return color


def getTEF(val):
    color = ""
    if 14.86<= val <=39.16:
        color = "#307330"  # verde oscuro
    elif 39.16<= val <= 56.23:
        color = "#6f9031"  # verde claro
    elif 56.23 <= val <= 77:
        color = "#ffed00"  # amarillo
    elif 77 <= val <= 100.78:
        color = "#ef7b00"  # naranja
    if 100.78 <= val <= 163.27:
        color = "#e30613"  # rojo
    return color


def getPEMB_A(val):
    color = ""
    if 9.375 <= val <= 16.01:
        color = "#307330"  # verde oscuro
    elif 16.01 <= val <= 19.811:
        color = "#6f9031"  # verde claro
    elif 19.811 <= val <= 23.664:
        color = "#ffed00"  # amarillo
    elif 23.664 <= val <= 30.337:
        color = "#ef7b00"  # naranja
    elif 30.337 <= val <= 39.241:
        color = "#e30613"  # rojo
    return color


def getG_MARG(val):
    color = ""
    if val == "Muy Alto":
        color = "#e30613"
    elif val == "Alto":
        color = "#ef7b00"
    elif val == "Medio":
        color = "#ffed00"
    elif val == "Bajo":
        color = "#6f9031"
    elif val == "Muy bajo":
        color = "#307330"
    return color


def getG_RS(val):
    color = ""
    if val == "Muy Alto":
        color = "#e30613"
    elif val == "Alto":
        color = "#ef7b00"
    elif val == "Medio":
        color = "#ffed00"
    elif val == "Bajo":
        color = "#6f9031"
    elif val == "Muy bajo":
        color = "#307330"
    return color


def getPREZ_EDU(val):
    color = ""
    if 7.33<= val <=18.079:
        color = "#307330"  # verde oscuro
    elif 18.079<= val <= 27.419:
        color = "#6f9031"  # verde claro
    elif 27.419 <= val <=34.725:
        color = "#ffed00"  # amarillo
    elif 34.725 <= val <=42.471:
        color = "#ef7b00"  # naranja
    elif 42.471 <= val <= 59.084:
        color = "#e30613"  # rojo
    return color


def getPOBREZA(val):
    color = ""
    if 30.02 <= val <= 48.87:
        color = "#307330"  # verde oscuro
    elif 48.87 <= val <= 60.76:
        color = "#6f9031"  # verde claro
    elif 60.76 <= val <=73.19:
        color = "#ffed00"  # amarillo
    elif 73.19 <= val <=84.35:
        color = "#ef7b00"  # naranja
    elif 84.35 <= val <= 97.12:
        color = "#e30613"  # rojo
    return color


def getPOBREZAE(val):
    color = ""
    if 3.394 <= val <= 13.112:
        color = "#307330"  # verde oscuro
    elif 13.112 <= val <= 22.391:
        color = "#6f9031"  # verde claro
    elif 22.391 <= val <= 33.802:
        color = "#ffed00"  # amarillo
    elif 33.802 <= val <= 50.113:
        color = "#ef7b00"  # naranja
    elif 50.113 <= val <= 64.849:
        color = "#e30613"  # rojo
    return color


def getGP_ESCOL(val):
    color = ""
    if 9.29 <= val <= 11.4:
        color = "#307330"  # verde oscuro
    elif 7.96 <= val <= 9.29:
        color = "#6f9031"  # verde claro
    elif 7.09 <= val <= 7.96:
        color = "#ffed00"  # amarillo
    elif 6.12 <= val <= 7.09:
        color = "#ef7b00"  # naranja
    elif 4.3 <= val <= 6.12:
        color = "#e30613"  # rojo
    return color


def getPPOB_MIG(val):
    color = ""
    if 1.14 <= val <= 2.979:
        color = "#307330"  # verde oscuro
    elif 2.979<= val <= 4.297:
        color = "#6f9031"  # verde claro
    elif  4.297 <= val <= 5.723:
        color = "#ffed00"  # amarillo
    elif 5.723 <= val <= 8.664:
        color = "#ef7b00"  # naranja
    elif 8.664 <= val <= 12.96:
        color = "#e30613"  # rojo
    return color


def getPPOB_IND(val):
    color = ""
    if 0.06 <= val <= 10.25:
        color = "#307330"  # verde oscuro
    elif 10.25 <= val <= 28.68:
        color = "#6f9031"  # verde claro
    elif 28.68<= val <=51.94:
        color = "#ffed00"  # amarillo
    elif 51.94<= val <=78.22:
        color = "#ef7b00"  # naranja
    elif 78.22<= val <=97.12:
        color = "#e30613"  # rojo
    return color


def getPPOBLIE(val):
    color = ""
    if 0.064 <= val <= 9.227:
        color = "#307330"  # verde oscuro
    elif 9.227 <= val <= 26.874:
        color = "#6f9031"  # verde claro
    elif 26.874 <= val <= 48.317:
        color = "#ffed00"  # amarillo
    elif 48.317 <= val <= 69.144:
        color = "#ef7b00"  # naranja
    elif 69.144 <= val <= 86.22:
        color = "#e30613"  # rojo
    return color


def getPPOBLINE(val):
    color = ""
    if 0 <= val <=1.4:
        color = "#307330"  # verde oscuro
    elif 1.4 <= val <= 5:
        color = "#6f9031"  # verde claro
    elif 5 <= val <= 13.9:
        color = "#ffed00"  # amarillo
    elif 13.9 <= val <= 22.5:
        color = "#ef7b00"  # naranja
    elif 22.5 <= val <=30.3:
        color = "#e30613"  # rojo
    return color


def getIVM_2021(val):
    color = ""
    if 0 <= val <= 5:
        color = "#307330"  # verde oscuro
    elif 5 <= val <= 16:
        color = "#6f9031"  # verde claro
    elif 16 <= val <= 37:
        color = "#ffed00"  # amarillo
    elif 37 <= val <= 232:
        color = "#ef7b00"  # naranja
    elif 232 <= val <= 512:
        color = "#e30613"  # rojo
    return color

def getSALUD_21(val):
    color = ""
    if 0 <= val <= 4:
        color = "#307330"  # verde oscuro
    elif 4 <= val <= 17:
        color = "#6f9031"  # verde claro
    elif 17 <= val <= 46:
        color = "#ffed00"  # amarillo
    elif 46 <= val <= 100:
        color = "#ef7b00"  # naranja
    elif 100 <= val <= 250:
        color = "#e30613"  # rojo
    return color

def getabuso_sex(val):
    color = ""
    if 0 <= val <= 1:
        color = "#307330"  # verde oscuro
    elif 1 <= val <= 4:
        color = "#6f9031"  # verde claro
    elif 4 <= val <= 11:
        color = "#ffed00"  # amarillo
    elif 11 <= val <= 29:
        color = "#ef7b00"  # naranja
    elif 29 <= val <= 49:
        color = "#e30613"  # rojo
    return color

def getfeminicidio(val):
    color = ""
    if 0<= val <=0:
        color = "#307330"  # verde oscuro
    elif 0<= val <=0:
        color = "#6f9031"  # verde claro
    elif 0<= val <=0:
        color = "#ffed00"  # amarillo
    elif 0<= val <=1:
        color = "#ef7b00"  # naranja
    elif 1<= val <=3:
        color = "#e30613"  # rojo
    return color

def gethomicidio_culposo(val):
    color = ""
    if 0<= val <=0:
        color = "#307330"  # verde oscuro
    elif 1<= val <=4:
        color = "#6f9031"  # verde claro
    elif 4<= val <=8:
        color = "#ffed00"  # amarillo
    elif 8<= val <=15:
        color = "#ef7b00"  # naranja
    elif 15<= val <=56:
        color = "#e30613"  # rojo
    return color

def gethomicidio_doloso(val):
    color = ""
    if 0<= val <=0:
        color = "#307330"  # verde oscuro
    elif 0<= val <=2:
        color = "#6f9031"  # verde claro
    elif 2<= val <=5:
        color = "#ffed00"  # amarillo
    elif 5<= val <=9:
        color = "#ef7b00"  # naranja
    elif 9<= val <=17:
        color = "#e30613"  # rojo
    return color

def getlesionesculposas(val):
    color = ""
    if 0<= val <=3:
        color = "#307330"  # verde oscuro
    elif 3<= val <=9:
        color = "#6f9031"  # verde claro
    elif 9<= val <=21:
        color = "#ffed00"  # amarillo
    elif 21<= val <=47:
        color = "#ef7b00"  # naranja
    elif 47<= val <=77:
        color = "#e30613"  # rojo
    return color

def getlesiones_dolosas(val):
    color = ""
    if 0<= val <=10:
        color = "#307330"  # verde oscuro
    elif 10<= val <=31:
        color = "#6f9031"  # verde claro
    elif 31<= val <=59:
        color = "#ffed00"  # amarillo
    elif 59<= val <=161:
        color = "#ef7b00"  # naranja
    elif 161<= val <=285:
        color = "#e30613"  # rojo
    return color

def getnarcomenudeo(val):
    color = ""
    if 0<= val <=3:
        color = "#307330"  # verde oscuro
    elif 3<= val <=11:
        color = "#6f9031"  # verde claro
    elif 11<= val <=26:
        color = "#ffed00"  # amarillo
    elif 26<= val <=64:
        color = "#ef7b00"  # naranja
    elif 64<= val <=80:
        color = "#e30613"  # rojo
    return color

def getsecuestro(val):
    color = ""
    if 0<= val <=0:
        color = "#307330"  # verde oscuro
    elif 0<= val <=0:
        color = "#6f9031"  # verde claro
    elif 0<= val <=1:
        color = "#ffed00"  # amarillo
    elif 1<= val <=2:
        color = "#ef7b00"  # naranja
    elif 2<= val <=4:
        color = "#e30613"  # rojo
    return color

def gettrata(val):
    color = ""
    if 0<= val <=0:
        color = "#307330"  # verde oscuro
    elif 0<= val <=0:
        color = "#6f9031"  # verde claro
    elif 0<= val <=0:
        color = "#ffed00"  # amarillo
    elif 0<= val <=0:
        color = "#ef7b00"  # naranja
    elif 0<= val <=1:
        color = "#e30613"  # rojo
    return color

def getviola_simple(val):
    color = ""
    if 0<= val <=0:
        color = "#307330"  # verde oscuro
    elif 0<= val <=2:
        color = "#6f9031"  # verde claro
    elif 2<= val <=6:
        color = "#ffed00"  # amarillo
    elif 6<= val <=17:
        color = "#ef7b00"  # naranja
    elif 17<= val <=26:
        color = "#e30613"  # rojo
    return color

def getviolen_genero(val):
    color = ""
    if 0<= val <=3:
        color = "#307330"  # verde oscuro
    elif 3<= val <=12:
        color = "#6f9031"  # verde claro
    elif 12<= val <=34:
        color = "#ffed00"  # amarillo
    elif 34<= val <=78:
        color = "#ef7b00"  # naranja
    elif 78<= val <=134:
        color = "#e30613"  # rojo
    return color

def getviolen_fam(val):
    color = ""
    if 0<= val <=18:
        color = "#307330"  # verde oscuro
    elif 18<= val <=57:
        color = "#6f9031"  # verde claro
    elif 57<= val <=121:
        color = "#ffed00"  # amarillo
    elif 121<= val <=440:
        color = "#ef7b00"  # naranja
    elif 440<= val <=652:
        color = "#e30613"  # rojo
    return color

def genera_carousel(lista, tipo):
    i = 0
    hay = False
    carousel = [" ", hay]
    carousel_inicio = """ <!-- Carousel container -->
                   <div id= "carouselExampleIndicators" class="carousel slide" data-ride="carousel">

                   """
    carousel_indicadores = """ <!-- Indicators -->
                       <ol class="carousel-indicators">"""
    carousel_contenido = """
                <!-- Content -->
                <div class="carousel-inner" role="listbox">"""

    carousel_controls = """
                <!-- Previous/Next controls -->
                      <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
                        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                        <span class="sr-only">Previous</span>
                      </a>
                      <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
                        <span class="carousel-control-next-icon" aria-hidden="true"></span>
                        <span class="sr-only">Next</span>
                      </a>         
                </div>
        """
    if lista:
        for elemento in lista:
            if elemento != "0":
                hay = True
                carousel_indicadores += """
                      <li data-target="#carouselExampleIndicators" data-slide-to='""" + str(i) + """' class="active"></li>
                          """
                if i == 0:
                    cl = "carousel-item active"
                else:
                    cl = "carousel-item"
                if tipo == "mixto":
                    if "https://live." in elemento:
                        carousel_contenido += """        <!-- Slide -->
                                    <div class='""" + cl + """'>
                                       <img class="d-block w-100" src='""" + str(elemento) + """' width='250' height='180'/>
                                    </div>        
                                               """
                    elif "https://flic.kr" in elemento:
                        carousel_contenido += """<!-- Slide -->
                                    <div class='""" + cl + """' style="height:180;width:250;">
                                        <p align = "center" style = "color:white"> Para más información consulta el siguiente enlace:
                                        <br>
                                            <a href='""" + str(elemento) + """' target="_blank"><strong>Link del Álbum </strong></a>
                                        </p>
                                        <br>
                                    </div>        
                                """
                    else:
                        carousel_contenido += """        <!-- Slide -->
                                    <div class='""" + cl + """' style="height:180;width:250;">
                                        """ + str(elemento) + """
                                    </div>
                            """
            i += 1
        carousel[
            0] = carousel_inicio + carousel_indicadores + "</ol>" + carousel_contenido + "</div>" + carousel_controls
        carousel[1] = hay
    return carousel

def tarjeta_acciones(row):
    FOTOS = [str(row.FOTO1), str(row.FOTO2), str(row.VIDEO)]
    fecha=str(row.FECHA).replace(" 00:00:00", "")

    texto = """
        <article class="popup" style="background-color:#6A0888; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + str(row.LOCALIDAD) + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i>""" + fecha + """  </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-group" style = "color:#FAC63A;"></i><strong>TOTAL PERSONAS BENEFICIADAS: </strong>""" + str(
        row.TOTAL) + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-female" style = "color:#FAC63A;"></i><strong>MUJERES: </strong>""" + str(
        row.MUJERES) + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-male" style = "color:#FAC63A;"></i><strong>HOMBRES: </strong>""" + str(
        row.HOMBRES) + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><strong>DESCRIPCIÓN: </strong>""" + str(row.DESCRIPCION) + """</p>
        """

    texto += """
        <div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
            <div class="carousel-inner">    
    """

    carousel_fotos = genera_carousel(FOTOS, "mixto")
    if carousel_fotos[1] :
        if carousel_fotos:
            texto += carousel_fotos[0]

    return texto

