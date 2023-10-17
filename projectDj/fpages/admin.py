from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import gettext_lazy as _


# Define a new FlatPageAdmin
class FlatPageAdmin(FlatPageAdmin):
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites')}),
        (_('Advanced options'), {
            'classes': ('collapse',),
            'fields': (
                'enable_comments',
                'registration_required',
                'template_name',
            ),
        }),
    )


# Re-register FlatPageAdmin
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)


# <!DOCTYPE html>
# <html lang="en">
#     <head>
#         <meta charset="utf-8" />
#         <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
#         <meta name="description" content="" />
#         <meta name="author" content="" />
#         <title>Bare - Start Bootstrap Template</title>
#         <!-- Favicon-->
#         <link rel="icon" type="image/x-icon" href="assets/favicon.ico" />
#         <!-- Core theme CSS (includes Bootstrap)-->
#         {% load static %}
#         <link href="{% static 'css/styles.css' %}" rel="stylesheet" />
#     </head>
#     <body>
#     <!-- Responsive navbar-->
#     <nav class="navbar navbar-expand-lg navbar-dark bg-dark static-top">
#         <div class="container">
#             <a class="navbar-brand" href="#">Django flatpages</a>
#             <button class="navbar-toggler" type="button" data-toggler="collapse"
#                     data-target="navbarResponsive"
#                     aria-controls="navbarResponsiv" aria-expanded="false"
#                     aria-label="Toggle navigation">
#                 <span class="navbar-toggler-icon"></span>
#             </button>
#             <div class="collapse navbar-collapse" id="navbarResponsive">
#                 <ul class="navbar-nav ml-auto">
#                     <li class="nav-item active">
#                         <a class="nav-link" href="#">Home
#                             <span class="sr-only">(current)</span>
#                         </a>
#                     </li>
#                     <li class="nav-item">
#                         <a class="nav-link" href="/about/">About</a>
#                     </li>
#                     <li class="nav-item">
#                         <a class="nav-link" href="/contacts/">Contact</a>
#                     </li>
#                 </ul>
#             </div>
#         </div>
#     </nav>
#     <!-- Page content-->
#     <div class="container">
#         <div class="row">
#             <div class="col-lg-12 text-center">
#                 {% block content %}
#                 {% endblock content %}
#             </div>
#         </div>
#     </div>
#     </body>
# </html>
