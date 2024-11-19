from RS import genera_rs
def highlight(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.7,
        'line_opacity': 0.7
    }

def tarjeta_contenido(MUNICIPIO,JURISDICCION,DIRECCION,DELEGADO,TEL,FOTO):
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center" style="color:#FFFFFF; margin: 0px;"><span class="badge badge-danger"><i class=" fa fa-map-marker" style = "color:#FAC63A;"></i><strong> Jurisdicción: <br></strong>""" + JURISDICCION + """ </span></br></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class ="fa fa-user" style = "color:#FAC63A;"></i><strong> DELEGADO: </strong > """ + DELEGADO + """ </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-home" style = "color:#FAC63A;"></i><strong> DIRECCIÓN: </strong>""" + DIRECCION + """  </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-phone" style = "color:#FAC63A;"></i><strong> TELÉFONO: </strong>""" + TEL + """  </p>
                <p style="color:#FFFFFF; margin: 0px;"><strong> MUNICIPIOS: </strong>""" + MUNICIPIO + """</p>

                    <div align = "center">
                        <img src='""" + FOTO + """' width='130' height='160' />
                    </div> 
        """


    texto += """            
                <div align = "center">
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("CCLV") + """
                </div>
            </div>
        </article>

    
    """

    return texto


