

def content_tarjeta(MUNICIPIO, BENEFICIADOS, ACCION, APOYO, FOTO):
    texto = """
        <article class="popup" style="width: 400px;background-color:#39395B;border-radius: 5px; padding:20px; text-overflow: ellipsis;">
            <div align=center><h4><span class="label label-primary">""" + MUNICIPIO + """</span></h2><div>
            <div class='h5 text-left' id='pageHeaderTitle' style="color:#FFFFFF;font-family:sans-serif;"><strong>ACCIÓN: </strong>""" + ACCION + """</div>"""
    if BENEFICIADOS != "0":
        texto += """<div class='h5 text-left' id='pageHeaderTitle' style="color:#FFFFFF;font-family:sans-serif;"><strong>BENEFICIADOS: </strong>""" + BENEFICIADOS + """</div>"""
    #print(APOYO)
    if APOYO != "0":
        texto += """
        <div class='h5 text-left' id='pageHeaderTitle' 
        style="color:#FFFFFF;font-family:sans-serif;"><strong>APOYO: </strong>""" + APOYO + """</div> """
    if FOTO != "0":
        # texto += """<img src='""" + FOTO + """' width='90%' height='90%'/>"""
        texto += """<div><a href='""" + FOTO + """' target="_blank"><i class="glyphicon glyphicon-camera" style="font-size:21px;color:#FFFFFF;"></i></a></div>"""

    texto += """
    <div class="panel-body">
    <p style="color:white">Más información:
            """

    texto += genera_rs("IVJ") + """
    </div>
    </article>
    """

    return texto

