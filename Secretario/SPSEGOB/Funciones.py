def content_directorio(NOMBRE, AREA, CARGO, NIVEL):
    texto2 = """
            <div class="article" style="width: 18rem; font-family:sans-serif; font-size:12px;color:#FFFFFF; background-color:#9880b9;">
              <div class="card-body">
                <h5 align = "center"><span class="badge badge-light">""" + NOMBRE + """</span></h5>
                <p style= "color:#FFFFFF;" "font-family:roboto; font-size:9px;><strong>Área: </strong>""" + AREA + """</p>
                <p style= "color:#FFFFFF;" "font-family:roboto; font-size:9px;><strong>Cargo: </strong>""" + CARGO + """</p>
                <p style= "color:#FFFFFF;" "font-family:roboto; font-size:9px;><strong>Nivel Jerárquico: </strong>""" + NIVEL + """</p>
              </div>
            </div>
    """

    return texto2
