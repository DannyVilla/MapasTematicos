import pandas as pd


def genera_rs(dep):
    rs_dep = pd.read_excel("C:\ESyP\Mapas_COESPO\MapasTematicos\Redes_Sociales.xlsx", sheet_name='datos')
    #rs_dep = pd.read_excel("/Users/4x/COESPOAX/MapasTematicos/Redes_Sociales.xlsx", sheet_name='datos')

    in_dep = rs_dep['SIGLA'] == dep
    rs = rs_dep[in_dep]

    texto = """
                   <div> """
    for row in rs.itertuples():
        if str(row.WEB) != '0':
            texto += """<a class="navbar-brand" target=_blank href='""" + str(row.WEB) + """'>
                    <img alt="Brand" src="images/""" + dep + """.png" width="30" height="30">
                  </a>"""
        if str(row.FACEBOOK) != '0':
            texto += """<a class="navbar-brand" target=_blank href='""" + str(row.FACEBOOK) + """'>
                    <img alt="Brand" src="images/fb3.png" width="30" height="30">
                  </a>"""
        if str(row.TWITTER) != '0':
            texto += """<a class="navbar-brand" target=_blank href='""" + str(row.TWITTER) + """'>
                <img alt="Brand" src="images/tw3.png" width="30" height="30">
              </a>"""
        if str(row.YOUTUBE) != '0':
            texto += """<a class="navbar-brand" target=_blank href='""" + str(row.YOUTUBE) + """'>
                <img alt="Brand" src="images/y3.png" width="30" height="30">
              </a>"""
        if str(row.INSTAGRAM) != '0':
            texto += """<a class="navbar-brand" target=_blank href='""" + str(row.INSTAGRAM) + """'>
                    <img alt="Brand" src="images/i3.png" width="30" height="30">
                  </a>"""

        texto += """
        </div>
        """

    return texto
