import numpy as np
from RS import genera_rs

def highlight(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.7,
        'line_opacity': 0.7
    }


def genera_tarjeta(MUNICIPIO, cursos, descripcion, anio):
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align = "center"><span class="badge badge-danger">""" + MUNICIPIO + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i><strong> Capacitaciones """ + anio + """</strong></p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-cubes" style = "color:#FAC63A;"></i><strong>Número de cursos: </strong>""" + cursos + """</p>                
                <p style="color:#FFFFFF; margin: 0px;"> """ + descripcion + """</p>

        """

    texto += """
                <div align = "center">
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("PC") + """
                </div>
            </div>
        </article>
        """

    return texto


def genera_fonden(municipio, anio, total_insumos, desp, cob, col, kl, ka, lam, la, cos, foto, declaratorias, conceptos):
    insumos = {'Despensas': desp, 'Cobertores': cob, 'Colchonetas': col, 'Kit de Limpieza': kl, 'Kit de aseo': ka,
               'Laminas': lam, 'Litros de agua': la, 'Costalillas': cos}
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align="center"><span class="badge badge-danger">""" + municipio + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i><strong>Ejercicio: </strong>""" + anio + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-cubes" style = "color:#FAC63A;"></i><strong>Total insumos entregados: </strong>""" + total_insumos + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><strong># Declaratorias: </strong>""" + declaratorias + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><strong>Declaratorias: </strong>""" + conceptos + """</p>           
                
                <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
                    <ol class="carousel-indicators">
                        <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
                        <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>                   
                    </ol>
                        <div class="carousel-inner">
                            <div class="carousel-item active">                    
                                <table class="table table-hover table-sm " style="font-family:sans-serif; font-size:9px;color:#FFFFFF; background-color:#D25B8A;">
                                    <tr >
                                        <th class="text-center">INSUMO</th>
                                        <th class="text-center">CANTIDAD</th>
                                    </tr>"""
    for insumo in insumos:
        texto += """
                    <tr >
                        <td class="text-left">""" + insumo + """</td>
                        <td class="text-center">""" + insumos[insumo] + """</td>
                    </tr>
                    
                    
                    """

    texto += """            </table>
                    <!-- Cierre primer slide. -->
                        </div>
                        <div class="carousel-item" align="center">
                            <img class="postcard__img" src='""" + foto + """' width='250' height='180'/> 
                        </div>
                    </div>
                        <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
                            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                                <span class="sr-only">Previous</span>
                        </a>
                        <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
                            <span class="carousel-control-next-icon" aria-hidden="true"></span>
                            <span class="sr-only">Next</span>
                        </a>
                    </div>
                    """

    # cierre de toda la tarjeta
    texto += """
            </div>
                <div align = "center">
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("PC") + """
                </div>
            </div>
        </article>
        """
    return texto


def genera_equipo(municipio, entidad, equipo, foto):
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align="center"><span class="badge badge-danger">""" + municipio + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-home" style = "color:#FAC63A;"></i><strong>Entidad Receptora: </strong>""" + entidad +"""</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-cubes" style = "color:#FAC63A;"></i><strong>Equipo Donado: </strong>""" + equipo + """</p>

                    """
    if foto != "0":
        texto += """
                    <div align="center" style="color:#FFFFFF; margin: 0px;">
                        <img class="postcard__img" src='""" + foto + """' width='250' height='180'/> 
                    </div>
           """
    texto += """
                <div align = "center">
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("PC") + """
                </div>
            </div>
        </article>
        """

    return texto


def genera_brigadas(municipio, localidad, anio):
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align="center"><span class="badge badge-danger">""" + localidad + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;">Municipio: """ + municipio + """</p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-calendar" style = "color:#FAC63A;"></i>  Año de instauración: """ + anio + """</p>
        """
    texto += """
                <div align = "center">
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("PC") + """
                </div>
            </div>
        </article>
        """

    return texto


def genera_refugio(municipio, nombre, direccion, capacidadpersonas, capacidadfamilias, foto):
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h5 align="center"><span class="badge badge-warning">""" + municipio + """</span></h5>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-home" style = "color:#FAC63A;"></i><strong>Nombre del Refugio: </strong>""" + nombre + """</p>

                
    """
    if capacidadpersonas != "0":
        texto +="""
                <p style="color:#FFFFFF; margin: 0px;"><i class ="fa fa-user" style = "color:#FAC63A;"></i><strong>Capacidad de Personas: </strong>""" + capacidadpersonas + """</p>
        """
    if capacidadfamilias != "0":
        texto +="""
                <p style="color:#FFFFFF; margin: 0px;"><i class ="fa fa-user" style = "color:#FAC63A;"></i><strong>Capacidad de Familias: </strong>""" + capacidadfamilias + """</p>
        """
    if direccion !="0":
        texto+="""
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-home" style = "color:#FAC63A;"></i><strong>Dirección: </strong>""" + direccion + """</p>
        """
    if foto != "0":
        texto += """
             <div align="center" style="color:#FFFFFF; margin: 0px;">
                <img class="postcard__img" src='""" + foto + """' width='250' height='180'/> 
             </div>
             """
    texto += """
                <div align = "center">
                    <p style="margin: 0px;color:white">Más información: </p> """ + genera_rs("PC") + """
                </div>
            </div>
        </article>
        """

    return texto


def conversion(old):
    direction = {'N': -1, 'S': 1, 'E': -1, 'W': 1}
    new = old.replace(u'°', ' ').replace('\'', ' ').replace('"', ' ')
    new = new.split()
    new_dir = new.pop()
    new.extend([0, 0, 0])
    return (int(new[0]) + int(new[1]) / 60.0 + float(new[2]) / 3600.0) * direction[new_dir]


def cambia_loc(df):
    # df = df.replace('NAN', np.nan)
    mask = df['LAT'].str.contains(r'N', na=False)
    df.loc[mask, 'LAT'] = df['b']
    df['a'] = df['a'].ffill()
    df.loc[mask, 'a'] = np.nan
