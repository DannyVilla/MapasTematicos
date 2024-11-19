from RS import genera_rs

def highlight(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.7,
        'line_opacity': 0.7
    }


def genera_directorio(MUNICIPIO, OFICIAL, COORDINACION, DIRECCION, TELEFONO, CORREO):
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class ="fa fa-user" style = "color:#FAC63A;"></i><strong> NOMBRE DEL OFICIAL: </strong > """ + OFICIAL + """ </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class ="fa fa-institution" style = "color:#FAC63A;"></i><strong> COORDINACIÓN: </strong > """ + COORDINACION + """ </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-home" style = "color:#FAC63A;"></i><strong> DIRECCIÓN: </strong>""" + DIRECCION + """  </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-phone" style = "color:#FAC63A;"></i><strong> TELÉFONO: </strong>""" + TELEFONO + """  </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-envelope" style = "color:#FAC63A;"></i><strong> CORREO: </strong>""" + CORREO + """  </p>
    """

    texto += """
                <div align = center>
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("DGRC") + """
                </div>
            </div>
        </article>
    """

    return texto


def genera_total(MUNICIPIO,DIRECCION,TELEFONO,NACIMIENTO,MATRIMONIO,DIVORCIO,DEFUNCION,SENTENCIA,TOTAL,anio):
    texto = """    
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i><strong> ACTAS """ + anio + """ </strong></p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-home" style = "color:#FAC63A;"></i><strong> DIRECCIÓN: </strong>""" + DIRECCION + """  </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-phone" style = "color:#FAC63A;"></i><strong> TELÉFONO: </strong>""" + TELEFONO + """  </p>
    """

    texto += """           
                <table class="table table-hover table-sm " style=" font-family:sans-serif; font-size:9px;color:#FFFFFF; background-color:#D25B8A;">
                    <tr>
                        <td>ACTA DE NACIMIENTO</td>
                        <td>""" + NACIMIENTO + """</td>
                    </tr>

                    <tr>
                        <td>ACTA DE MATRIMONIO</td>
                        <td> """ + MATRIMONIO + """</td>
                    </tr>
                    
                    <tr>
                        <td>ACTA DE DIVORCIO</td>
                        <td>""" + DIVORCIO + """</td>
                    </tr>  
                                    
                    <tr>
                        <td>ACTA DE DEFUNCIÓN</td>
                        <td>""" + DEFUNCION + """</td>
                    </tr>
                   
                    <tr>
                        <td>ACTA DE SENTENCIA</td>
                        <td>""" + SENTENCIA + """</td>
                    </tr>
                    
                    <tr>
                        <td>TOTAL DE ACTAS</td>
                        <td>""" + TOTAL + """</td>
                    </tr>

                </table> 
        """

    texto += """
                <div align = center>
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("DGRC") + """
                </div>
            </div>
        </article>
    """

    return texto

def genera_datos(MUNICIPIO,MES,REGION,DIRECCION,TELEFONO,NACIMIENTO,MATRIMONIO,DIVORCIO,DEFUNCION,SENTENCIA,TOTAL):
    texto = """
    <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
                <div class="card-body">
                    <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                    <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-home" style = "color:#FAC63A;"></i><strong> DIRECCIÓN: </strong>""" + DIRECCION + """  </p>
                    <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-phone" style = "color:#FAC63A;"></i><strong> TELÉFONO: </strong>""" + TELEFONO + """  </p>
        """

    texto += """           
                    <table class="table table-hover table-sm " style=" font-family:sans-serif; font-size:9px;color:#FFFFFF; background-color:#D25B8A;">
                        <tr>
                            <td>ACTA DE NACIMIENTO</td>
                            <td>""" + NACIMIENTO + """</td>
                        </tr>

                        <tr>
                            <td>ACTA DE MATRIMONIO</td>
                            <td> """ + MATRIMONIO + """</td>
                        </tr>

                        <tr>
                            <td>ACTA DE DIVORCIO</td>
                            <td>""" + DIVORCIO + """</td>
                        </tr>  

                        <tr>
                            <td>ACTA DE DEFUNSIÓN</td>
                            <td>""" + DEFUNCION + """</td>
                        </tr>

                        <tr>
                            <td>ACTA DE SENTENCIA</td>
                            <td>""" + SENTENCIA + """</td>
                        </tr>

                        <tr>
                            <td>TOTAL DE ACTAS</td>
                            <td>""" + TOTAL + """</td>
                        </tr>

                    </table> 
            """

    texto += """
                    <div align = center>
                        <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("DGRC") + """
                    </div>
                </div>
            </article>
        """

def genera_brigadas(ID, MUNICIPIO,FECHA,BENEFICIARIOS, COLOR):
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-home" style = "color:#FAC63A;"></i><strong> FECHA: </strong>""" + FECHA+ """  </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-group" style = "color:#FAC63A;"></i><strong> BENEFICIARIOS: </strong>""" + BENEFICIARIOS + """  </p>
        """

    texto += """
                <div align = "center">
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("DGRC") + """
                </div>
            </div>
        </article>
        """

    return texto
