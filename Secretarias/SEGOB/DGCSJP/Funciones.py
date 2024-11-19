from RS import genera_rs


def highlight(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.7,
        'line_opacity': 0.7
    }


def genera_tabla(NUM1,FECHA1,FOTO1, NUM2,FECHA2,FOTO2, NUM3,FECHA3,FOTO3, NUM4,FECHA4,FOTO4, NUM5,FECHA5,FOTO5,
                 NUM6,FECHA6,FOTO6, NUM7,FECHA7,FOTO7, NUM8,FECHA8,FOTO8, NUM9,FECHA9,FOTO9, NUM10,FECHA10,FOTO10,
                 NUM11,FECHA11,FOTO11, NUM12,FECHA12,FOTO12, NUM13,FECHA13,FOTO13, NUM14,FECHA14,FOTO14, NUM15,FECHA15,FOTO15,
                 NUM16,FECHA16,FOTO16, NUM17,FECHA17,FOTO17, NUM18,FECHA18,FOTO18, NUM19,FECHA19,FOTO19, NUM20,FECHA20,FOTO20,
                 NUM21,FECHA21,FOTO21, NUM22,FECHA22,FOTO22, NUM23,FECHA23,FOTO23, NUM24,FECHA24,FOTO24):

    fila_tabla = " "
    if NUM1 != "0":
        fila_tabla += """           
                    <tr>
                        <td><p align = "center" style="color:#FFFFFF; margin: 0px;">""" + NUM1 + """</p></td>
                        <td><p align = "center" style="color:#FFFFFF; margin: 0px;">""" + FECHA1 + """</p></td>
            """
        if FOTO1 != "0":
            fila_tabla += """
                            <td><p align = "center" style="margin: 0px;"><a href = '""" + FOTO1 + """'><i class ="fa fa-camera"></i></a></p></td>

                """
        fila_tabla += """
                        </tr>
            """

    if NUM2 != "0":
        fila_tabla += """           
                        <tr>
                            <td><p align = "center" style="color:#FFFFFF; margin: 0px;">""" + NUM2 + """</p></td>
                            <td><p align = "center" style="color:#FFFFFF; margin: 0px;">""" + FECHA2 + """</p></td>
                """
        if FOTO2 != "0":
            fila_tabla += """
                            <td><p align = "center" style="margin: 0px;"><a href = '""" + FOTO2 + """'><i class ="fa fa-camera"></i></a></p></td>

                """
        fila_tabla += """
                        </tr>
            """

    if NUM3 != "0":
        fila_tabla += """           
                        <tr>
                            <td><p align = "center" style="color:#FFFFFF; margin: 0px;">""" + NUM3 + """</p></td>
                            <td><p align = "center" style="color:#FFFFFF; margin: 0px;">""" + FECHA3 + """</p></td>
                """
        if FOTO3 != "0":
            fila_tabla += """
                            <td><p align = "center" style="margin: 0px;"><a href = '""" + FOTO3 + """'><i class ="fa fa-camera"></i></a></p></td>

                """
        fila_tabla += """
                        </tr>
            """

    if NUM4 != "0":
        fila_tabla += """           
                        <tr>
                            <td><p align = "center" style="color:#FFFFFF; margin: 0px;">""" + NUM4 + """</p></td>
                            <td><p align = "center" style="color:#FFFFFF; margin: 0px;">""" + FECHA4 + """</p></td>
                """
        if FOTO4 != "0":
            fila_tabla += """
                            <td><p align = "center" style="margin: 0px;"><a href = '""" + FOTO4 + """'><i class ="fa fa-camera"></i></a></p></td>

                """
        fila_tabla += """
                        </tr>
            """

    if NUM5 != "0":
        fila_tabla += """           
                        <tr>
                            <td><p align = "center" style="color:#FFFFFF; margin: 0px;">""" + NUM5 + """</p></td>
                            <td><p align = "center" style="color:#FFFFFF; margin: 0px;">""" + FECHA5 + """</p></td>
                """
        if FOTO5 != "0":
            fila_tabla += """
                            <td><p align = "center" style="margin: 0px;"><a href = '""" + FOTO5 + """'><i class ="fa fa-camera"></i></a></p></td>

                """
        fila_tabla += """
                        </tr>
            """

    if NUM6 != "0":
        fila_tabla += """           
                        <tr>
                            <td><p align = "center" style="color:#FFFFFF; margin: 0px;">""" + NUM6 + """</p></td>
                            <td><p align = "center" style="color:#FFFFFF; margin: 0px;">""" + FECHA6 + """</p></td>
                """
        if FOTO6 != "0":
            fila_tabla += """
                            <td><p align = "center" style="margin: 0px;"><a href = '""" + FOTO6 + """'><i class ="fa fa-camera"></i></a></p></td>

                """
        fila_tabla += """
                        </tr>
            """

    if NUM7 != "0":
        fila_tabla += """           
                        <tr>
                            <td><p align = "center" style="color:#FFFFFF; margin: 0px;">""" + NUM7 + """</p></td>
                            <td><p align = "center" style="color:#FFFFFF; margin: 0px;">""" + FECHA7 + """</p></td>
                """
        if FOTO7 != "0":
            fila_tabla += """
                            <td><p align = "center" style="margin: 0px;"><a href = '""" + FOTO7 + """'><i class ="fa fa-camera"></i></a></p></td>

                """
        fila_tabla += """
                        </tr>
            """

    if NUM8 != "0":
        fila_tabla += """           
                        <tr>
                            <td><p align = "center" style="color:#FFFFFF; margin: 0px;">""" + NUM8 + """</p></td>
                            <td><p align = "center" style="color:#FFFFFF; margin: 0px;">""" + FECHA8 + """</p></td>
                """
        if FOTO1 != "0":
            fila_tabla += """
                            <td><p align = "center" style="margin: 0px;"><a href = '""" + FOTO1 + """'><i class ="fa fa-camera"></i></a></p></td>

                """
        fila_tabla += """
                        </tr>
            """

    if NUM9 != "0":
        fila_tabla += """           
                        <tr>
                            <td><p align = "center" style="color:#FFFFFF; margin: 0px;">""" + NUM9 + """</p></td>
                            <td><p align = "center" style="color:#FFFFFF; margin: 0px;">""" + FECHA9 + """</p></td>
                """
        if FOTO9 != "0":
            fila_tabla += """
                            <td><p align = "center" style="margin: 0px;"><a href = '""" + FOTO9 + """'><i class ="fa fa-camera"></i></a></p></td>

                """
        fila_tabla += """
                        </tr>
            """

    if NUM10 != "0":
        fila_tabla += """           
                        <tr>
                            <td><p align = "center" style="color:#FFFFFF; margin: 0px;">""" + NUM10 + """</p></td>
                            <td><p align = "center" style="color:#FFFFFF; margin: 0px;">""" + FECHA10 + """</p></td>
                """
        if FOTO10 != "0":
            fila_tabla += """
                            <td><p align = "center" style="margin: 0px;"><a href = '""" + FOTO10 + """'><i class ="fa fa-camera"></i></a></p></td>

                """
        fila_tabla += """
                        </tr>
            """

    if NUM11 != "0":
        fila_tabla += """           
                        <tr>
                            <td><p align = "center" style="color:#FFFFFF; margin: 0px;">""" + NUM11 + """</p></td>
                            <td><p align = "center" style="color:#FFFFFF; margin: 0px;">""" + FECHA11 + """</p></td>
                """
        if FOTO11 != "0":
            fila_tabla += """
                            <td><p align = "center" style="margin: 0px;"><a href = '""" + FOTO11 + """'><i class ="fa fa-camera"></i></a></p></td>

                """
        fila_tabla += """
                        </tr>
            """

    if NUM12 != "0":
        fila_tabla += """           
                        <tr>
                            <td><p align = "center" style="color:#FFFFFF; margin: 0px;">""" + NUM12 + """</p></td>
                            <td><p align = "center" style="color:#FFFFFF; margin: 0px;">""" + FECHA12 + """</p></td>
                """
        if FOTO12 != "0":
            fila_tabla += """
                            <td><p align = "center" style="margin: 0px;"><a href = '""" + FOTO12 + """'><i class ="fa fa-camera"></i></a></p></td>

                """
        fila_tabla += """
                        </tr>
            """

    if NUM13 != "0":
        fila_tabla += """           
                        <tr>
                            <td><p align = "center" style="color:#FFFFFF; margin: 0px;">""" + NUM13 + """</p></td>
                            <td><p align = "center" style="color:#FFFFFF; margin: 0px;">""" + FECHA13 + """</p></td>
                """
        if FOTO13 != "0":
            fila_tabla += """
                            <td><p align = "center" style="margin: 0px;"><a href = '""" + FOTO13 + """'><i class ="fa fa-camera"></i></a></p></td>

                """
        fila_tabla += """
                        </tr>
            """

    if NUM14 != "0":
        fila_tabla += """           
                        <tr>
                            <td><p align = "center" style="color:#FFFFFF; margin: 0px;">""" + NUM14 + """</p></td>
                            <td><p align = "center" style="color:#FFFFFF; margin: 0px;">""" + FECHA14 + """</p></td>
                """
        if FOTO14 != "0":
            fila_tabla += """
                            <td><p align = "center" style="margin: 0px;"><a href = '""" + FOTO14 + """'><i class ="fa fa-camera"></i></a></p></td>

                """
        fila_tabla += """
                        </tr>
            """

    if NUM15 != "0":
        fila_tabla += """           
                        <tr>
                            <td><p align = "center" style="color:#FFFFFF; margin: 0px;">""" + NUM15 + """</p></td>
                            <td><p align = "center" style="color:#FFFFFF; margin: 0px;">""" + FECHA15 + """</p></td>
                """
        if FOTO15 != "0":
            fila_tabla += """
                            <td><p align = "center" style="margin: 0px;"><a href = '""" + FOTO15 + """'><i class ="fa fa-camera"></i></a></p></td>

                """
        fila_tabla += """
                        </tr>
            """

    if NUM16 != "0":
        fila_tabla += """           
                        <tr>
                            <td><p align = "center" style="color:#FFFFFF; margin: 0px;">""" + NUM16 + """</p></td>
                            <td><p align = "center" style="color:#FFFFFF; margin: 0px;">""" + FECHA16 + """</p></td>
                """
        if FOTO16 != "0":
            fila_tabla += """
                            <td><p align = "center" style="margin: 0px;"><a href = '""" + FOTO16 + """'><i class ="fa fa-camera"></i></a></p></td>

                """
        fila_tabla += """
                        </tr>
            """

    if NUM17 != "0":
        fila_tabla += """           
                        <tr>
                            <td><p align = "center" style="color:#FFFFFF; margin: 0px;">""" + NUM17 + """</p></td>
                            <td><p align = "center" style="color:#FFFFFF; margin: 0px;">""" + FECHA17 + """</p></td>
                """
        if FOTO17 != "0":
            fila_tabla += """
                            <td><p align = "center" style="margin: 0px;"><a href = '""" + FOTO17 + """'><i class ="fa fa-camera"></i></a></p></td>

                """
        fila_tabla += """
                        </tr>
            """

    if NUM18 != "0":
        fila_tabla += """           
                        <tr>
                            <td><p align = "center" style="color:#FFFFFF; margin: 0px;">""" + NUM18 + """</p></td>
                            <td><p align = "center" style="color:#FFFFFF; margin: 0px;">""" + FECHA18 + """</p></td>
                """
        if FOTO18 != "0":
            fila_tabla += """
                            <td><p align = "center" style="margin: 0px;"><a href = '""" + FOTO18 + """'><i class ="fa fa-camera"></i></a></p></td>

                """
        fila_tabla += """
                        </tr>
            """

    if NUM19 != "0":
        fila_tabla += """           
                        <tr>
                            <td><p align = "center" style="color:#FFFFFF; margin: 0px;">""" + NUM19 + """</p></td>
                            <td><p align = "center" style="color:#FFFFFF; margin: 0px;">""" + FECHA19 + """</p></td>
                """
        if FOTO19 != "0":
            fila_tabla += """
                            <td><p align = "center" style="margin: 0px;"><a href = '""" + FOTO19 + """'><i class ="fa fa-camera"></i></a></p></td>

                """
        fila_tabla += """
                        </tr>
            """

    if NUM20 != "0":
        fila_tabla += """           
                        <tr>
                            <td><p align = "center" style="color:#FFFFFF; margin: 0px;">""" + NUM20 + """</p></td>
                            <td><p align = "center" style="color:#FFFFFF; margin: 0px;">""" + FECHA20 + """</p></td>
                """
        if FOTO20 != "0":
            fila_tabla += """
                            <td><p align = "center" style="margin: 0px;"><a href = '""" + FOTO20 + """'><i class ="fa fa-camera"></i></a></p></td>

                """
        fila_tabla += """
                        </tr>
            """

    if NUM21 != "0":
        fila_tabla += """           
                        <tr>
                            <td><p align = "center" style="color:#FFFFFF; margin: 0px;">""" + NUM21 + """</p></td>
                            <td><p align = "center" style="color:#FFFFFF; margin: 0px;">""" + FECHA21 + """</p></td>
                """
        if FOTO21 != "0":
            fila_tabla += """
                            <td><p align = "center" style="margin: 0px;"><a href = '""" + FOTO21 + """'><i class ="fa fa-camera"></i></a></p></td>

                """
        fila_tabla += """
                        </tr>
            """

    if NUM22 != "0":
        fila_tabla += """           
                        <tr>
                            <td><p align = "center" style="color:#FFFFFF; margin: 0px;">""" + NUM22 + """</p></td>
                            <td><p align = "center" style="color:#FFFFFF; margin: 0px;">""" + FECHA22 + """</p></td>
                """
        if FOTO22 != "0":
            fila_tabla += """
                            <td><p align = "center" style="margin: 0px;"><a href = '""" + FOTO22 + """'><i class ="fa fa-camera"></i></a></p></td>

                """
        fila_tabla += """
                        </tr>
            """

    if NUM23 != "0":
        fila_tabla += """           
                        <tr>
                            <td><p align = "center" style="color:#FFFFFF; margin: 0px;">""" + NUM23 + """</p></td>
                            <td><p align = "center" style="color:#FFFFFF; margin: 0px;">""" + FECHA23 + """</p></td>
                """
        if FOTO23 != "0":
            fila_tabla += """
                            <td><p align = "center" style="margin: 0px;"><a href = '""" + FOTO23 + """'><i class ="fa fa-camera"></i></a></p></td>

                """
        fila_tabla += """
                        </tr>
            """

    if NUM24 != "0":
        fila_tabla += """           
                        <tr>
                            <td><p align = "center" style="color:#FFFFFF; margin: 0px;">""" + NUM24 + """</p></td>
                            <td><p align = "center" style="color:#FFFFFF; margin: 0px;">""" + FECHA24 + """</p></td>
                """
        if FOTO24 != "0":
            fila_tabla += """
                            <td><p align = "center" style="margin: 0px;"><a href = '""" + FOTO24 + """'><i class ="fa fa-camera"></i></a></p></td>

                """
        fila_tabla += """
                        </tr>
            """


    return fila_tabla


def genera_contenido(MUNICIPIO, ACCION, NUM1,FECHA1,FOTO1, NUM2,FECHA2,FOTO2, NUM3,FECHA3,FOTO3, NUM4,FECHA4,FOTO4, NUM5,FECHA5,FOTO5,
                 NUM6,FECHA6,FOTO6, NUM7,FECHA7,FOTO7, NUM8,FECHA8,FOTO8, NUM9,FECHA9,FOTO9, NUM10,FECHA10,FOTO10,
                 NUM11,FECHA11,FOTO11, NUM12,FECHA12,FOTO12, NUM13,FECHA13,FOTO13, NUM14,FECHA14,FOTO14, NUM15,FECHA15,FOTO15,
                 NUM16,FECHA16,FOTO16, NUM17,FECHA17,FOTO17, NUM18,FECHA18,FOTO18, NUM19,FECHA19,FOTO19, NUM20,FECHA20,FOTO20,
                 NUM21,FECHA21,FOTO21, NUM22,FECHA22,FOTO22, NUM23,FECHA23,FOTO23, NUM24,FECHA24,FOTO24):

    validar_tabla = genera_tabla(NUM1,FECHA1,FOTO1, NUM2,FECHA2,FOTO2, NUM3,FECHA3,FOTO3, NUM4,FECHA4,FOTO4, NUM5,FECHA5,FOTO5,
                 NUM6,FECHA6,FOTO6, NUM7,FECHA7,FOTO7, NUM8,FECHA8,FOTO8, NUM9,FECHA9,FOTO9, NUM10,FECHA10,FOTO10,
                 NUM11,FECHA11,FOTO11, NUM12,FECHA12,FOTO12, NUM13,FECHA13,FOTO13, NUM14,FECHA14,FOTO14, NUM15,FECHA15,FOTO15,
                 NUM16,FECHA16,FOTO16, NUM17,FECHA17,FOTO17, NUM18,FECHA18,FOTO18, NUM19,FECHA19,FOTO19, NUM20,FECHA20,FOTO20,
                 NUM21,FECHA21,FOTO21, NUM22,FECHA22,FOTO22, NUM23,FECHA23,FOTO23, NUM24,FECHA24,FOTO24)
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;">""" + ACCION + """</p>
        """

    texto += """
                <div class "card-body" style = "margin: 0px; height:200px; overflow-y: scroll;">
                    <table class="table table-hover table-sm" style="font-family:sans-serif; font-size:9px;color:#FFFFFF; background-color:#D25B8A;">
                        <tr align=center>
                            <th>NUMERO DE SESIÓN</th>
                            <th>FECHA</th> 
                            <th>FOTO</th>  
                                  
                            <tbody> 
                            """ + validar_tabla + """
                            </tbody>
                    </table>
                </div>    
        """

    texto += """
                <div align = center>
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("DGCSJP") + """
                </div>
        </article>
            """
    return texto

def genera_contenidomesas_2022(MUNICIPIO, FECHA, DESCRIPCION, ASISTENTESH, ASISTENTESM, ASISTENTEST, FOTO1, FOTO2, VIDEO):
    FOTOS =[FOTO1, FOTO2]
    FECHA = FECHA.replace(" 00:00:00", "")
    texto = """
    <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i> """ + FECHA + """  </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-check-circle" style = "color:#FAC63A;"></i> """ + DESCRIPCION +"""</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-group" style = "color:#FAC63A;"></i><strong> TOTAL PERSONAS CAPACITADAS: </strong>""" + ASISTENTEST + """</p>
            """
    if ASISTENTESM != 0:
            texto+= """
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-female" style = "color:#FAC63A;"></i><strong> MUJERES: </strong>""" + ASISTENTESM + """</p>
                """
    if ASISTENTESH != 0:
            texto+= """           
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-male" style = "color:#FAC63A;"></i><strong> HOMBRES: </strong>""" + ASISTENTESH + """</p>

    """

    texto += """
                <div align = center>
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("DGCSJP") + """
                </div>
            </div>
        </article>
            """

    return texto

def genera_contenidocapacitaciones_2022(MUNICIPIO, FECHA, DESCRIPCION, ASISTENTEST, ASISTENTESM, ASISTENTESH, FOTO1, FOTO2, VIDEO):
    FECHA = FECHA.replace(" 00:00:00", "")
    texto = """
    <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i> """ + FECHA + """  </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-check-circle" style = "color:#FAC63A;"></i> """ + DESCRIPCION +"""</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-group" style = "color:#FAC63A;"></i><strong> TOTAL PERSONAS CAPACITADAS: </strong>""" + ASISTENTEST + """</p>
            """
    if ASISTENTESM != 0:
            texto+= """
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-female" style = "color:#FAC63A;"></i><strong> MUJERES: </strong>""" + ASISTENTESM + """</p>
                """
    if ASISTENTESH != 0:
            texto+= """           
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-male" style = "color:#FAC63A;"></i><strong> HOMBRES: </strong>""" + ASISTENTESH + """</p>


    """

    texto += """
                <div align = center>
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("DGCSJP") + """
                </div>
            </div>
        </article>
            """

    return texto


def tarjeta_genera_2023_2024(MUNICIPIO, FECHA, DESCRIPCION, ASISTENTESM, ASISTENTESH, ASISTENTEST, FOTO1, FOTO2, VIDEO):
    FECHA = FECHA.replace(" 00:00:00", "")
    texto = """
    <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i> """ + FECHA + """  </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-check-circle" style = "color:#FAC63A;"></i> """ + DESCRIPCION +"""</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-group" style = "color:#FAC63A;"></i><strong> TOTAL PERSONAS CAPACITADAS: </strong>""" + ASISTENTEST + """</p>
            """
    if ASISTENTESM != 0:
            texto+= """
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-female" style = "color:#FAC63A;"></i><strong> MUJERES: </strong>""" + ASISTENTESM + """</p>
                """
    if ASISTENTESH != 0:
            texto+= """           
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-male" style = "color:#FAC63A;"></i><strong> HOMBRES: </strong>""" + ASISTENTESH + """</p>


    """

    texto += """
                <div align = center>
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("DGCSJP") + """
                </div>
            </div>
        </article>
            """

    return texto
