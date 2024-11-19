from RS import genera_rs

def highlight(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.7,
        'line_opacity': 0.7
    }

def content_capacitaciones(MUNICIPIO,TEMA,H,M,T):
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h6 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h6>
                <p style= "color:#FFFFFF; margin: 0px;"><strong>Tema: </strong>""" + TEMA + """</p>
                <table id=defunciones class="table table-hover table-sm " style="font-family:sans-serif; font-size:9px;color:#FFFFFF; background-color:#D25B8A;">
                <tr>
                    <td align = "center">
                        <p style= "color:#FFFFFF; margin: 0px;"><strong>Hombres: </strong>""" + H + """</p>
                    </td>                
                </tr>
                <tr>
                    <td align = "center">
                        <p style= "color:#FFFFFF; margin: 0px;"><strong>Mujeres: </strong>""" + M + """</p>
                    </td>                
                </tr> 
                <tr>
                    <td align = "center">
                        <p style= "color:#FFFFFF; margin: 0px;"><strong>Totales: </strong>""" + T + """</p>
                    </td>                
                </tr>
                </table>
             
        """

    texto += """<div align = "center">
                    <p style= "margin:0px;color:white;">Más información: </p> """ + genera_rs("SSP") + """
                </div>
            </div>  
        </article>
                
        """

    return texto

def content_tarjeta(MUNICIPIO, DIRECCION, TEL, FOTO):
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h6 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h6>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-home" style = "color:#FAC63A;"></i><strong> DIRECCIÓN: </strong>""" + DIRECCION + """  </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-phone" style = "color:#FAC63A;"></i><strong> TELÉFONO: </strong>""" + TEL + """  </p>
    """

    if ".jpg" in FOTO:
        texto += """
                <div align = "center">            
                    <img align  = "center" src='""" + FOTO + """' width='250' height='180'/>                    
                    <p style= "margin:0px;color:white;">Más información: </p> """ + genera_rs("SSP") + """                   
                </div>
            """
    else:
        texto += """<div align = "center">
                        <a href='""" + FOTO + """' target="_blank"><i class="fa fa-camera" style="font-family:sans-serif;font-size:11px;color:#FFFFFF;"></i></a>
                         <p style= "margin:0px;color:white;">Más información: </p> """ + genera_rs("SSP") + """
                    </div>              
                   
            """
        texto += """                
            </article>
            """
    return texto


def content_licencias(MUNICIPIO, DIRECCION, TEL, FOTO):
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h6 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h6>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-home" style = "color:#FAC63A;"></i><strong> DIRECCIÓN: </strong>""" + DIRECCION + """  </p>
            """
    if TEL != "0":
        texto += """
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-phone" style = "color:#FAC63A;"></i><strong> TELÉFONO: </strong>""" + TEL + """  </p>
            """
    if ".jpg" in FOTO:
        texto += """
                <div align = "center">
                    <img src='""" + FOTO + """' width='250' height='180'>
                    <p style= "margin:0px;color:white;">Más información: </p> """ + genera_rs("SSP") + """
                </div>    
                
        """
    else:
        texto += """<div align = "center">
                        <a href='""" + FOTO + """' target="_blank"><i class="fa fa-camera"></i></a>
                        <p style= "margin:0px;color:white;">Más información: </p> """ + genera_rs("SSP") + """
                    </div>
                    
            """
    return texto

def genera_acciones_2022(MUNICIPIO, TEXTO, FECHA, CLASIFICACION, FOTO1):
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h6 align = "center" ><span class="badge badge-danger">""" + MUNICIPIO + """</span></h6>
                <p style= "color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i>""" + FECHA + """</p>
                <p style= "color:#FFFFFF; margin: 0px;">""" + TEXTO + """</p>

        """
    if FOTO1 != "0":
        texto += """                        
                       """ + FOTO1 + """              
        """

    texto += """
                    <div align = "center">
                         <p style= "margin:0px;color:white;">Más información: </p> """ + genera_rs("SSP") + """
                    </div>
                </div>
        </article>
        """
    return texto
