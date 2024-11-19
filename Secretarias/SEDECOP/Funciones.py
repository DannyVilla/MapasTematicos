from RS import genera_rs

def highlight(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.7,
        'line_opacity': 0.7
    }

def html_tabla(PROG1, DESC1, BEN1, FOTO1, PROG2, DESC2, BEN2, FOTO2, PROG3, DESC3, BEN3, FOTO3,
                              PROG4, DESC4, BEN4, FOTO4, PROG5, DESC5, BEN5, FOTO5, PROG6, DESC6, BEN6, FOTO6,
                              PROG7, DESC7, BEN7, FOTO7, PROG8, DESC8, BEN8, FOTO8, PROG9, DESC9, BEN9, FOTO9,
                              PROG10, DESC10, BEN10, FOTO10, PROG11, DESC11, BEN11, FOTO11, PROG12, DESC12, BEN12, FOTO12,
                              PROG13, DESC13, BEN13, FOTO13):
    texto_tabla = " "
    if PROG1 != "0":
        texto_tabla += """
            <tr>
                        <td>""" + PROG1 + """
                        <div id="accordion">                       
                                  <h5 class="mb-0" align="center" >
                                    <button class="btn btn-link" style="color: #F5CE57; font-family:sans-serif; font-size:10px;" data-toggle="collapse" data-target="#collapseOne" 
                                    aria-expanded="true" aria-controls="collapseOne" >
                                      MÁS INFORMACIÓN
                                    </button>
                                  </h5>
                                <div id="collapseOne" class="collapse" aria-labelledby="headingOne" data-parent="#accordion">
                                    <p style="color:#FFFFFF; margin: 0px; font-size:10px; font-family:sans-serif;"> """ + DESC1 + """</p>
                                </div>                                                            
                            </div>   
                                              
                        </td>                     
                        <td align="center">""" + BEN2 + """</td>
           </tr>                
        """

    if PROG2 != "0":
        texto_tabla += """
           <tr>
                        <td>""" + PROG2 + """
                        <div id="accordion">                       
                                  <h5 class="mb-0" align="center" >
                                    <button class="btn btn-link" style="color: #F5CE57; font-family:sans-serif; font-size:10px;" data-toggle="collapse" data-target="#collapseTwo" 
                                    aria-expanded="true" aria-controls="collapseTwo" >
                                      MÁS INFORMACIÓN
                                    </button>
                                  </h5>
                                <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordion">
                                    <p style="color:#FFFFFF; margin: 0px; font-size:10px; font-family:sans-serif;"> """ + DESC2 + """</p>
                                </div>                                                            
                            </div>   
                                              
                        </td>                     
                        <td align="center">""" + BEN2 + """</td>
           </tr>

        """
    if PROG3 != "0":
        texto_tabla += """
           <tr>
                        <td>""" + PROG3 + """
                        <div id="accordion">                       
                                  <h5 class="mb-0" align="center" >
                                    <button class="btn btn-link" style="color: #F5CE57; font-family:sans-serif; font-size:10px;" data-toggle="collapse" data-target="#collapseThree" 
                                    aria-expanded="true" aria-controls="collapseThree" >
                                      MÁS INFORMACIÓN
                                    </button>
                                  </h5>
                                <div id="collapseThree" class="collapse" aria-labelledby="headingThree" data-parent="#accordion">
                                    <p style="color:#FFFFFF; margin: 0px; font-size:10px; font-family:sans-serif;"> """ + DESC3 + """</p>
                                </div>
                                                         
                            </div>   
                        </td>
                        <td align="center">""" + BEN3 + """</td>
           </tr>

        """
    if PROG4 != "0":
        texto_tabla += """
           <tr>
                        <td>""" + PROG4 + """
                        <div id="accordion">                       
                                  <h5 class="mb-0" align="center" >
                                    <button class="btn btn-link" style="color: #F5CE57; font-family:sans-serif; font-size:10px;" data-toggle="collapse" data-target="#collapseFour" 
                                    aria-expanded="true" aria-controls="collapseFour" >
                                      MÁS INFORMACIÓN
                                    </button>
                                  </h5>
                                <div id="collapseFour" class="collapse" aria-labelledby="headingFour" data-parent="#accordion">
                                    <p style="color:#FFFFFF; margin: 0px; font-size:10px; font-family:sans-serif;"> """ + DESC4 + """</p>
                                </div>                                                            
                            </div>   
                                          
                        </td>
                        <td align="center">""" + BEN4 + """</td>
           </tr>

        """
    if PROG5 != "0":
        texto_tabla += """
           <tr>
                        <td>""" + PROG5 + """
                        <div id="accordion">                       
                                  <h5 class="mb-0" align="center" >
                                    <button class="btn btn-link" style="color: #F5CE57; font-family:sans-serif; font-size:10px;" data-toggle="collapse" data-target="#collapseFive" 
                                    aria-expanded="true" aria-controls="collapseFive">
                                      MÁS INFORMACIÓN
                                    </button>
                                  </h5>
                                <div id="collapseFive" class="collapse" aria-labelledby="headingFive" data-parent="#accordion">
                                    <p style="color:#FFFFFF; margin: 0px; font-size:10px; font-family:sans-serif;"> """ + DESC5 + """</p>
                                </div>                                                            
                            </div>   
                                          
                        </td>
                        <td align="center">""" + BEN5 + """</td>
           </tr>

        """
    if PROG6 != "0":
        texto_tabla += """
           <tr>
                        <td>""" + PROG6 + """
                        <div id="accordion">                       
                                  <h5 class="mb-0" align="center" >
                                    <button class="btn btn-link" style="color: #F5CE57; font-family:sans-serif; font-size:10px;" data-toggle="collapse" data-target="#collapseSix" 
                                    aria-expanded="true" aria-controls="collapseSix" >
                                      MÁS INFORMACIÓN
                                    </button>
                                  </h5>
                                <div id="collapseSix" class="collapse" aria-labelledby="headingSix" data-parent="#accordion">
                                    <p style="color:#FFFFFF; margin: 0px; font-size:10px; font-family:sans-serif;"> """ + DESC6 + """</p>
                                </div>                                                            
                            </div>   
                                          
                        </td>
                        <td align="center">""" + BEN6 + """</td>
           </tr>

        """
    if PROG7 != "0":
        texto_tabla += """
           <tr>
                        <td>""" + PROG7 + """
                        <div id="accordion">                       
                                  <h5 class="mb-0" align="center" >
                                    <button class="btn btn-link" style="color: #F5CE57; font-family:sans-serif; font-size:10px;" data-toggle="collapse" data-target="#collapseSeven" 
                                    aria-expanded="true" aria-controls="collapseSeven" >
                                      MÁS INFORMACIÓN
                                    </button>
                                  </h5>
                                
                            
                                <div id="collapseSeven" class="collapse" aria-labelledby="headingSeven" data-parent="#accordion">
                                    <p style="color:#FFFFFF; margin: 0px; font-size:10px; font-family:sans-serif;"> """ + DESC7 + """</p>
                                </div>                                                            
                            </div>   
                                          
                        </td>
                        <td align="center">""" + BEN7 + """</td>
           </tr>

        """
    if PROG8 != "0":
        texto_tabla += """
           <tr>
                        <td>""" + PROG8 + """
                        <div id="accordion">                       
                                  <h5 class="mb-0" align="center" >
                                    <button class="btn btn-link" style="color: #F5CE57; font-family:sans-serif; font-size:10px;" data-toggle="collapse" data-target="#collapseEight" 
                                    aria-expanded="true" aria-controls="collapseEight" >
                                      MÁS INFORMACIÓN
                                    </button>
                                  </h5>
                                
                            
                                <div id="collapseEight" class="collapse" aria-labelledby="headingEight" data-parent="#accordion">
                                    <p style="color:#FFFFFF; margin: 0px; font-size:10px; font-family:sans-serif;"> """ + DESC8 + """</p>
                                </div>                                                            
                            </div>   
                                          
                        </td>
                        <td align="center">""" + BEN8 + """</td>
           </tr>

        """
    if PROG9 != "0":
        texto_tabla += """
           <tr>
                        <td>""" + PROG9 + """
                        <div id="accordion">                       
                                  <h5 class="mb-0" align="center" >
                                    <button class="btn btn-link" style="color: #F5CE57; font-family:sans-serif; font-size:10px;" data-toggle="collapse" data-target="#collapseNine" 
                                    aria-expanded="true" aria-controls="collapseNine" >
                                      MÁS INFORMACIÓN
                                    </button>
                                  </h5>
                                
                            
                                <div id="collapseNine" class="collapse" aria-labelledby="headingNine" data-parent="#accordion">
                                    <p style="color:#FFFFFF; margin: 0px; font-size:10px; font-family:sans-serif;"> """ + DESC9 + """</p>
                                </div>                                                            
                            </div>   
                                          
                        </td>
                        <td align="center">""" + BEN9 + """</td>
           </tr>

        """
    if PROG10 != "0":
        texto_tabla += """
           <tr>
                        <td>""" + PROG10 + """
                        <div id="accordion">                       
                                  <h5 class="mb-0" align="center" >
                                    <button class="btn btn-link" style="color: #F5CE57; font-family:sans-serif; font-size:10px;" data-toggle="collapse" data-target="#collapseTen" 
                                    aria-expanded="true" aria-controls="collapseTen" >
                                      MÁS INFORMACIÓN
                                    </button>
                                  </h5>
                                
                            
                                <div id="collapseTen" class="collapse" aria-labelledby="headingTen" data-parent="#accordion">
                                    <p style="color:#FFFFFF; margin: 0px; font-size:10px; font-family:sans-serif;"> """ + DESC10 + """</p>
                                </div>                                                            
                            </div>   
                                          
                        </td>
                        <td align="center">""" + BEN10 + """</td>
           </tr>

        """
    if PROG11 != "0":
        texto_tabla += """
           <tr>
                        <td>""" + PROG11 + """
                        <div id="accordion">                       
                                  <h5 class="mb-0" align="center" >
                                    <button class="btn btn-link" style="color: #F5CE57; font-family:sans-serif; font-size:10px;" data-toggle="collapse" data-target="#collapseEleven" 
                                    aria-expanded="true" aria-controls="collapseEleven" >
                                      MÁS INFORMACIÓN
                                    </button>
                                  </h5>
                                
                            
                                <div id="collapseEleven" class="collapse" aria-labelledby="headingEleven" data-parent="#accordion">
                                    <p style="color:#FFFFFF; margin: 0px; font-size:10px; font-family:sans-serif;"> """ + DESC11 + """</p>
                                </div>                                                            
                            </div>   
                                          
                        </td>
                        <td align="center">""" + BEN11 + """</td>
           </tr>

        """
    if PROG12 != "0":
        texto_tabla += """
           <tr>
                        <td>""" + PROG12 + """ </td>
                        <td align="center">""" + BEN12 + """</td>
           </tr>

        """
    if PROG13 != "0":
        texto_tabla += """
           <tr>
                        <td>""" + PROG13 + """ </td>
                        <td align="center">""" + BEN13 + """</td>
           </tr>

        """

    return texto_tabla

def html_foto(FOTO1,FOTO2,FOTO3,FOTO4,FOTO5,FOTO6,FOTO7,FOTO8,FOTO9,FOTO10,FOTO11,FOTO12,FOTO13,
              PROG1,PROG2,PROG3,PROG4,PROG5,PROG6,PROG7,PROG8,PROG9,PROG10,PROG11,PROG12,PROG13):

    btn_slide= """
            <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="sr-only">Previous</span>
            </a>
            <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="sr-only">Next</span>
            </a>            
    """

    texto_foto = " "
    if FOTO1 != "VACIO":
        texto_foto += """
        <p style="color:#FFFFFF; margin: 0px;"> Evidencia: """ + PROG1 + """</p>
        <div class="carousel-item" align="center">
            <img class="d-block w-100" src='""" + FOTO1 + """' alt="Second slide" width='250' height='180'/>
        </div> 
        """+ btn_slide + """   
    """



    if FOTO2 != "VACIO":
        texto_foto += """
        <p style="color:#FFFFFF; margin: 0px;"> Evidencia: """ + PROG2 + """</p>

        <div class="carousel-item" align="center">
            <img class="d-block w-100" src='""" + FOTO2 + """' alt="Third slide" width='250' height='180'/>
        </div>  
        """+ btn_slide + """         
    """


    if FOTO3 != "VACIO":
        texto_foto += """
        <p style="color:#FFFFFF; margin: 0px;"> Evidencia: """ + PROG3 + """</p>

        <div class="carousel-item" align="center">
            <img class="d-block w-100" src='""" + FOTO3 + """' alt="Fourth slide" width='250' height='180'/>
        </div> 
        """+ btn_slide + """          
    """

    if FOTO4 != "VACIO":
        texto_foto += """
        <p style="color:#FFFFFF; margin: 0px;"> Evidencia: """ + PROG4 + """</p>

        <div class="carousel-item" align="center">
            <img class="d-block w-100" src='""" + FOTO4 + """' alt="Fifth slide" width='250' height='180'/>
        </div> 
        """+ btn_slide + """  
    """


    if FOTO5 != "VACIO":
        texto_foto += """
        <p style="color:#FFFFFF; margin: 0px;"> Evidencia: """ + PROG5 +"""</p>

        <div class="carousel-item" align="center">
            <img class="d-block w-100" src='""" + FOTO5 + """' alt="Sixth slide" width='250' height='180'/>
        </div>
        """+ btn_slide + """           
    """


    if FOTO6 != "VACIO":
        texto_foto += """
        <p style="color:#FFFFFF; margin: 0px;"> Evidencia: """ + PROG6 + """</p>

        <div class="carousel-item" align="center">
            <img class="d-block w-100" src='""" + FOTO6 + """' alt="Seventh slide" width='250' height='180'/>
        </div> 
        """+ btn_slide + """          
    """


    if FOTO7 != "VACIO":
        texto_foto += """
        <p style="color:#FFFFFF; margin: 0px;"> Evidencia: """ + PROG7 + """</p>

        <div class="carousel-item" align="center">
            <img class="d-block w-100" src='""" + FOTO7 + """' alt="Eighth slide" width='250' height='180'/>
        </div> 
        """+ btn_slide + """          
    """


    if FOTO8 != "VACIO":
        texto_foto += """
        <p style="color:#FFFFFF; margin: 0px;"> Evidencia: """ + PROG8 + """</p>

        <div class="carousel-item" align="center">
            <img class="d-block w-100" src='""" + FOTO8 + """' alt="Ninth slide" width='250' height='180'/>
        </div>
        """+ btn_slide + """           
    """


    if FOTO9 != "VACIO":
        texto_foto += """
        <p style="color:#FFFFFF; margin: 0px;"> Evidencia: """ + PROG9 + """</p>

        <div class="carousel-item" align="center">
            <img class="d-block w-100" src='""" + FOTO9 + """' alt="Tenth slide" width='250' height='180'/>
        </div>   
        """+ btn_slide + """        
    """


    if FOTO10 != "VACIO":
        texto_foto += """
        <p style="color:#FFFFFF; margin: 0px;"> Evidencia: """ + PROG10 + """</p>

        <div class="carousel-item" align="center">
            <img class="d-block w-100" src='""" + FOTO10 + """' alt="Eleventh slide" width='250' height='180'/>
        </div>  
        """+ btn_slide + """         
    """


    if FOTO11 != "VACIO":
        texto_foto += """
        <p style="color:#FFFFFF; margin: 0px;"> Evidencia: """ + PROG11 + """</p>
        <div class="carousel-item" align="center">
            <img class="d-block w-100" src='""" + FOTO11 + """' alt="Twelfth slide" width='250' height='180'/>
        </div> 
        """+ btn_slide + """          
    """


    if FOTO12 != "VACIO":
        texto_foto += """
        <p style="color:#FFFFFF; margin: 0px;"> Evidencia: """ + PROG12 + """</p>

        <div class="carousel-item" align="center">
            <img class="d-block w-100" src='""" + FOTO12 + """' alt="Thirteenth slide" width='250' height='180'/>
        </div> 
        """+ btn_slide + """          
    """


    if FOTO13 != "VACIO":
        texto_foto += """
        <p style="color:#FFFFFF; margin: 0px;"> Evidencia: """ + PROG13 + """</p>

        <div class="carousel-item" align="center">
            <img class="d-block w-100" src='""" + FOTO13 + """' alt="Fourteenth slide" width='250' height='180'/>
        </div> 
        """+ btn_slide + """  
    """

    return texto_foto

def genera_tarjeta2021(MUNICIPIO, PROG1, DESC1, BEN1, FOTO1, PROG2, DESC2, BEN2, FOTO2, PROG3, DESC3, BEN3, FOTO3,
                              PROG4, DESC4, BEN4, FOTO4, PROG5, DESC5, BEN5, FOTO5, PROG6, DESC6, BEN6, FOTO6,
                              PROG7, DESC7, BEN7, FOTO7, PROG8, DESC8, BEN8, FOTO8, PROG9, DESC9, BEN9, FOTO9,
                              PROG10, DESC10, BEN10, FOTO10, PROG11, DESC11, BEN11, FOTO11, PROG12, DESC12, BEN12, FOTO12,
                              PROG13, DESC13, BEN13, FOTO13, anio):


    validar_tabla = html_tabla(PROG1, DESC1, BEN1, FOTO1, PROG2, DESC2, BEN2, FOTO2, PROG3, DESC3, BEN3, FOTO3,
                              PROG4, DESC4, BEN4, FOTO4, PROG5, DESC5, BEN5, FOTO5, PROG6, DESC6, BEN6, FOTO6,
                              PROG7, DESC7, BEN7, FOTO7, PROG8, DESC8, BEN8, FOTO8, PROG9, DESC9, BEN9, FOTO9,
                              PROG10, DESC10, BEN10, FOTO10, PROG11, DESC11, BEN11, FOTO11, PROG12, DESC12, BEN12, FOTO12,
                              PROG13, DESC13, BEN13, FOTO13)

    validar_foto = html_foto(FOTO1, FOTO2, FOTO3, FOTO4, FOTO5, FOTO6, FOTO7, FOTO8, FOTO9, FOTO10, FOTO11, FOTO12, FOTO13,
                             PROG1,PROG2,PROG3,PROG4,PROG5,PROG6,PROG7,PROG8,PROG9,PROG10,PROG11,PROG12,PROG13)


    contenido_tabla = """
        <div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
          <div class="carousel-inner">
            <div class="carousel-item active">
                <table id=defunciones class="table table-hover table-sm " style="font-family:sans-serif; font-size:9px;color:#FFFFFF; background-color:#D25B8A;">
                    <tr align=center>
                        <th>DESCRIPCIÓN</th>
                        <th>BENEFICIARIOS</th>          
                    </tr>
    """
    if validar_foto != " ":
        validar_foto = validar_foto

    cierre = """
                </table>
                <!-- Cierre primer slide. -->            
                    </div>
                        
                           """ + validar_foto + """  
                      
                    </div> """
    if validar_foto != " ":
        contenido_tabla +="""
        
                      <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
                        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                        <span class="sr-only">Previous</span>
                      </a>
                      <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
                        <span class="carousel-control-next-icon" aria-hidden="true"></span>
                        <span class="sr-only">Next</span>
                      </a>

                      """

    """
    """


    if validar_tabla != " ":
        validar_tabla = contenido_tabla + validar_tabla + cierre

    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                <h6 align = "center"><span class="badge badge-light"><i class="fa fa-calendar" style = "color:#FAC63A;"></i> ACCIONES """ + anio + """<span></h6>
  
            """ + validar_tabla + """         
        
        """

    texto += """
                <div align = "center">
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("SEDECOP") + """
                </div>
            </div>
        </article>
        """

    return texto

def genera_tarjeta2022(MUNICIPIO,CAP,HV,TIENDA_HV,COD_BAR,EST_DE_CONT,REG_DE_MARCA,LOGO_E_IMAGEN,VINC_COM,
                       FOROS_Y_EXPOS,PAAV,ASIST_TEC_ART,ASIST_TEC_EMP,DIS_DE_EMB,ART_IMPULSO_A_LA_PROD,TERMIN_DE_COBRO,SUMAS,anio):
    texto = """
            <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
                <div class="card-body">
                    <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                    <h6 align = "center"><span class="badge badge-light"><i class="fa fa-calendar" style = "color:#FAC63A;"></i> ACCIONES """ + anio + """<span></h6>
            """

    texto += """           
                <table class="table table-hover table-sm " style=" font-family:sans-serif; font-size:9px;color:#FFFFFF; background-color:#D25B8A;">
                """
    if CAP != "0":
        texto += """
                    <tr>
                        <td>Capacitación Empresarial</td>
                        <td>""" + CAP + """</td>
                    </tr>
                """
    if HV != "0":
        texto += """

                    <tr>
                        <td>Empresas acreditadas (Hecho en Veracruz)</td>
                        <td> """ + HV + """</td>
                    </tr>
                """
    if TIENDA_HV != "0":
        texto += """

                    <tr>
                        <td>Tienda HV</td>
                        <td>""" + TIENDA_HV + """</td>
                    </tr> 
                """
    if COD_BAR != "0":
        texto += """ 

                    <tr>
                        <td>Empresas apoyadas con código de barras</td>
                        <td>""" + COD_BAR + """</td>
                    </tr>
                """
    if EST_DE_CONT != "0":
        texto += """

                    <tr>
                        <td>Empresas apoyadas con su Estudio de contenido nutrimental</td>
                        <td>""" + EST_DE_CONT + """</td>
                    </tr>
                """
    if REG_DE_MARCA != "0":
        texto += """

                    <tr>
                        <td>Empresas apoyadas con su registro de marca</td>
                        <td>""" + REG_DE_MARCA + """</td>
                    </tr>
                """
    if LOGO_E_IMAGEN != "0":
        texto += """
                    
                    <tr>
                        <td>Empresas apoyadas con su diseño de logotipo e imagen corporativa</td>
                        <td>""" + LOGO_E_IMAGEN + """</td>
                    </tr>
                """
    if VINC_COM != "0":
        texto += """
                    
                    <tr>
                        <td>Empresas Vinculadas a comercios y cadenas</td>
                        <td>""" + VINC_COM + """</td>
                    </tr>
                """
    if FOROS_Y_EXPOS != "0":
        texto += """
                    
                    <tr>
                        <td>Participanes en ferias y exposiciones comerciales</td>
                        <td>""" + FOROS_Y_EXPOS + """</td>
                    </tr>
                """
    if PAAV != "0":
        texto += """
                    
                    <tr>
                        <td>Participantes del Premio Anual Artesanal Veracruzano</td>
                        <td>""" + PAAV + """</td>
                    </tr>
                """
    if ASIST_TEC_ART != "0":
        texto += """
                    
                    <tr>
                        <td>Artesanos apoyados con asistencia técnica</td>
                        <td>""" + ASIST_TEC_ART + """</td>
                    </tr>
                """
    if ASIST_TEC_EMP != "0":
        texto += """
                    
                    <tr>
                        <td>Empresarios apoyados con asistencia técnica</td>
                        <td>""" + ASIST_TEC_EMP + """</td>
                    </tr>
                """
    if DIS_DE_EMB != "0":
        texto += """
                    
                    <tr>
                        <td>Empresas apoyadas con Diseño de Embalaje</td>
                        <td>""" + DIS_DE_EMB + """</td>
                    </tr>
                """
    if ART_IMPULSO_A_LA_PROD != "0":
        texto += """
                    
                    <tr>
                        <td>Artesanos apoyados para impulsar su producción</td>
                        <td>""" + ART_IMPULSO_A_LA_PROD + """</td>
                    </tr>
                """
    if TERMIN_DE_COBRO != "0":
        texto += """

                    <tr>
                        <td>Empresas apoyadas con terminales de cobro</td>
                        <td>""" + TERMIN_DE_COBRO + """</td>
                    </tr>
                """
    if SUMAS != "0":
        texto += """
                    
                    <tr>
                        <td>Total</td>
                        <td>""" + SUMAS + """</td>
                    </tr>

                </table> 
        """


    texto += """
                <div align = "center">
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("SEDECOP") + """
                </div>
            </div>
        </article>
        """

    return texto

