from django.shortcuts import render, get_object_or_404, redirect
from .forms import ClienteForm, ContactoForm
from .models import Cliente, Contacto
import logging
from .models import Alumno, Genero
from datetime import datetime
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Articulo
from .forms import ArticuloForm
from django.urls import reverse_lazy
from .forms import GeneroForm
from .models import TipoProducto
from .forms import TipoProductoForm
from django.shortcuts import render, redirect
from .models import Proveedor
from .forms import ProveedorForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

#from django.shortcuts import render, redirect

#logger = logging.getLogger(__name__) #Para validar si los datos se guardan de forma correcta


def dashboard(request):
    return render(request, 'galeria/dashboard.html')

def index(request):
    return render(request, 'galeria/index.html')

def anime(request):
    return render(request, 'galeria/anime.html')

def games(request):
    return render(request, 'galeria/games.html')

def contacto(request):
    return render(request, 'galeria/contacto.html')

def comprar(request):
    return render(request, 'galeria/comprar.html')

def polera1(request):
    return render(request, 'galeria/polera1.html')

def polera2(request):
    return render(request, 'galeria/polera2.html')

def polera3(request):
    return render(request, 'galeria/polera3.html')

def polera4(request):
    return render(request, 'galeria/polera4.html')

def api(request):
    return render(request, 'galeria/api.html')

def rock(request):
    return render(request, 'galeria/rock.html')

def cliente_lista(request):
    clientes = Cliente.objects.all()
    return render(request, 'galeria/cliente_lista.html', {'clientes': clientes})


def cliente_detalle(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'cliente_detalle.html', {'cliente': cliente})

def cliente_crear(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            return redirect('cliente_detalle', pk=cliente.pk)
    else:
        form = ClienteForm()
    return render(request, 'galeria/cliente_formulario.html', {'form': form})


def cliente_editar(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            cliente = form.save()
            return redirect('cliente_detalle', pk=cliente.pk)
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'cliente_formulario.html', {'form': form})

def cliente_eliminar(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        cliente.delete()
        return redirect('cliente_lista')
    return render(request, 'cliente_confirmar_eliminacion.html', {'cliente': cliente})


#crear contacto
def contacto_crear(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacto_exito')
    else:
        form = ContactoForm()
    return render(request, 'galeria/contacto_formulario.html', {'form': form})

def contacto_lista(request):
    contactos = Contacto.objects.all()
    return render(request, 'galeria/contacto_lista.html', {'contactos': contactos})

def contacto_exito(request):
    return render(request, 'galeria/contacto_exito.html')


#prueba
class persona:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
        super().__init__()

def index(request):

    hijo=persona("Juan Perez", "7")

    lista=["Lazaña", "Charquican", "Porotos Granados"]

    alumnos= Alumno.objects.all()

    context={"hijo":hijo, "nombre":"Claudia Andrea", "comidas":lista, "alumnos":alumnos}

    return render(request, 'galeria/index.html', context)

def crud(request):
    alumnos = Alumno.objects.all()
    context = {'alumnos': alumnos}
    return render(request, 'galeria/alumnos_list.html', context)


from django.shortcuts import render, redirect
from .models import Alumno, Genero

def alumnosAdd(request):
    if request.method == "POST":
        # Es un POST, por lo tanto se recuperan los datos del formulario y se graban en la tabla
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        aPaterno = request.POST["paterno"]
        aMaterno = request.POST["materno"]
        fechaNac = request.POST["fechaNac"]
        id_genero = request.POST.get("genero")
        telefono = request.POST["telefono"]
        email = request.POST["email"]
        direccion = request.POST["direccion"]
        activo = True  # Usar True para BooleanField

        genero = Genero.objects.get(id_genero=id_genero)
        
        # Crear un nuevo alumno y guardarlo en la base de datos
        nuevo_alumno = Alumno(
            rut=rut,
            nombre=nombre,
            apellido_paterno=aPaterno,
            apellido_materno=aMaterno,
            fecha_nacimiento=fechaNac,
            genero=genero,  # Asegúrate de que esto coincide con el nombre del campo en tu modelo
            telefono=telefono,
            email=email,
            direccion=direccion,
            activo=activo
        )
        nuevo_alumno.save()
        
        return redirect('crud')  # Redirige a la lista de alumnos después de agregar uno
    
    else:
        # No es un POST, por lo tanto se muestra el formulario para agregar
        generos = Genero.objects.all()
        context = {'generos': generos}
        return render(request, 'galeria/alumnos_add.html', context)

def alumnos_del(request, pk):
    context = {}
    try:
        alumno=Alumno.objects.get(rut=pk)

        alumno.delete()
        mensaje="Bien, datos eliminados..."
        alumnos = Alumno.objects.all()
        context = {'alumnos':alumnos, 'mensaje': mensaje}
        return render(request, 'galeria/alumnos_list.html', context)
    except Alumno.DoesNotExist:
        mensaje="Error, no se encontró el registro..."
        alumnos = Alumno.objects.all()  
        context = {'alumnos':alumnos, 'mensaje': mensaje}
        return render(request, 'galeria/alumnos_list.html', context)
    
def alumnos_findEdit(request, pk):

    if pk!="":
        alumno=Alumno.objects.get(rut=pk)
        generos=Genero.objects.all()

        #print(type(alumno.id_genero.genero))

        context = {'alumno':alumno, 'generos':generos}
        if alumno:
            return render(request, 'galeria/alumnos_edit.html', context)
        else:
            context = {'mensaje': "Error, no se encontró el registro..."}
            return render(request, 'galeria/alumnos_list.html', context)
        


def alumnosUpdate(request):
    if request.method == "POST":
        rut=request.POST["rut"]
        nombre=request.POST["nombre"]
        aPaterno=request.POST["paterno"]
        aMaterno=request.POST["materno"]
        fechaNac=request.POST["fechaNac"]
        genero=request.POST["genero"]
        telefono=request.POST["telefono"]
        email=request.POST["email"]
        direccion=request.POST["direccion"]
        activo="1"

        objGenero=Genero.objects.get(id_genero = genero)

        alumno = Alumno.objects.get(rut=rut)
        alumno.nombre=nombre
        alumno.apellido_paterno=aPaterno
        alumno.apellido_materno=aMaterno
        alumno.fecha_nacimiento = datetime.strptime(fechaNac, "%Y-%m-%d")
        alumno.id_genero = objGenero 
        alumno.telefono=telefono
        alumno.email=email
        alumno.direccion=direccion
        alumno.activo=1
        alumno.save()
        
        generos=Genero.objects.all()
        context = {'mensaje': "Ok, datos actualizados...", 'generos':generos, 'alumno':alumno}
        return render(request, 'galeria/alumnos_edit.html', context)
    else:
        alumnos=Alumno.objects.all()
        context={'alumnos':alumnos}
        return render(request, 'galeria/alumnos_list.html', context)
        

def crud_generos(request):
    generos = Genero.objects.all()
    context = {'generos': generos}
    print('enviando datos generos_list')
    return render(request, "galeria/generos_list.html", context)

def generosAdd(request):
    print("estoy en controlador generosAdd...")
    context = {}
    
    if request.method == "POST":
        print("controlador es un post...")
        form = GeneroForm(request.POST)
        if form.is_valid():
            print("estoy en agregar, is_valid")
            form.save()

            # limpiar form
            form = GeneroForm()
            
            context = {'mensaje': 'Ok, datos grabados...', 'form': form}
            return render(request, "galeria/generos_add.html", context)
    else:
        form = GeneroForm()
        context = {'form': form}
        return render(request, 'galeria/generos_add.html', context)

def generos_del(request, pk):
    mensajes = []
    errores = []
    generos = Genero.objects.all()
    try:
        genero = Genero.objects.get(id_genero=pk)
        context = {}
        if genero:
            genero.delete()
            mensajes.append("Bien, datos eliminados...")
            context = {'generos': generos, 'mensajes': mensajes, 'errores': errores}
            return render(request, 'galeria/generos_list.html', context)
    except:
        print("Error, id no existe...")
        generos = Genero.objects.all()
        mensaje = "Error, id no existe"
        context = {'mensaje': mensaje, 'generos': generos}
        return render(request, 'galeria/generos_list.html', context)
        
def generos_edit(request, pk):
    try:
        genero = Genero.objects.get(id_genero=pk)
        context = {}
        print("Edit encontró el género...")
        if genero:
            if request.method == "POST":
                print("edit, es un POST")
                form = GeneroForm(request.POST, instance=genero)
                if form.is_valid():
                    form.save()
                    mensaje = "Bien, datos actualizados..."
                    print(mensaje)
                    context = {'genero': genero, 'form': form, 'mensaje': mensaje}
                    return render(request, 'galeria/generos_edit.html', context)
            else:
                print("edit, NO es un POST")
                form = GeneroForm(instance=genero)
                mensaje = ""
                context = {'genero': genero, 'form': form, 'mensaje': mensaje}
                return render(request, 'galeria/generos_edit.html', context)
    except Genero.DoesNotExist:
        print("Error, id no existe...")
        generos = Genero.objects.all()
        mensaje = "Error, id no existe"
        context = {'mensaje': mensaje, 'generos': generos}
        return render(request, 'galeria/generos_list.html', context)
    

class ArticuloListView(ListView):
    model = Articulo
    template_name = 'galeria/articulo_list.html'

class ArticuloCreateView(CreateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = 'galeria/articulo_form.html'
    success_url = reverse_lazy('articulo-list')

class ArticuloUpdateView(UpdateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = 'galeria/articulo_form.html'
    success_url = reverse_lazy('articulo-list')

class ArticuloDeleteView(DeleteView):
    model = Articulo
    template_name = 'galeria/articulo_confirm_delete.html'
    success_url = reverse_lazy('articulo-list')

def verificar_articulos(request):
    articulos = Articulo.objects.all()
    return render(request, 'galeria/verificar_articulos.html', {'articulos': articulos})


#Tipo Producto.
def lista_tipos_productos(request):
    tipos_productos = TipoProducto.objects.all()
    return render(request, 'galeria/lista_tipos_productos.html', {'tipos_productos': tipos_productos})

def crear_tipo_producto(request):
    if request.method == 'POST':
        form = TipoProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tipos_productos')
    else:
        form = TipoProductoForm()
    return render(request, 'galeria/crear_tipo_producto.html', {'form': form})

def editar_tipo_producto(request, id):
    tipo_producto = TipoProducto.objects.get(id=id)
    if request.method == 'POST':
        form = TipoProductoForm(request.POST, instance=tipo_producto)
        if form.is_valid():
            form.save()
            return redirect('lista_tipos_productos')
    else:
        form = TipoProductoForm(instance=tipo_producto)
    return render(request, 'galeria/editar_tipo_producto.html', {'form': form})

def eliminar_tipo_producto(request, id):
    tipo_producto = TipoProducto.objects.get(id=id)
    if request.method == 'POST':
        tipo_producto.delete()
        return redirect('lista_tipos_productos')
    return render(request, 'galeria/eliminar_tipo_producto.html', {'tipo_producto': tipo_producto})


# Vista Proveedores
def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'galeria/lista_proveedores.html', {'proveedores': proveedores})

def crear_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_proveedores')
    else:
        form = ProveedorForm()
    return render(request, 'galeria/crear_proveedor.html', {'form': form})

def editar_proveedor(request, id):
    proveedor = Proveedor.objects.get(id=id)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('lista_proveedores')
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, 'galeria/editar_proveedor.html', {'form': form})

def eliminar_proveedor(request, id):
    proveedor = Proveedor.objects.get(id=id)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('lista_proveedores')
    return render(request, 'galeria/eliminar_proveedor.html', {'proveedor': proveedor})


#proteger los crud con login
@login_required
def lista_tipos_productos(request):
    tipos_productos = TipoProducto.objects.all()
    return render(request, 'galeria/lista_tipos_productos.html', {'tipos_productos': tipos_productos})

@login_required
def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'galeria/lista_proveedores.html', {'proveedores': proveedores})

# Asegúrate de proteger también las demás vistas CRUD de la misma manera


#Dhasboard para acceso Crud

@login_required
def dashboard(request):
    return render(request, 'galeria/dashboard.html')


def articulos(request):
    # Asegúrate de que la ruta de la plantilla es correcta
    return render(request, 'galeria/articulo_list.html')


#ArticulosCrud

def articulos(request):
    articulos = Articulo.objects.all()
    return render(request, 'galeria/articulo_list.html', {'articulos': articulos})

def crear_articulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articulos')
    else:
        form = ArticuloForm()
    return render(request, 'galeria/articulo_form.html', {'form': form})

def editar_articulo(request, id):
    articulo = get_object_or_404(Articulo, id=id)
    if request.method == 'POST':
        form = ArticuloForm(request.POST, instance=articulo)
        if form.is_valid():
            form.save()
            return redirect('articulos')
    else:
        form = ArticuloForm(instance=articulo)
    return render(request, 'galeria/articulo_form.html', {'form': form})

def eliminar_articulo(request, id):
    articulo = get_object_or_404(Articulo, id=id)
    if request.method == 'POST':
        articulo.delete()
        return redirect('articulos')
    return render(request, 'galeria/articulo_confirm_delete.html', {'articulo': articulo})


#Tienda

def index(request):
    return render(request, 'galeria/index.html')

def store(request):
    return render(request, 'galeria/store.html')
