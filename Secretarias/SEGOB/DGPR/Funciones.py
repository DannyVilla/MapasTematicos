from RS import genera_rs


def content_tarjeta_old(zona, delegacion, delegado, oficina, celular, dir, mpios_aten, foto):
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <div align=center><h4><span class="label label-primary">""" + zona + """</span></h2><div>
                <div align=center><h4><span class="label label-primary">""" + delegacion + """</span></h2><div>
                <p style="color:#FFFFFF; margin: 0px;"><i class ="fa fa-user" style = "color:#FAC63A;"></i><strong> DELEGADO: </strong > """ + delegado + """ </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-home" style = "color:#FAC63A;"></i><strong> DIRECCIÓN: </strong>""" + dir + """  </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-phone" style = "color:#FAC63A;"></i><strong> TELÉFONO: </strong>""" + oficina + """  </p>
                <p style="color:#FFFFFF; margin: 0px;"><strong>MUNICIPIOS ATENDIDOS: </strong>""" + mpios_aten + """</p>"""

    if ".jpg" in foto:

        texto += """<img src='""" + foto + """' width='90%' height='90%'/>"""
    else:
        texto += """<div><a href='""" + foto + """' target="_blank"><i class="glyphicon glyphicon-camera" style="font-size:21px;color:#FFFFFF;"></i></a></div>"""

    return texto


def content_tarjeta(zona, delegacion, delegado, oficina, celular, dir, mpios_aten, foto):
    if ".jpg" in foto:
        img = """ <img src = '""" + foto + """' width = '120' height = '140'></img> """
    else:
        foto = "images/user2.png"
        img = """ <img src = '""" + foto + """' width = '120' height = '140'></img> """

    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
            <h5 align = "center"><span class="badge badge-danger">""" + zona + """</span></h5>
            <h5 align = "center"><span class="badge badge-danger">""" + delegacion + """</span></h5>
            <table id=delegado class="table table-condensed" style="font-family:sans-serif; font-size:12px;color:#FFFFFF; background-color:#900C3F;"> 
                    <tr >
                        <td rowspan="3" align="center">""" + img + """</td>
                        <td><p style="color:#FFFFFF; margin: 0px;"><i class ="fa fa-user" style = "color:#FAC63A;"></i>""" + delegado + """</p></td>
                    </tr>
                    <tr>
                        <td><p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-phone" style = "color:#FAC63A;"></i> Oficina: """ + oficina + """</p></td>
                    <tr>
                        <td><p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-phone" style = "color:#FAC63A;"></i> Celular: """ + celular + """</p></td>
                    </tr>
                    <tr>
                        <td colspan="2"><p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-home" style = "color:#FAC63A;"></i> Dirección: """ + dir + """</p></td>
                    </tr>
                    <tr>
                      <td colspan="2">Municipios Atendidos: """ + mpios_aten + """</td>
                    </tr>
                    <tr>
                      <td colspan="2" align = "center"> Actualización 01 Septiembre 2022</td>
                    </tr>
      
                </table>"""
    texto += """            
                <div align = "center">
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("DGPR") + """
                </div>
            </div>
        </article>
    """

    return texto


def content_representantes(zona, delegacion, representante, oficina, celular, dir, foto, delegaciones):
    if ".jpg" in foto:
        img = """ <img src = '""" + foto + """' width = '120' height = '140'></img> """
    else:
        foto = "images/user2.png"
        img = """ <img src = '""" + foto + """' width = '120' height = '140'></img> """

    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
            <h5 align = "center"><span class="badge badge-danger">""" + zona + """</span></h5>
            <h5 align = "center"><span class="badge badge-danger">""" + delegacion + """</span></h5>
            <table id=delegado class="table table-condensed" style="font-family:sans-serif; font-size:12px;color:#FFFFFF; background-color:#900C3F;"> 
                <tr >
                    <td rowspan="3" align="center">""" + img + """</td>
                    <td><p style="color:#FFFFFF; margin: 0px;"><i class ="fa fa-user" style = "color:#FAC63A;"></i>""" + representante + """</p></td>
                </tr>
                <tr>
                    <td><p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-phone" style = "color:#FAC63A;"></i> Oficina: """ + oficina + """</p></td>
                <tr>
                    <td><p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-phone" style = "color:#FAC63A;"></i> Celular: """ + celular + """</p></td>
                </tr>
                <tr>
                    <td colspan="2"><p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-home" style = "color:#FAC63A;"></i> Dirección: """ + dir + """</p></td>
                </tr>
                <tr>
                  <td colspan="2">Delegaciones Atendidas: """ + delegaciones + """</td>
                </tr>
                <tr>
                      <td colspan="2" align = "center"> Actualización 01 Septiembre 2022</td>
                </tr>
            </table>"""
    texto += """            
                <div align = "center">
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("DGPR") + """
                </div>
            </div>
        </article>
    """

    return texto


def content_directorio(nombre, puesto, telefono, dir, foto):
    if ".jpg" in foto:
        img = """ <img src = '""" + foto + """' width = '120' height = '140'></img> """
    else:
        foto = "images/user2.png"
        img = """ <img src = '""" + foto + """' width = '120' height = '140'></img> """

    texto = """    
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
            <h5 align = "center"><span class="badge badge-danger">""" + nombre + """</span></h5>
            <table id=delegado class="table table-condensed" style="font-family:sans-serif; font-size:12px;color:#FFFFFF; background-color:#900C3F;"> 
                <tr >
                    <td rowspan="2" align="center">""" + img + """</td>
                    <td>Puesto: """ + puesto + """</td>
                </tr>
                <tr>
                    <td><p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-phone" style = "color:#FAC63A;"></i> Teléfono: """ + telefono + """</p></td>
                </tr>
                <tr>
                    <td colspan="2"><p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-home" style = "color:#FAC63A;"></i> Dirección: """ + dir + """</p></td>
                </tr>
                <tr>
                      <td colspan="2" align = "center"> Actualización 01 Septiembre 2022</td>
                </tr>
            </table>"""
    texto += """            
                <div align = "center">
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("DGPR") + """
                </div>
            </div>
        </article>
    """

    return texto
