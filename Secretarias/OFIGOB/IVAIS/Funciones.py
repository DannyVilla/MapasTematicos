from RS import genera_rs

def highlight(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.7,
        'line_opacity': 0.7
    }


def genera_tarjeta(MUNICIPIO, LUGAR, EVENTO, CAPA, FECHA, GRUPOS, FOTO1, FOTO2, FOTO3, FOTO4):
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i>""" + FECHA + """  </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-home" style = "color:#FAC63A;"></i><strong> LUGAR: </strong>""" + LUGAR + """  </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-group" style = "color:#FAC63A;"></i><strong> ASISTENTES: """+ GRUPOS +""" </strong></p>
                <p style="color:#FFFFFF; margin: 0px;"><strong>EVENTO: </strong>""" + EVENTO + """</p>    
            """
    if FOTO1 != "0":
        texto += """        
                <div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
                    <div class="carousel-inner" align  = "center">
                        <div class="carousel-item active">
                            <img class="postcard__img" src='""" + FOTO1 + """'  width='250' height='180'/>
                        </div>"""
    else:
        texto +="""    
                </div>
    """
    if FOTO2 != "0":
        texto += """
                        <div class="carousel-item" align  = "center">
                            <img class="postcard__img" src='""" + FOTO2 + """'  width='250' height='180'/>
                        </div>"""
    else:
        texto +="""    
                </div>
    """
    if FOTO3 != "0":
        texto += """
                        <div class="carousel-item" align  = "center">
                            <img class="postcard__img" src='""" + FOTO3 + """'  width='250' height='180'/>
                        </div>"""
    else:
        texto +="""    
                </div>
    """
    if FOTO4 != "0":
        texto += """
                        <div class="carousel-item" align  = "center">
                            <img class="postcard__img" src='""" + FOTO4 + """'  width='250' height='180'/>
                        </div>"""
    else:
        texto += """    
                </div>
        """

    texto += """        <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
                            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                            <span class="sr-only">Previous</span>
                        </a>
                        <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
                            <span class="carousel-control-next-icon" aria-hidden="true"></span>
                            <span class="sr-only">Next</span>
                        </a>
                </div>                   
    """
    texto += """
            <div align = "center">
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("IVAIS") + """
                </div>
            </div>
        </article>
        """

    return texto


def genera_tabla_alfabetizacion(MUNICIPIO, DESCRIPCION, A19, A20, A21, NOTA):
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
            <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
            <p style="color:#FFFFFF; margin: 0px;"><strong>Acción:</strong>""" + DESCRIPCION + """</p>
                <table class="table table-hover table-sm " style="font-family:sans-serif; font-size:9px;color:#FFFFFF; background-color:#D25B8A;">
                    <tr align= "center">
                        <td>2019</td>
                        <td>2020</td>
                        <td>2021</td> 
                    </tr>
                    <tr align= "center">
                        <td>""" + A19 + """</td>
                        <td>""" + A20 + """</td>
                        <td>""" + A21 + """</td>
                    </tr>
                </table>
                        
        <p style="color:#FFFFFF; margin: 0px;"><strong>NOTA:</strong>""" + NOTA + """</p>
    """
    texto += """
            <div align = "center">
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("IVAIS") + """
                </div>
            </div>
        </article>
    """

    return texto


def genera_sociedades(MUNICIPIO, MUN_PART, ACCION, ACTIVIDAD, M_2020, H_2020, T_2020, M_2021, H_2021, T_2021):
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
            <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
            <p style="color:#FFFFFF; margin: 0px;"><strong>Acción:</strong> """ + ACCION + """</p>
            <p style="color:#FFFFFF; margin: 0px;"><strong>Actividad productiva/artesanal:</strong> """ + ACTIVIDAD + """</p>
            <p style="color:#FFFFFF; margin: 0px;"><strong>Municipios participantes:</strong> """ + MUN_PART + """</p>
             
                <table class="table table-hover table-sm " style="font-family:sans-serif; font-size:9px;color:#FFFFFF; background-color:#D25B8A;">
                           <tr align= "center">
                            <td colspan=3>2020</td>
                           </tr>
                            <tr align = "center">
                            <td >Mujeres</td>
                            <td >Hombres</td>
                            <td >Total Integrantes</td>  
                           </tr>
                            <tr align=center>
                            <td >""" + M_2020 + """</td>
                            <td >""" + H_2020 + """</td>
                            <td >""" + T_2020 + """</td>  
                           </tr>
                 </table>
                <table class="table table-hover table-sm " style="font-family:sans-serif; font-size:9px;color:#FFFFFF; background-color:#D25B8A;">
                           <tr align=center>
                            <td colspan=3>2021</td>
                           </tr>
                    <tr align=center>
                            <td >Mujeres</td>
                            <td >Hombres</td>
                            <td >Total Integrantes</td>  
                           </tr>
                            <tr align=center>
                            <td >""" + M_2021 + """</td>
                            <td >""" + H_2021 + """</td>
                            <td >""" + T_2021 + """</td>   
                           </tr>
                 </table>
      
        </div>
     """
    texto += """
            <div align = "center">
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("IVAIS") + """
                </div>
            </div>
        </article>
    """
    return texto


def genera_covid(MUNICIPIO, REGION, LENGUA, DESCRIPCION, A_2020, C_2020, V_2020, A_2021, C_2021, V_2021):
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
            <h5 align=center><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
            <p style="color:#FFFFFF; margin: 0px;"><strong>Región:</strong> """ + REGION + """</p>
            <p style="color:#FFFFFF; margin: 0px;"><strong>Lengua:</strong> """ + LENGUA + """</p>
            <p style="color:#FFFFFF; margin: 0px;"><strong>Actividad:</strong> """ + DESCRIPCION + """</p>
                <table class="table table-hover table-sm " style="font-family:sans-serif; font-size:9px;color:#FFFFFF; background-color:#D25B8A;">
                            <tr align=center>
                               <td colspan=3>2020</td>
                            </tr>
                            <tr align=center>
                                <td >AUDIOS</td>
                                <td >CARTELES</td>
                                <td >VIDEO</td>  
                            </tr>
                            <tr align=center>
                                <td >""" + A_2020 + """</td>
                                <td >""" + C_2020 + """</td>
                                <td >""" + V_2020 + """</td>  
                            </tr>
                       </table>
                <table class="table table-hover table-sm " style="font-family:sans-serif; font-size:9px;color:#FFFFFF; background-color:#D25B8A;">
                               <tr align=center>
                                <td colspan=3>2021</td>
                               </tr>
                        <tr align=center>
                                <td >AUDIOS</td>
                                <td >CARTELES</td>
                                <td >VIDEO</td>   
                               </tr>
                                <tr align=center>
                                <td >""" + A_2021 + """</td>
                                <td >""" + C_2021 + """</td>
                                <td >""" + V_2021 + """</td>   
                               </tr>
                     </table>

    
       </div>
    """
    texto += """
            <div align = "center">
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("IVAIS") + """
                </div>
            </div>
        </article>
    """

    return texto
