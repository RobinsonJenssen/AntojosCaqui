from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/api/', include("Productos.urls")),
    path('users/api/', include('Usuarios.urls')),
    path("cart/api/", include("carrito.urls")),
]
