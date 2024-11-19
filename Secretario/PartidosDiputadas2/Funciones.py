def content_directorio(NOMBRE, PARTIDO, ANIO, ENTIDAD, FOTO,anio,nom_dis):
    if ".jpg" in FOTO:
        # img = """ <img src = '""" + foto + """' width = '170' height = '170'></img> """
        img = """ <img class="card-img-top" src= '""" + FOTO + """' width = '170' height = '170' alt=""> """

    else:
        foto = "images/user2.png"
        img = """ <img src = '""" + foto + """' width = '170' height = '170'></img> """

    texto = """
        <article style="width: 400px;background-color:#C6046B;border-radius: 5px; padding:20px; text-overflow: ellipsis;">
        <div align=center><h4><span class="label label-primary">""" + NOMBRE + """</span></h2><div>
        <table id=delegado class="table table-condensed" style="font-family:sans-serif; font-size:12px;color:#FFFFFF; background-color:#9880b9;">
                <tr >
                    <td rowspan="3" align="center">""" + img + """</td>
                    <td>Partido: """ + PARTIDO + """</td>
                    <td>Año: """ + anio + """</td>
                </tr>

                <tr>
                    <td colspan="2">Región: """ + ENTIDAD + """</td>
                </tr>

            </table>"""
    texto2 = """
            <div class="card" style="width: 18rem; font-family:sans-serif; font-size:12px;color:#FFFFFF; background-color:#9880b9;">
              """ + img + """
              <div class="card-body">
                <h6 class="card-title">""" + NOMBRE + """</h6>              
                <p style= "color:#FFFFFF;" "font-family:roboto; font-size:9px;><strong>Partido: </strong>""" + PARTIDO + """</p>
                <p style= "color:#FFFFFF;" "font-family:roboto; font-size:9px;><strong> </strong>""" + ENTIDAD + """</p>
                <p style= "color:#FFFFFF;" "font-family:roboto; font-size:9px;><strong>Año: </strong>""" + anio + """</p>
                <p style= "color:#FFFFFF;" "font-family:roboto; font-size:9px;><strong>Dtto: </strong>""" + nom_dis + """</p>

              </div>
            </div>
    """

    return texto2


def content_proporcional(NOMBRE, PARTIDO, ENTIDAD, NOMBRE1, PARTIDO1, ENTIDAD1, NOMBRE2, PARTIDO2, ENTIDAD2,
                         NOMBRE3, PARTIDO3, ENTIDAD3, NOMBRE4, PARTIDO4, ENTIDAD4, NOMBRE5, PARTIDO5, ENTIDAD5,
                         NOMBRE6, PARTIDO6, ENTIDAD6, NOMBRE7, PARTIDO7, ENTIDAD7, NOMBRE8, PARTIDO8, ENTIDAD8,
                         NOMBRE9, PARTIDO9, ENTIDAD9, NOMBRE10, PARTIDO10, ENTIDAD10, NOMBRE11, PARTIDO11, ENTIDAD11,
                         NOMBRE12, PARTIDO12, ENTIDAD12):
    texto2 = """
    <div class="card" style="width: 18rem; font-family:sans-serif; font-size:12px;color:#FFFFFF; background-color:#9880b9;">
    <div class = "card-body" align = "center">
    <h4 align = "center"><span class="label label-primary">""" + ENTIDAD + """</span></h2>
        <tbody align = "center">
        <div class = "card-body" align = "center" style = width:'600px;'>
            <table id=aplicaciones class="table table-hover table-sm table table-condensed" style="font-family:sans-serif; font-size:12px;color:#FFFFFF; background-color:#9880b9; width: '450';"> 
                    <tr align="center">
                        <th align = "center">PARTIDOS</th>                                               
                        <th align = "center">TOTAL: [13]</th>          
                    </tr>
                    <tr> 
                        <td> 
                            <div id="accordion">                       
                                  <h5 class="mb-0" align="center" >
                                    <button class="btn btn-link" style="color: #F5CE57; font-family:sans-serif; font-size:10px;" data-toggle="collapse" data-target="#collapseOne" 
                                    aria-expanded="true" aria-controls="collapseOne" >
                                    PRI
                                    </button>
                                  </h5>
                                  <div id="collapseOne" class="collapse" aria-labelledby="headingOne" data-parent="#accordion">
                                  <div class="card-body">
                                    <p style="color:#FFFFFF; margin: 0px; font-size:11px; font-family:sans-serif;">* """ + NOMBRE + """ </p>


                                    <p style="color:#FFFFFF; margin: 0px; font-size:11px; font-family:sans-serif;">* """ + NOMBRE1 + """ </p>

                                  </div>
                                </div> 

                            </div>      

                        </td>
                        <td> 2 </td>

                    </tr> 

                    <tr> 
                        <td> 
                            <div id="accordion">                       
                                  <h5 class="mb-0" align="center" >
                                    <button class="btn btn-link" style="color: #F5CE57; font-family:sans-serif; font-size:10px;" data-toggle="collapse" data-target="#collapseTwo" 
                                    aria-expanded="true" aria-controls="collapseTwo" >
                                    MC
                                    </button>
                                  </h5>
                                  <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordion">
                                  <div class="card-body">
                                    <p style="color:#FFFFFF; margin: 0px; font-size:11px; font-family:sans-serif;">* """ + NOMBRE2 + """ </p>


                                    <p style="color:#FFFFFF; margin: 0px; font-size:11px; font-family:sans-serif;">* """ + NOMBRE3 + """ </p>

                                  </div>
                                </div> 

                            </div>      

                        </td>
                        <td> 2 </td>

                    </tr>

                    <tr> 
                        <td> 
                            <div id="accordion">                       
                                  <h5 class="mb-0" align="center" >
                                    <button class="btn btn-link" style="color: #F5CE57; font-family:sans-serif; font-size:10px;" data-toggle="collapse" data-target="#collapseThree" 
                                    aria-expanded="true" aria-controls="collapseThree" >
                                    PAN
                                    </button>
                                  </h5>
                                  <div id="collapseThree" class="collapse" aria-labelledby="headingThree" data-parent="#accordion">
                                  <div class="card-body">
                                    <p style="color:#FFFFFF; margin: 0px; font-size:11px; font-family:sans-serif;">* """ + NOMBRE4 + """ </p>


                                    <p style="color:#FFFFFF; margin: 0px; font-size:11px; font-family:sans-serif;">* """ + NOMBRE5 + """ </p>


                                    <p style="color:#FFFFFF; margin: 0px; font-size:11px; font-family:sans-serif;">* """ + NOMBRE6 + """ </p>

                                  </div>
                                </div> 

                            </div>      

                        </td> 
                        <td> 3 </td>                    
                    </tr>

                    <tr> 
                        <td> 
                            <div id="accordion">                       
                                  <h5 class="mb-0" align="center" >
                                    <button class="btn btn-link" style="color: #F5CE57; font-family:sans-serif; font-size:10px;" data-toggle="collapse" data-target="#collapseFour" 
                                    aria-expanded="true" aria-controls="collapseFour" >
                                    MORENA
                                    </button>
                                  </h5>
                                  <div id="collapseFour" class="collapse" aria-labelledby="headingFour" data-parent="#accordion">
                                  <div class="card-body">
                                    <p style="color:#FFFFFF; margin: 0px; font-size:11px; font-family:sans-serif;">* """ + NOMBRE7 + """ </p>


                                    <p style="color:#FFFFFF; margin: 0px; font-size:11px; font-family:sans-serif;">* """ + NOMBRE8 + """ </p>

                                  </div>
                                </div> 

                            </div>      

                        </td>
                         <td> 2 </td>


                    </tr>

                    <tr> 
                        <td> 
                            <div id="accordion">                       
                                  <h5 class="mb-0" align="center" >
                                    <button class="btn btn-link" style="color: #F5CE57; font-family:sans-serif; font-size:10px;" data-toggle="collapse" data-target="#collapseFive" 
                                    aria-expanded="true" aria-controls="collapseFive" >
                                    PRD
                                    </button>
                                  </h5>
                                  <div id="collapseFive" class="collapse" aria-labelledby="headingFive" data-parent="#accordion">
                                  <div class="card-body">
                                    <p style="color:#FFFFFF; margin: 0px; font-size:11px; font-family:sans-serif;">* """ + NOMBRE9 + """ </p>


                                    <p style="color:#FFFFFF; margin: 0px; font-size:11px; font-family:sans-serif;">* """ + NOMBRE10 + """ </p>

                                  </div>
                                </div> 

                            </div>      

                        </td>
                         <td> 2 </td>


                    </tr>

                    <tr> 
                        <td> 
                            <div id="accordion">                       
                                  <h5 class="mb-0" align="center" >
                                    <button class="btn btn-link" style="color: #F5CE57; font-family:sans-serif; font-size:10px;" data-toggle="collapse" data-target="#collapseSix" 
                                    aria-expanded="true" aria-controls="collapseSix" >
                                    PVEM
                                    </button>
                                  </h5>
                                  <div id="collapseSix" class="collapse" aria-labelledby="headingSix" data-parent="#accordion">
                                  <div class="card-body">
                                    <p style="color:#FFFFFF; margin: 0px; font-size:11px; font-family:sans-serif;">* """ + NOMBRE11 + """ </p>


                                    <p style="color:#FFFFFF; margin: 0px; font-size:11px; font-family:sans-serif;">* """ + NOMBRE12 + """ </p>

                                  </div>
                                </div> 

                            </div>      

                        </td>
                         <td> 2 </td>


                    </tr>




                    </tbody>        
                </table>   
            </div>
            </div>
    </div>   

        """

    return texto2
