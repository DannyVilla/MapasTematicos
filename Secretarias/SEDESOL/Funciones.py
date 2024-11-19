from RS import genera_rs

def highlight(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.7,
        'line_opacity': 0.7
    }


def genera_tarjeta(DISTRITO, MUNICIPIO, U_SOC, DIAGNOSTICOS, JUEGOS, A_MUJE, B_MUJE, A_AUTO, B_AUTO, A_PROG, B_PROG,
                   A_PISO, B_PISO, A_TECH, B_TECH, A_MURO, B_MURO, A_CUAR, B_CUAR, A_ESTU, B_ESTU, A_ELEC, B_ELEC):
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i>ACCIONES 2020</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-home" style = "color:#FAC63A;"></i><strong> DISTRITO: </strong>""" + DISTRITO + """  </p>
        """
    if U_SOC != "0" or DIAGNOSTICOS != "0" or JUEGOS != "0":
        texto += """
            <table class="table table-hover table-sm " style="font-family:sans-serif; font-size:9px;color:#FFFFFF; background-color:#D25B8A;">

                <tr align=center>
                    <th>DESCRIPCIÓN</th>
                    <th>BENEFICIARIOS</th>
                </tr>"""
        if U_SOC != "0":
            texto += """<tr align=center>
                                <td>Unidades Sociales del Bienestar</td>
                                <td>""" + U_SOC + """</td>
                            </tr>
                         """
        if DIAGNOSTICOS != "0":
            texto += """<tr align=center>
                                <td>Diagnósticos Comunitarios</td>
                                <td>""" + DIAGNOSTICOS + """</td>
                            </tr>
                         """

        if JUEGOS != "0":
            texto += """<tr align=center>
                               <td>Juegos Infantiles</td>
                               <td>""" + JUEGOS + """</td>
                           </tr>
                    """
        texto += """
            </table>
            """
    if A_MUJE != "0" or B_MUJE != "0" or A_AUTO != "0" or B_AUTO != "0" or A_PROG != "0" or B_PROG != "0" or A_PISO != "0" or B_PISO != "0" or A_TECH != "0" or B_TECH != "0" or A_MURO != "0" or B_MURO != "0" or A_CUAR != "0" or B_CUAR != "0" or A_ESTU != "0" or B_ESTU != "0" or A_ELEC != "0" or B_ELEC != "0":
        texto += """
                <table class="table table-hover table-sm " style="font-family:sans-serif; font-size:9px;color:#FFFFFF; background-color:#D25B8A;">
                    <tr align=center>
                        <th>DESCRIPCIÓN</th>
                        <th>APOYOS</th>
                        <th>BENEFICIARIOS</th>
                    </tr>"""
        if A_MUJE != "0":
            texto += """
                <tr align=center>
                            <td>Programa Mujeres Emprendedoras</td>
                            <td>""" + A_MUJE + """</td>
                            <td>""" + B_MUJE + """</td>
                        </tr>
                """
        if A_AUTO != "0":
            texto += """
                    <tr align=center>
                            <td>Programa Módulos Hacia la Autosuficiencia Alimentaria</td>
                            <td>""" + A_AUTO + """</td>
                            <td>""" + B_AUTO + """</td>
                        </tr>
            """
        if A_PROG != "0":
            texto += """
                <tr align=center>
                            <td>Programa Emergente</td>
                            <td>""" + A_PROG + """</td>
                            <td>""" + B_PROG + """</td>
                        </tr>
                """
        if A_PISO != "0":
            texto += """
                <tr align=center>
                            <td>Pisos</td>
                            <td>""" + A_PISO + """</td>
                            <td>""" + B_PISO + """</td>
                </tr>
            """
        if A_TECH != "0":
            texto += """
            <tr align=center>
                            <td>Techos</td>
                            <td>""" + A_TECH + """</td>
                            <td>""" + B_TECH + """</td>
                        </tr>
            """
        if A_MURO != "0":
            texto += """
                <tr align=center>
                            <td>Muros</td>
                            <td>""" + A_MURO + """</td>
                            <td>""" + B_MURO + """</td>
                        </tr>
            """
        if A_CUAR != "0":
            texto += """
                    <tr align=center>
                            <td>Cuartos dormitorios</td>
                            <td>""" + A_CUAR + """</td>
                            <td>""" + B_CUAR + """</td>
                        </tr>
            """
        if A_ESTU != "0":
            texto += """
                    <tr align=center>
                            <td>Estufas Ecológicas</td>
                            <td>""" + A_ESTU + """</td>
                            <td>""" + B_ESTU + """</td>
                        </tr>
            """
        if A_ELEC != "0":
            texto += """
                    <tr align=center>
                            <td>Electrificación</td>
                            <td>""" + A_ELEC + """</td>
                            <td>""" + B_ELEC + """</td>
                        </tr>
            """
        texto += """
                    </table>
                    """

    # cierre de toda la tarjeta
    texto += """            
                <div align = "center">
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("SEDESOL") + """
                </div>
            </div>
        </article>
    """

    return texto


def genera_tarjeta_programa(MUNICIPIO, ME_Acciones, ME_Beneficiarios, MAA_Acciones, MAA_Beneficiarios, MAG_Acciones, MAG_Beneficiarios, MHI_Acciones, MHI_Beneficiarios, Pisos,
                   Pisos_Beneficiarios, Techos, Techos_Beneficiarios, Cuartos_Dormitorios, Cuartos_Beneficiarios, Estufas_ecológicas, Estufas_Beneficiarios, Sanitarios, Sanitarios_Beneficiarios):
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i>ACCIONES 2022</p>
        """

    if ME_Acciones != "0" or ME_Beneficiarios != "0" or MAA_Acciones != "0" or MAA_Beneficiarios != "0" or MAG_Acciones != "0" or MAG_Beneficiarios != "0" or MHI_Acciones != "0" or MHI_Beneficiarios != "0" or Pisos != "0"\
            or Pisos_Beneficiarios != "0" or Techos != "0" or Techos_Beneficiarios != "0" or Cuartos_Dormitorios != "0" or Cuartos_Beneficiarios != "0" or Estufas_ecológicas != "0" or Estufas_Beneficiarios != "0" or Sanitarios != "0" or Sanitarios_Beneficiarios != "0":
        texto += """
                <table class="table table-hover table-sm " style="font-family:sans-serif; font-size:9px;color:#FFFFFF; background-color:#D25B8A;">
                    <tr align=center>
                        <th>DESCRIPCIÓN</th>
                        <th>APOYOS</th>
                        <th>BENEFICIARIOS</th>
                    </tr>"""
        if ME_Acciones != "0":
            texto += """
                <tr align=center>
                            <td>Programa Mujeres Emprendedoras</td>
                            <td>""" + ME_Acciones + """</td>
                            <td>""" + ME_Beneficiarios + """</td>
                        </tr>
                """
        if MAA_Acciones != "0":
            texto += """
                    <tr align=center>
                            <td>Programa Módulos Hacia la Autosuficiencia Alimentaria</td>
                            <td>""" + MAA_Acciones + """</td>
                            <td>""" + MAA_Beneficiarios + """</td>
                        </tr>
            """
        if MAG_Acciones != "0":
            texto += """
                <tr align=center>
                            <td>Modulos de Agua</td>
                            <td>""" + MAG_Acciones + """</td>
                            <td>""" + MAG_Beneficiarios + """</td>
                        </tr>
                """
        if MHI_Acciones != "0":
            texto += """
                <tr align=center>
                            <td>Huertos Infantiles</td>
                            <td>""" + MHI_Acciones + """</td>
                            <td>""" + MHI_Beneficiarios + """</td>
                </tr>
            """
        if Pisos != "0":
            texto += """
            <tr align=center>
                            <td>Pisos</td>
                            <td>""" + Pisos + """</td>
                            <td>""" + Pisos_Beneficiarios + """</td>
                        </tr>
            """
        if Techos != "0":
            texto += """
                <tr align=center>
                            <td>Techos</td>
                            <td>""" + Techos + """</td>
                            <td>""" + Techos_Beneficiarios + """</td>
                        </tr>
            """
        if Cuartos_Dormitorios != "0":
            texto += """
                    <tr align=center>
                            <td>Cuartos dormitorios</td>
                            <td>""" + Cuartos_Dormitorios + """</td>
                            <td>""" + Cuartos_Beneficiarios + """</td>
                        </tr>
            """
        if Estufas_ecológicas != "0":
            texto += """
                    <tr align=center>
                            <td>Estufas Ecológicas</td>
                            <td>""" + Estufas_ecológicas + """</td>
                            <td>""" + Estufas_Beneficiarios + """</td>
                        </tr>
            """
        if Sanitarios != "0":
            texto += """
                    <tr align=center>
                            <td>Sanitarios con Biodigestor</td>
                            <td>""" + Sanitarios + """</td>
                            <td>""" + Sanitarios_Beneficiarios + """</td>
                        </tr>
            """
        texto += """
                    </table>
                    """

    # cierre de toda la tarjeta
    texto += """            
                <div align = "center">
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("SEDESOL") + """
                </div>
            </div>
        </article>
    """

    return texto
