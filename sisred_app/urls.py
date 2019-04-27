from django.urls import path
from sisred_app.views import  views_equipo1,views_equipo2,views_equipo3,views_equipo4

urlpatterns = [

    #path('recurso_list/', views_equipo1.recurso_list, name='recurso_list'),
    path('recurso_get/<int:id>', views_equipo1.recurso_get, name='recurso_get'),
    path('recurso_put/', views_equipo1.recurso_put, name='recurso_put'),
    path('recurso_post/', views_equipo1.recurso_post, name='recurso_post'),
    path('fase_byid/<int:id>', views_equipo1.fase_byid, name='fase_byid'),

    path('post_proyecto_red/', views_equipo3.post_proyecto_red, name='agregar_proyecto_red'),
    path('detallered/', views_equipo3.get_detallered, name='detallered'),
    path('detallered/metadata/', views_equipo3.get_detallered_metadata, name='detallered'),
    path('detallered/personas/', views_equipo3.get_detallered_personas, name='detallered'),
    path('detallered/recursos/', views_equipo3.get_detallered_recursos, name='detallered'),
    path('detallered/proyectos/', views_equipo3.get_detallered_proyectosred, name='detallered'),
    path('reds/asignados/<int:id>', views_equipo3.get_reds_asignados, name='reds_asignados'),

    path('getProyectosRED/', views_equipo2.getProyectosRED),
    path('getRecurso/', views_equipo2.getRecurso),
    path('getRED/', views_equipo2.getRED),
    path('asignaciones/', views_equipo2.getAsignaciones),
    path('red/<int:id>/recursos/', views_equipo2.getRecursosRed),
    path('versiones/<int:id>/', views_equipo2.getVerVersion),
    path('versiones/<int:id>/recursos/', views_equipo2.getVerVersionR),
    path('reds/<int:id>/versiones/', views_equipo2.getVersionesRED),
    path('versiones/<int:id>/marcar', views_equipo2.marcarVersion, name='marcarVersion'),
    path('buscarReds/<int:idUsuario>/', views_equipo2.buscarRed, name='reds'),
    path('versiones/', views_equipo2.versiones, name='versiones'),
    path('versiones/<int:id_v>/recursos/<int:id_r>/comentarios/', views_equipo2.comentarioExistente, name='comentarioExistente'),
    path('versiones/<int:id_v>/recursos/<int:id_r>/comentariosnuevos/', views_equipo2.comentarioNuevo, name='comentarioNuevo'),
    path('versiones/<int:id_v>/recursos/<int:id_r>/listacomentarios/<int:id_cm>/', views_equipo2.getListaComentarios, name='getListaComentarios'),

    path('users/', views_equipo4.getAllUser, name='allUsers'),
    path('users/<int:id>/', views_equipo4.getUser, name='getUserId'),
    path('users/add/', views_equipo4.postUser, name='addUser'),
    path('users/update/<int:id>/', views_equipo4.putUser, name='updateUser'),
    path('users/delete/<int:id>/', views_equipo4.deleteUser, name='deleteUser'),
    path('reds/relacionados/<int:id>/', views_equipo4.get_reds_relacionados, name='reds_relacionados'),
    path('getRecurso/<int:id>/', views_equipo4.getRecurso, name='getRecurso'),
    path('getRedDetailRecursos/<int:id>/', views_equipo4.getRedDetailRecursos, name='getRedDetailRecursos'),
    path('getUserAut/', views_equipo4.getUserAut, name='getUserAut'),
    path('update_sisred/', views_equipo4.update_sisred, name='update_sisred'),
    path('reds/', views_equipo4.get_red, name='reds'),
    path('sisred_create/', views_equipo4.sisred_create, name='sisred_create'),
    path('sisred_remove/', views_equipo4.sisred_remove, name='sisred_remove'),
    path('asignaciones/add/', views_equipo4.postRolAsignado, name='addRolAsignado'),
    path('asignaciones/update/<int:id>/', views_equipo4.putRolAsignado, name='putRolAsignado'),
    path('asignaciones/delete/<int:id>/', views_equipo4.deleteRolAsignado, name='deleteRolAsignado'),

]
