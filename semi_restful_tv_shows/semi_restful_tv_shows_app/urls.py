from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_all_shows),
    # path('<int:show_id>/destroy', views.delete_show),
    # path('<int:show_id>/update', views.update_show),

    path('new', views.add_show_form),
    path('create', views.create_new_show),

    path('<int:show_id>', views.display_show_info),

    path('<int:show_id>/edit', views.edit_show),

]