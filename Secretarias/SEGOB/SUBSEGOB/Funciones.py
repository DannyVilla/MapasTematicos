from RS import genera_rs

def highlight(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.7,
        'line_opacity': 0.7
    }

def tarjeta_peticiones(row):
    texto = """
            <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + str(row.MUNICIPIO) + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i><strong> ACCIONES 2021 </strong></P>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-check-square" style = "color:#FAC63A;"></i><strong> PETICIONES CIUDADANAS ATENDIDAS: </strong>""" + str(row.CANTIDAD) + """  </p>
            """

    texto += """            
                        <div align = center>
                            <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("SUBSEGOB") + """
                        </div>
                </div>
            </article>
        """

    return texto

def tarjeta_peticiones_2022(row):
    texto = """
            <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + str(row.MUNICIPIO) + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i><strong> ACCIONES 2022 </strong></P>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-check-square" style = "color:#FAC63A;"></i><strong> PETICIONES CIUDADANAS ATENDIDAS: </strong>""" + str(row.CANTIDAD) + """  </p>
            """

    texto += """            
                        <div align = center>
                            <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("SUBSEGOB") + """
                        </div>
                </div>
            </article>
        """

    return texto

def tarjeta_peticiones_2023(row):
    texto = """
            <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + str(row.MUNICIPIO) + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i><strong> ACCIONES 2023 </strong></P>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-check-square" style = "color:#FAC63A;"></i><strong> PETICIONES CIUDADANAS ATENDIDAS: </strong>""" + str(row.CANTIDAD) + """  </p>
            """

    texto += """            
                        <div align = center>
                            <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("SUBSEGOB") + """
                        </div>
                </div>
            </article>
        """

    return texto

def tarjeta_peticiones_2024(row):
    texto = """
            <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + str(row.MUNICIPIO) + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i><strong> ACCIONES 2024 </strong></P>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-check-square" style = "color:#FAC63A;"></i><strong> PETICIONES CIUDADANAS ATENDIDAS: </strong>""" + str(row.CANTIDAD) + """  </p>
            """

    texto += """            
                        <div align = center>
                            <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("SUBSEGOB") + """
                        </div>
                </div>
            </article>
        """

    return texto



