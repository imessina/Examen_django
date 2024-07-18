from django.urls import path
from .views import index, crud,alumnos_findEdit
from galeria import views
from .views import ArticuloListView, ArticuloCreateView, ArticuloUpdateView, ArticuloDeleteView
from .views import verificar_articulos
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [

    #LoginLogout
    path('login/', auth_views.LoginView.as_view(template_name='galeria/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('tipos_productos/', views.lista_tipos_productos, name='lista_tipos_productos'),
    path('tipos_productos/crear/', views.crear_tipo_producto, name='crear_tipo_producto'),
    path('tipos_productos/editar/<int:id>/', views.editar_tipo_producto, name='editar_tipo_producto'),
    path('tipos_productos/eliminar/<int:id>/', views.eliminar_tipo_producto, name='eliminar_tipo_producto'),
    path('proveedores/', views.lista_proveedores, name='lista_proveedores'),
    path('proveedores/crear/', views.crear_proveedor, name='crear_proveedor'),
    path('proveedores/editar/<int:id>/', views.editar_proveedor, name='editar_proveedor'),
    path('proveedores/eliminar/<int:id>/', views.eliminar_proveedor, name='eliminar_proveedor'),
    path('crud/', views.crud, name='crud'),
    path('crud_generos/', views.crud_generos, name='crud_generos'),
    path('articulos/', views.articulos, name='articulos'),
    path('articulos/crear/', views.crear_articulo, name='crear_articulo'),
    path('articulos/editar/<int:id>/', views.editar_articulo, name='editar_articulo'),
    path('articulos/eliminar/<int:id>/', views.eliminar_articulo, name='eliminar_articulo'),


    #Login
    path('login/', auth_views.LoginView.as_view(template_name='galeria/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    #Htmls
    path('', views.index, name='index'),
    path('anime/', views.anime, name='anime'),
    path('games/', views.games, name='games'),
    path('contacto/', views.contacto, name='contacto'),
    path('comprar/', views.comprar, name='comprar'),
    path('polera1/', views.polera1, name='polera1'),
    path('polera2/', views.polera2, name='polera2'),
    path('polera3/', views.polera3, name='polera3'),
    path('polera4/', views.polera4, name='polera4'),
    path('api/', views.api, name='api'),
    path('rock/', views.rock, name='rock'),
    
    #clientes

    path('clientes/', views.cliente_lista, name='cliente_lista'),
    path('clientes/<int:pk>/', views.cliente_detalle, name='cliente_detalle'),
    path('clientes/nuevo/', views.cliente_crear, name='cliente_crear'),
    path('clientes/<int:pk>/editar/', views.cliente_editar, name='cliente_editar'),
    path('clientes/<int:pk>/eliminar/', views.cliente_eliminar, name='cliente_eliminar'),

    #contacto
    path('contacto/', views.contacto_crear, name='contacto_crear'),
    path('contacto/exito/', views.contacto_exito, name='contacto_exito'),
    path('contactos/', views.contacto_lista, name='contacto_lista'),


    #Crud

    path('crud', views.crud, name='crud'),
    path('galeria/alumnosAdd', views.alumnosAdd, name='alumnosAdd'),
    path('galeria/alumnos_del/<str:pk>', views.alumnos_del, name='alumnos_del'),
    path('galeria/alumnos_findEdit/<str:pk>', views.alumnos_findEdit, name='alumnos_findEdit'),
    path('galeria/alumnosUpdate', views.alumnosUpdate, name='alumnosUpdate'),

    path('crud_generos', views.crud_generos, name='crud_generos'),
    path('generosAdd', views.generosAdd, name='generosAdd'),
    path('generos_del/<str:pk>', views.generos_del, name='generos_del'),
    path('generos_edit/<str:pk>', views.generos_edit, name='generos_edit'),
    path('galeria/alumnosAdd/', views.alumnosAdd, name='alumnos_add'),
    
    #articulos (Productos)
    path('articulos/', ArticuloListView.as_view(), name='articulo-list'),
    path('articulos/new/', ArticuloCreateView.as_view(), name='articulo-create'),
    path('articulos/<str:pk>/edit/', ArticuloUpdateView.as_view(), name='articulo-update'),
    path('articulos/<str:pk>/delete/', ArticuloDeleteView.as_view(), name='articulo-delete'),
    path('verificar_articulos/', verificar_articulos, name='verificar-articulos'),


    #Tipoprod
    path('tipos_productos/', views.lista_tipos_productos, name='lista_tipos_productos'),
    path('tipos_productos/crear/', views.crear_tipo_producto, name='crear_tipo_producto'),
    path('tipos_productos/editar/<int:id>/', views.editar_tipo_producto, name='editar_tipo_producto'),
    path('tipos_productos/eliminar/<int:id>/', views.eliminar_tipo_producto, name='eliminar_tipo_producto'),

    #Proveedores

    path('proveedores/', views.lista_proveedores, name='lista_proveedores'),
    path('proveedores/crear/', views.crear_proveedor, name='crear_proveedor'),
    path('proveedores/editar/<int:id>/', views.editar_proveedor, name='editar_proveedor'),
    path('proveedores/eliminar/<int:id>/', views.eliminar_proveedor, name='eliminar_proveedor'),


    #Tienda
    path('', views.index, name='index'),
    path('store/', views.store, name='store'),



]

