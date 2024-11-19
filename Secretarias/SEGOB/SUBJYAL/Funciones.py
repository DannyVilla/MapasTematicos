from RS import genera_rs

def highlight(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.7,
        'line_opacity': 0.7
    }

def genera_tabla(ACCION1,ACCION2,TOTAL):
    fila_tabla = " "
    if ACCION1 != "0":
        fila_tabla += """           
                    <tr>
                        <td> Atención Ciudadana </td>
                        <td><p style="color:#FFFFFF; margin: 0px;">""" + ACCION1 + """</p></td>
                    </tr>
            """
    if ACCION2 != "0":
        fila_tabla += """           
                    <tr>
                        <td> Invitación para Adhesión al Acuerdo Veracruz por la Democracia </td>
                        <td><p style="color:#FFFFFF; margin: 0px;">""" + ACCION2 + """</p></td>
                    </tr>
            """
    if TOTAL != "0":
        fila_tabla += """           
                    <tr>
                        <td> Total </td>
                        <td><p style="color:#FFFFFF; margin: 0px;">""" + TOTAL + """</p></td>
                    </tr>
            """
    return fila_tabla

def genera_tarjeta(MUNICIPIO, ACCION1, ACCION2,TOTAL):

    validar_tabla = genera_tabla(ACCION1,ACCION2,TOTAL)

    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>

        """

    texto+= """
                <table id=defunciones class="table table-hover table-sm " style="font-family:sans-serif; font-size:9px;color:#FFFFFF; background-color:#D25B8A;">
                        <tbody> 
                        """ + validar_tabla + """
                        </tbody>
                </table>    
    """

    texto += """
                <div align = center>
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("SUBJYAL") + """
                </div>
            </div>
        </article>
    """
    return texto