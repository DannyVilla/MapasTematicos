from RS import genera_rs

def highlight(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.7,
        'line_opacity': 0.7
    }

def genera_tarjeta(MUNICIPIO, BENEFICIADOS, APOYOS, PROGRAMA, FOTO, VIDEO, ANIO):
    texto = """
    <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
           <div class="card-body">
              <h5 align ="center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
              <h6 align = "center"><span class="badge badge-light">Acción del Año """ + ANIO + """</span></h6>
              <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-cubes" style = "color:#FAC63A;"></i><strong>APOYOS: </strong>""" + APOYOS + """ </p> 
              <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-group" style = "color:#FAC63A;"></i><strong>BENEFICIADOS: </strong>""" + BENEFICIADOS + """ </p>               
              <p style="color:#FFFFFF; margin: 0px;"><strong>PROGRAMA: </strong>""" + PROGRAMA + """</p>
        """
    if FOTO != "0":
        texto += """<div align = "center">
                        <img src='""" + FOTO + """' width='250' height='180'/>
                    </div>                        
    """
    if VIDEO != "0":
        texto += VIDEO

    texto += """<div align = center><p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("DIF") + """</div>
        </article>
        """

    return texto
