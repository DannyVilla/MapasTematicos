from RS import genera_rs


# from HTML import genera_html
def highlight(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.7,
        'line_opacity': 0.7
    }


def html_tabla1(defunciones, edas, iras):
    texto_tabla1 = " "
    if defunciones != "0":
        texto_tabla1 += """           
            <tr>
                <td>Defunciones</td>
                <td>""" + defunciones + """</td>
            </tr>
         """
    if edas != "0":
        texto_tabla1 += """
            <tr>
                <td>EDAS</td>
                <td>""" + edas + """</td>
            </tr>
        """
    if iras != "0":
        texto_tabla1 += """
            <tr>
                <td>IRAS</td>
                <td>""" + iras + """</td>
            </tr>
        """
    return texto_tabla1


def html_tabla2(BCG, pentavalente, HB, RV5, NC, RV1, HEX):
    texto_tabla2 = " "
    if BCG != "0":
        texto_tabla2 += """
            <tr>
                <td>BCG</td>
                <td>""" + BCG + """</td>
            </tr>
         """
    if pentavalente != "0":
        texto_tabla2 += """
            <tr>
                <td>Pentavalente Acelular</td>
                <td>""" + pentavalente + """</td>
            </tr>
        """
    if HB != "0":
        texto_tabla2 += """                                
            <tr>
                <td>Hepatitis B</td>
                <td>""" + HB + """</td>
            </tr>
        """
    if RV5 != "0":
        texto_tabla2 += """                                
            <tr>
                <td>Rotavirus RV5</td>
                <td>""" + RV5 + """</td>
            </tr>
        """
    if NC != "0":
        texto_tabla2 += """                  
            <tr>
                <td>Neumocócica Conjugada</td>
                <td>""" + NC + """</td>
            </tr>
        """
    if RV1 != "0":
        texto_tabla2 += """                                
            <tr>
                <td>Rotavirus RV1</td>
                <td>""" + RV1 + """</td>
            </tr>
        """
    if HEX != "0":
        texto_tabla2 += """                                
            <tr>
                <td>Hexavalente</td>
                <td>""" + HEX + """</td>
            </tr>
        """

    return texto_tabla2


# Función tabla 3
def html_tabla3(HIP, OBE, DIS, TUB, LEP, BRU, EPOC, LEPTO, CH, IMC, VIH):
    texto_tabla3 = " "
    if HIP != "0":
        texto_tabla3 += """
                <tr>
                    <td>Hipertensión</td>
                    <td>""" + HIP + """</td>
                </tr>
         """
    if OBE != "0":
        texto_tabla3 += """
                <tr>
                    <td>Obesidad</td>
                    <td>""" + OBE + """</td>
                </tr>
         """
    if DIS != "0":
        texto_tabla3 += """
                <tr>
                    <td>Dislipedemias</td>
                    <td>""" + DIS + """</td>
                </tr>
         """
    if TUB != "0":
        texto_tabla3 += """
                <tr>
                    <td>Tuberculosis</td>
                    <td>""" + TUB + """</td>
                </tr>
         """
    if LEP != "0":
        texto_tabla3 += """
                <tr>
                    <td>Lepra</td>
                    <td>""" + LEP + """</td>
                </tr>
         """
    if BRU != "0":
        texto_tabla3 += """
                <tr>
                    <td>Brucelosis</td>
                    <td>""" + BRU + """</td>
                </tr>
         """
    if EPOC != "0":
        texto_tabla3 += """
                <tr>
                    <td>EPOC</td>
                    <td>""" + EPOC + """</td>
                </tr>
         """
    if LEPTO != "0":
        texto_tabla3 += """
                <tr>
                    <td>Leptospirosis</td>
                    <td>""" + LEPTO + """</td>
                </tr>
         """
    if CH != "0":
        texto_tabla3 += """
                <tr>
                    <td>Chagas</td>
                    <td>""" + CH + """</td>
                </tr
         """
    if IMC != "0":
        texto_tabla3 += """
                <tr>
                    <td>IMC Niñez</td>
                    <td>""" + IMC + """</td>
                </tr>
         """
    if VIH != "0":
        texto_tabla3 += """
                <tr>
                    <td>VIH</td>
                    <td>""" + VIH + """</td>
                </tr>
         """

    return texto_tabla3

# Función tabla 4
def html_tabla4(UAA, MANT, PREV, PART, PARTC, ELAB, TRAT, CIRU, CONSUL, ANTIRR, ITS, LEHIS):
    texto_tabla4 = " "
    if UAA != "0":
        texto_tabla4 += """
                <tr>
                    <td>Usuarios Activos Adolescentes</td>
                    <td>""" + UAA + """</td>
                </tr>
         """
    if MANT != "0":
        texto_tabla4 += """
                <tr>
                    <td>Mujeres con Método Anticonceptivo</td>
                    <td>""" + MANT + """</td>
                </tr>
         """
    if PREV != "0":
        texto_tabla4 += """
                <tr>
                    <td>Prevención Estomatología</td>
                    <td>""" + PREV + """</td>
                </tr>
         """
    if PART != "0":
        texto_tabla4 += """
                <tr>
                    <td>Partos Atendidos por Parteras</td>
                    <td>""" + PART + """</td>
                </tr>
         """
    if PARTC != "0":
        texto_tabla4 += """
                <tr>
                    <td>Parteras Capacitadas</td>
                    <td>""" + PARTC + """</td>
                </tr>
         """
    if ELAB != "0":
        texto_tabla4 += """
                <tr>
                    <td>Estudios de Laboratorio</td>
                    <td>""" + ELAB + """</td>
                </tr>
         """
    if TRAT != "0":
        texto_tabla4 += """
                <tr>
                    <td>Tratamientos Sustancias Psicoactivas</td>
                    <td>""" + TRAT + """</td>
                </tr>
         """
    if CIRU != "0":
        texto_tabla4 += """
                <tr>
                    <td>Cirugía Extra Muros</td>
                    <td>""" + CIRU + """</td>
                </tr>
         """
    if CONSUL != "0":
        texto_tabla4 += """
                <tr>
                    <td>Consultas a Migrantes</td>
                    <td>""" + CONSUL + """</td>
                </tr>
         """
    if ANTIRR != "0":
        texto_tabla4 += """
                <tr>
                    <td>Vacunación Antirrábica</td>
                    <td>""" + ANTIRR + """</td>
                </tr>
         """
    if ITS != "0":
        texto_tabla4 += """
                <tr>
                    <td>Consulta ITS</td>
                    <td>""" + ITS + """</td>
                </tr>
         """
    if LEHIS != "0":
        texto_tabla4 += """
                <tr>
                    <td>Tratamientos Lehismaniasis</td>
                    <td>""" + LEHIS + """</td>
                </tr>
         """
    return texto_tabla4


def genera_tarjeta(MUNICIPIO, JURISDICCION, defunciones, edas, iras, BCG, pentavalente, HB, RV5, NC, RV1, HEX, HIP, OBE,
                   DIS, TUB, LEP, BRU, EPOC, LEPTO, CH, IMC, VIH, UAA, MANT, PREV, PART, PARTC, ELAB, TRAT, CIRU,
                   CONSUL, ANTIRR, ITS, LEHIS):
    # CONTENIDO TABLA 1

    contenido_tabla1 = """
    <div class="col-sm-6">
                <table id=defunciones class="table table-hover table-sm " style="font-family:sans-serif; font-size:9px;color:#FFFFFF; background-color:#C4903D;">
                <tr>
                    <td>
                        <p align = "center" style = "margin:0;font-family:sans-serif;font-size:12px;color:#000000;"><b>Detecciones</b></p>
                    </td>                
                </tr> 
    """
    cierre = """
                </table>
            </div>
    """
    validar_tabla1 = html_tabla1(defunciones, edas, iras)
    if validar_tabla1 != " ":
        validar_tabla1 = contenido_tabla1 + validar_tabla1 + cierre


    # CONTENIDO TABLA2

    contenido_tabla2 = """
        <div class="col-sm-6">
        <table id=aplicaciones class="table table-hover table-sm " style="font-family:sans-serif; font-size:9px;color:#FFFFFF; background-color:#C4903D;"> 
            <tr>
                <td>
                    <p align = "center" style = "margin:0;font-family:sans-serif;font-size:12px;color:#000000;"><b>Aplicaciones de Biológicos</b></p>
                </td>                
            </tr>          
        """
    cierre = """
                    </table>
                </div>
        """

    validar_tabla2 = html_tabla2(BCG, pentavalente, HB, RV5, NC, RV1, HEX)
    if validar_tabla2 != " ":
        validar_tabla2 = contenido_tabla2 + validar_tabla2 + cierre

    # CONTENIDO TABLA3

    contenido_tabla3 = """
        <div class="col-sm-6">
            <table id=detecciones class="table table-hover table-sm " style="font-family:sans-serif; font-size:9px;color:#FFFFFF; background-color:#D25B8A;"> 
            <tr>
                <td>
                    <p align = "center" style = "margin:0;font-family:sans-serif;font-size:12px;color:#000000;"><b>Detecciones</b></p>
                </td>                
            </tr>
        """
    cierre = """
                    </table>
                </div>
        """
    validar_tabla3 = html_tabla3(HIP, OBE, DIS, TUB, LEP, BRU, EPOC, LEPTO, CH, IMC, VIH)
    if validar_tabla3 != " ":
        validar_tabla3 = contenido_tabla3 + validar_tabla3 + cierre

    # CONTENIDO TABLA3

    contenido_tabla4 = """
        <div class="col-sm-6">
            <table id=otros class="table table-hover table-sm " style="font-family:sans-serif; font-size:9px;color:#FFFFFF; background-color:#D25B8A;"> 
            <tr>
                <td>
                    <p align = "center" style = "margin:0;font-family:sans-serif;font-size:12px;color:#000000;"><b>Otros</b></p>
                </td>                
            </tr>        
        """
    cierre = """
                    </table>
                </div>
        """
    validar_tabla4 = html_tabla4(UAA, MANT, PREV, PART, PARTC, ELAB, TRAT, CIRU, CONSUL, ANTIRR, ITS, LEHIS)
    if validar_tabla4 != " ":
        validar_tabla4 = contenido_tabla4 + validar_tabla4 + cierre

    texto = """
    <article class="popup" style="background-color:#900C3F; font-family:sans-serif; font-size:14px;border-radius: 20px;">
        <div class = "card-body" style="width: 500px ;background-color:#900C3F;border-radius: 15px;">
            <h5 align ="center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
            <h6 align = "center" style = "color:#FFFFFF; margin: 0px; font-size:11px; font-family:sans-serif;">Jurisdicción: """ + JURISDICCION + """ </h6>
        <div class="row justify-content-center">
            
            """ + validar_tabla1 + """
            """ + validar_tabla2 + """
        </div>
    
        <div class="row justify-content-center">
            """ + validar_tabla3 + """
            """ + validar_tabla4 + """   
        </div>        

      """

    texto += """<div align = center><p style="margin:0; font-family:sans-serif; color:white">Más información: </p> """ + genera_rs("SESVER") + """</div>
        </article>
        """

    texto += """
        </div>
    </article>
    """

    return texto


def content_unidades(NOMBRE, MUNICIPIO, LOCALIDAD, TIPO, DIRECCION):
    texto = """
        <article class="popup" style="background-color:#900C3F; font-family:sans-serif; font-size:14px;border-radius: 20px;">
        <div class = "card-body" align = "center">
            <h5><span class="badge badge-danger">Municipio: """ + MUNICIPIO + """</span></h5>
            <h6 style="margin:0;color:#FFFFFF;font-family:sans-serif;font-size:11px;"><strong>Localidad: </strong>""" + LOCALIDAD + """</h6>
            <h6 style="margin:0;color:#FFFFFF;font-family:sans-serif;font-size:11px"><strong>Nombre de la Unidad Medica: </strong>""" + NOMBRE + """</h6>
            <h6 style="margin:0;color:#FFFFFF;font-family:sans-serif;font-size:11px"><strong>Tipo: </strong>""" + TIPO + """</h6>
            <h6 style="margin:0;color:#FFFFFF;font-family:sans-serif;font-size:11px"><i class="fa-regular fa-location-dot"></i><strong>Dirección: </strong>""" + DIRECCION + """</h6>
        <div>
        """
    texto += """<div align = center><p style="margin: 0px;color:white;font-family:sans-serif;font-size:11px">Más información: </p> """ + genera_rs("SESVER") + """</div>
        </article>
        """
    return texto


def genera_tarjeta_intervencion(MUNICIPIO,JUR,CLUES,LOCALIDAD,TIPO_UNIDAD,NOMBRE_UNIDAD,ANIO_INTERVENCION,TIPO_INTERVENCION,POBLACION):
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;" align="center"><strong>JURISDICCIÓN: </strong>""" + JUR + """</p>
                <p style="color:#FFFFFF; margin: 0px;" align="center"><strong>LOCALIDAD: </strong>""" + LOCALIDAD + """</p>
                <p style="color:#FFFFFF; margin: 0px;" align="center"><strong>TIPO: </strong>""" + TIPO_UNIDAD + """</p>
                <p style="color:#FFFFFF; margin: 0px;" align="center"><strong>NOMBRE DE LA UNIDAD MÉDICA: </strong>""" + NOMBRE_UNIDAD + """</p>
                <p style="color:#FFFFFF; margin: 0px;" align="center"><strong>AÑO DE INTERVENCIÓN: </strong>""" + ANIO_INTERVENCION + """</p>
                <p style="color:#FFFFFF; margin: 0px;" align="center"><strong>TIPO DE INTERVENCIÓN: </strong>""" + TIPO_INTERVENCION + """</p>
                <p style="color:#FFFFFF; margin: 0px;" align="center"><strong>POBLACIÓN: </strong>""" + POBLACION + """</p>
        """
    texto += """            
                <div align = "center">
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("SESVER") + """
                </div>
            </div>
        </article>
        """
    return texto


def content_unidades_2022(MUNICIPIO, LOCALIDAD, TIPO, NOMBRE, ANIO_INTERVENCION, TIPO_INTERVENCION):
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;" align="center"><strong>LOCALIDAD: </strong>""" + LOCALIDAD + """</p>
                <p style="color:#FFFFFF; margin: 0px;" align="center"><strong>TIPO: </strong>""" + TIPO + """</p>
                <p style="color:#FFFFFF; margin: 0px;" align="center"><strong>NOMBRE DE LA UNIDAD MÉDICA: </strong>""" + NOMBRE + """</p>
                <p style="color:#FFFFFF; margin: 0px;" align="center"><strong>AÑO DE INTERVENCIÓN: </strong>""" + ANIO_INTERVENCION + """</p>
                <p style="color:#FFFFFF; margin: 0px;" align="center"><strong>TIPO DE INTERVENCIÓN: </strong>""" + TIPO_INTERVENCION + """</p>

        """
    texto += """            
                <div align = "center">
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("SESVER") + """
                </div>
            </div>
        </article>
        """
    return texto

