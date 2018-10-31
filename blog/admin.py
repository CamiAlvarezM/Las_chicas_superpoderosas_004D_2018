from django.contrib import admin
from .models import Post, Perritos
from .models import Perfil

admin.site.register(Post)
admin.site.register(Perritos)

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'bio', 'web')