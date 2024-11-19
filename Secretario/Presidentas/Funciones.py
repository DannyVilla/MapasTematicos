def content_directorio(nombre, partido, foto, region,municipio):
    if ".jpg" in foto:
        #img = """ <img src = '""" + foto + """' width = '170' height = '170'></img> """
        img = """ <img class="card-img-top" src= '""" + foto + """' width = '170' height = '170' alt=""> """

    else:
        foto = "images/user2.png"
        img = """ <img src = '""" + foto + """' width = '170' height = '170'></img> """

    texto = """
        <article style="width: 300px;background-color:#C6046B;border-radius: 5px; padding:20px; text-overflow: ellipsis;">
        <div align=center><h4><span class="label label-primary">""" + nombre + """</span></h2><div>
        <table id=delegado class="table table-condensed" style="font-family:sans-serif; font-size:12px;color:#FFFFFF; background-color:#9880b9;">
                <tr >
                    <td rowspan="3" align="center">""" + img + """</td>
                    <td>Partido: """ + partido + """</td>
                </tr>
                                
                <tr>
                    <td colspan="2">Región: """ + region + """</td>
                </tr>
               
            </table>"""
    #<h6 class="card-title">"""+ nombre +"""</h6> <p class="card-text">Partido: """+ partido +"""</p>
    texto2 = """
            <div class="card" style="width: 12rem; font-family:sans-serif; font-size:11px;color:#FFFFFF; background-color:#9880b9;">
              """+ img +"""
              <div class="card-body">
                <strong>"""+ nombre +"""</strong><br>
                Municipio: """+ municipio +"""
                <br>Partido: """+ partido +"""
              </div>
            </div>
    """

    return texto2
