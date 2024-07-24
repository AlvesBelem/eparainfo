from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

@admin.register(ImageItemEstoque)
class ImageUploadAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'image', 'uploaded_at')

    def image_tag(self, obj):
        if obj.image:
            # Ajuste a URL para incluir o protocolo correto
            return mark_safe(f'<img src="{obj.image.url}" width="100" height="80" />')
        return "-"
    image_tag.short_description = 'Image'
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Categoria)
admin.site.register(Tipo)
admin.site.register(Marca)
admin.site.register(Mram)
admin.site.register(Armazenamento)
admin.site.register(Processador)
admin.site.register(Produto)
admin.site.register(ItemEstoque)
admin.site.register(Endereco)
admin.site.register(Pedido)
admin.site.register(ItensPedido)
admin.site.register(BannerGrid)
admin.site.register(Cor)
admin.site.register(Pagamento)
admin.site.register(BannerPrincipal)
admin.site.register(BannerIndividual)

# Register your models here.
