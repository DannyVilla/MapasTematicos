import numpy as np
from RS import genera_rs

def highlight(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.7,
        'line_opacity': 0.7
    }

def genera_tarjeta(MUNICIPIO, PROGRAMA, BENEFICIADOS, CLASIFICACION, PRODUCTO, FOTO1, FOTO2, anio):
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body" >
                <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-group" style = "color:#FAC63A;"></i><strong> BENEFICIADOS: </strong>"""+ BENEFICIADOS +""" </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-list" style = "color:#FAC63A;"></i><strong> CLASIFICACIÓN: </strong>""" + CLASIFICACION +"""</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-check-circle" style = "color:#FAC63A;"></i><strong> PROGRAMA: </strong>""" + PROGRAMA +"""</p>
        """

    texto += """
        <div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
            <div class="carousel-inner">    
    """

    if FOTO1 != "0" and FOTO1 != 0:
        texto += """            
                   
                            <div class="carousel-item active" align = center>                            
                                <img src='""" + FOTO1 + """' width='250' height='180' </img>
                            </div> 

          """


    if FOTO2 != "0" and FOTO2 != 0:
        texto += """            
            <div class="carousel-item" align = center>                            
                <img src='""" + FOTO2 + """' width='280' height='180' </img>
            </div>
        """

    if FOTO1 != "0" and FOTO2 != "0":

        texto += """
                </div>
                  <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="sr-only">Previous</span>
                  </a>
                  <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="sr-only">Next</span>
                  </a>     
        """
    texto += """
            <p style="color:#FFFFFF; font-size:11px; margin: 0px; font-family:sans-serif;"><strong>PRODUCTO: </strong>""" + PRODUCTO + """</p>

    """

    texto += """</div>
            <div align = center><p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("SIOP") + """</div>
        </article>
        """

    return texto
