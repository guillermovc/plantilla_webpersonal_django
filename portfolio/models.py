from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripción")
    image =  models.ImageField(verbose_name="Imagen", upload_to="projects")
    more_info_url = models.URLField(verbose_name="Enlace más información", null=True, blank=True)

    # Django esconde estos campos por defecto, se pueden mostrar en admin.py
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    # Nombre en español y otros metadatos
    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos" # Por defecto solo añade una s al final de verbose_name
        ordering = ["-created"]  # Cómo ordenar los proyectos (el menos es para reversed)

    # Para que en el admin se muestre el titulo del proyecto y no Project object(1)
    def __str__(self):
        return self.title