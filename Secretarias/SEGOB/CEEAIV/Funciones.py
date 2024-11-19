from RS import genera_rs


def highlight(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.7,
        'line_opacity': 0.7
    }

def genera_tabla(ASESORIA, PRIMER, PSICOLOGICA, REGISTROS, DICTAMENES):
    fila_tabla = " "
    if ASESORIA != "0":
        fila_tabla += """           
                    <tr>
                        <td>Asesoría Jurídica</td>
                        <td align = "center">""" + ASESORIA + """</td>
                    </tr>
            """

    if PRIMER != "0":
        fila_tabla += """           
                    <tr>
                        <td>Primer Contacto</td>
                        <td align = "center">""" + PRIMER + """</td>
                    </tr>
            """
    if PSICOLOGICA != "0":
        fila_tabla += """           
                    <tr>
                        <td>Atención Psicológica</td>
                        <td align = "center">""" + PSICOLOGICA + """</td>
                    </tr>
            """
    if REGISTROS != "0":
        fila_tabla += """           
                    <tr>
                        <td>Registros</td>
                        <td align = "center">""" + REGISTROS + """</td>
                    </tr>
            """
    if DICTAMENES != "0":
        fila_tabla += """           
                    <tr>
                        <td>Dictámenes</td>
                        <td align = "center">""" + DICTAMENES + """</td>
                    </tr>
            """

    return fila_tabla

def genera_actividades(MUNICIPIO, ASESORIA, PRIMER, PSICOLOGICA, REGISTROS, DICTAMENES, BENEFICIADOS, APOYOS1, APOYOS2, anio):

    validar_tabla = genera_tabla(ASESORIA, PRIMER, PSICOLOGICA, REGISTROS, DICTAMENES)

    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i><strong> ACCIONES """+ anio +""" </strong></p>
        """
    if BENEFICIADOS != "0":
            texto += """
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-group" style = "color:#FAC63A;"></i><strong> COMITÉ INTERDISCIPLINARIO - BENEFICIADOS: """+ BENEFICIADOS +""" </strong></p>
            """
    if APOYOS1 != "0":
            texto += """
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-cubes" style = "color:#FAC63A;"></i><strong> COMITÉ INTERDISCIPLINARIO - APOYOS: """+ APOYOS1 +""" </strong></p>
            """
    if APOYOS2 != "0":
            texto += """
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-cubes" style = "color:#FAC63A;"></i><strong> ATENCIÓN PSICOLÓGICA - APOYOS: """+ APOYOS2 +""" </strong></p>
            """

    texto += """
                <table id=defunciones class="table table-hover table-sm " style="font-family:sans-serif; font-size:9px;color:#FFFFFF; background-color:#D25B8A;">
                    <tr align = "center">
                        <th>ACCIÓN</th>
                        <th>NO.</th>
                    </tr>
                    
                    <tbody> 
                        """ + validar_tabla + """
                    </tbody>
                    
                </table>    
        """

    texto += """
                <div align = center>
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("CEEAIV") + """
                </div>
            </div>
        </article>
        """

    return texto


def genera_tabla_2023(ASESORIA, PRIMER_B, PRIMER_A, TRABAJO_B, TRABAJO_A, PSICOLOGICA_B, PSICOLOGICA_A, REGISTROS_B, REGISTROS_A,
                            COMITÉ_B, COMITÉ_A):
    fila_tabla = " "
    if ASESORIA != "0":
        fila_tabla += """           
                    <tr>
                        <td>Asesoría Jurídica</td>
                        <td align = "center">""" + ASESORIA + """</td>
                        <td align = "center">""" + ASESORIA + """</td>
                    </tr>
            """

    if PRIMER_A != "0":
        fila_tabla += """           
                    <tr>
                        <td>Primer Contacto</td>
                        <td align = "center">""" + PRIMER_A + """</td>
                        <td align = "center">""" + PRIMER_B + """</td>
                    </tr>
            """

    if TRABAJO_A != "0":
        fila_tabla += """           
                    <tr>
                        <td>Trabajo Social</td>
                        <td align = "center">""" + TRABAJO_A + """</td>
                        <td align = "center">""" + TRABAJO_B + """</td>
                    </tr>
            """

    if PSICOLOGICA_A != "0":
        fila_tabla += """           
                    <tr>
                        <td>Atención Psicológica </td>
                        <td align = "center">""" + PSICOLOGICA_A + """</td>
                        <td align = "center">""" + PSICOLOGICA_B + """</td>
                    </tr>
            """

    if REGISTROS_A != "0":
        fila_tabla += """           
                    <tr>
                        <td>Registros </td>
                        <td align = "center">""" + REGISTROS_A + """</td>
                        <td align = "center">""" + REGISTROS_B + """</td>
                    </tr>
            """

    if COMITÉ_A != "0":
        fila_tabla += """           
                    <tr>
                        <td>Comité Interdisciplinario</td>
                        <td align = "center">""" + COMITÉ_A + """</td>
                        <td align = "center">""" + COMITÉ_B + """</td>
                    </tr>
            """

    return fila_tabla


def genera_actividades_2023_2024(MUNICIPIO, ASESORIA, PRIMER_B, PRIMER_A, TRABAJO_B, TRABAJO_A, PSICOLOGICA_B, PSICOLOGICA_A, REGISTROS_B, REGISTROS_A,
                            COMITÉ_B, COMITÉ_A, anio):

    validar_tabla = genera_tabla_2023(ASESORIA, PRIMER_B, PRIMER_A, TRABAJO_B, TRABAJO_A, PSICOLOGICA_B, PSICOLOGICA_A, REGISTROS_B, REGISTROS_A,
                            COMITÉ_B, COMITÉ_A)

    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i><strong> ACCIONES """ + anio + """ </strong></p>

            """


    texto += """
                <table id=defunciones class="table table-hover table-sm " style="font-family:sans-serif; font-size:9px;color:#FFFFFF; background-color:#D25B8A;">
                    <tr align = "center">
                        <th>ACCIÓN</th>
                        <th>APOYOS.</th>
                        <th>BENEFICIARIOS.</th>
                    </tr>

                    <tbody> 
                        """ + validar_tabla + """
                    </tbody>

                </table>    
        """

    texto += """
                <div align = center>
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("CEEAIV") + """
                </div>
            </div>
        </article>
        """

    return texto


def genera_oficinas(municipio, tel, direccion, foto):
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + municipio + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-home" style = "color:#FAC63A;"></i><strong> DIRECCIÓN: </strong>""" + direccion + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-phone" style = "color:#FAC63A;"></i><strong> TEL: </strong>""" + tel + """</p>"""

    if foto != "0":
        texto += """<img src = '""" + foto + """' width = '250' height = '180' /> """

    texto += """
                <div align = center>
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("CEEAIV") + """
                </div>
            </div>
        </article>
            """
    return texto
