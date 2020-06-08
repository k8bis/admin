from django.shortcuts import render, redirect
from gestionAsociados.models.asociado_models import Asociado, AsocRedesSociales, ExperienciaLab,Educacion
from gestionAsociados.models.asociado_models import Habilidades, HabilidadesIdiomas, HabilidadesLenguajes
from gestionAsociados.models.asociado_models import CursosCapacitaciones
from gestionAsociados.models.proyecto_models import Proyecto
from django.contrib.auth.models import User

def vw_index(request):
    if request.method == 'POST':
        return redirect('accounts/login', request.path)
    else:
        asociados_list = list( Asociado.objects.filter( estatus=1 ) )
        proyectos_list = list( Proyecto.objects.all() )

        return render( request, "index/index.html", { 'asoc' : asociados_list, 
                                                      'proy' : proyectos_list } )

def dynamic_lookup_view(request, usr):
    asociado_por_usuario = list(Asociado.objects.filter(usuario__username=usr))
    redes_sociales_por_usuario = list(AsocRedesSociales.objects.filter(asociado__usuario__username=usr))
    experiencia_lab_por_usuario = list(ExperienciaLab.objects.filter(asociado__usuario__username=usr))
    educacion_por_usuario = list(Educacion.objects.filter(asociado__usuario__username=usr))
    habilidades_por_usuario = list(Habilidades.objects.filter(asociado__usuario__username=usr))
    lenguajes_por_usuario = list(HabilidadesLenguajes.objects.filter(asociado__usuario__username=usr))
    idiomas_por_usuario = list(HabilidadesIdiomas.objects.filter(asociado__usuario__username=usr))
    cursos_por_usuario = list(CursosCapacitaciones.objects.filter(asociado__usuario__username=usr))
    proyectos_por_usuario = list(Proyecto.objects.filter(autor__usuario__username=usr))

    usuario_id = asociado_por_usuario[0].usuario.id
    nombre = asociado_por_usuario[0].get_nombre_completo

    return render(request, "asociados/asociados.html",{ 'asociado' : asociado_por_usuario,
                                                        'redes_sociales' : redes_sociales_por_usuario,
                                                        'experiencialab' : experiencia_lab_por_usuario,
                                                        'educacion' : educacion_por_usuario,
                                                        'habilidades' : habilidades_por_usuario,
                                                        'lenguajes' : lenguajes_por_usuario,
                                                        'idiomas' : idiomas_por_usuario,
                                                        'cursos' : cursos_por_usuario,
                                                        'id_usuario' : usuario_id,
                                                        'nombre' : nombre,
                                                        'proyectos' : proyectos_por_usuario})

def show_proyecto(request,usr,proy):
    proyectos_por_id = Proyecto.objects.filter(pk=proy)
    nombre = proyectos_por_id[0].get_nombre

    context={'proyecto':proyectos_por_id,
            'nombre':nombre}

    return render(request,"proyectos/tmpl_proyectos.html",context)
