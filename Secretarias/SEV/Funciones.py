def highlight(feature):
    return {
        'weight': 5,
        'opacity': 1,
        'fillOpacity': 0.7,
        'line_opacity': 0.7
    }


def content_delegaciones(Nombre_Del, Direccion, Telefono, Titular, Correo):
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <h6 align = "center"><span class="badge badge-danger">DELEGACIÓN """ + Nombre_Del + """</span></h6>
                <p style="color:#FFFFFF; margin: 0px;"><i class ="fa fa-user" style = "color:#FAC63A;"></i><strong> TITULAR: </strong > """ + Titular + """ </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class ="fa fa-envelope" style = "color:#FAC63A;"></i><strong> CORREO: </strong > """ + Correo + """ </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-phone" style = "color:#FAC63A;"></i><strong> TELÉFONO: </strong>""" + Telefono + """  </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-home" style = "color:#FAC63A;"></i><strong> DIRECCIÓN: </strong>""" + Direccion + """  </p>

        """
    return texto


def content_escuelas(nombre_ct, domicilio, num_ext, total_alumnos, profesores, nivel, clave):
    texto = """
        <article class="popup" style="background-color:#900C3F; margin: 0px; font-family:sans-serif; font-size:11px;border-radius: 20px; padding=5px;">
            <div class="card-body">
                <p align = "center" style="color:#FAC63A; margin: 0px;"><strong>""" + nombre_ct + """</strong></p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-group" style = "color:#FAC63A;"></i><strong> ALUMNOS: """+ total_alumnos +""" </strong></p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-user-secret" style = "color:#FAC63A;"></i><strong> PROFESORES: </strong>""" + profesores + """  </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-trophy" style = "color:#FAC63A;"></i><strong> NIVEL: </strong>""" + nivel + """  </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-newspaper-o" style = "color:#FAC63A;"></i><strong> CLAVE: </strong>""" + clave + """  </p>
                <p style="color:#FFFFFF; margin: 0px;"><i class="fa fa-home" style = "color:#FAC63A;"></i><strong> DIRECCIÓN: </strong>""" + domicilio + " " + num_ext + """  </p>
                

        """
    return texto
