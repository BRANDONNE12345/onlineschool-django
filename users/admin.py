from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User

    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_active', 'is_staff')
    list_filter = ('role', 'is_staff', 'is_active','is_approved')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

    # Organisation des champs dans le formulaire de modification
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informations personnelles', {'fields': ('first_name', 'last_name', 'email')}),
        ('Rôle utilisateur', {'fields': ('role',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Dates importantes', {'fields': ('last_login', 'date_joined')}),
    )
    # Organisation lors de la création d'un utilisateur
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 'role', 'password1', 'password2'),
        }),
    )

    # Actions personnalisées pour modifier en masse le rôle d'utilisateurs
    actions = ['set_as_teacher', 'set_as_student', 'set_as_scolarite', 'set_as_compta', 'set_as_admin']

    def set_as_teacher(self, request, queryset):
        updated = queryset.update(role='ENSEIGNANT')
        self.message_user(request, f"{updated} utilisateur(s) mis à jour en tant qu'enseignant(s).")
    set_as_teacher.short_description = "Définir comme Enseignant"

    def set_as_student(self, request, queryset):
        updated = queryset.update(role='ETUDIANT')
        self.message_user(request, f"{updated} utilisateur(s) mis à jour en tant qu'étudiant(s).")
    set_as_student.short_description = "Définir comme Étudiant"

    def set_as_scolarite(self, request, queryset):
        updated = queryset.update(role='SCOLARITE')
        self.message_user(request, f"{updated} utilisateur(s) mis à jour en tant que Responsable de scolarité.")
    set_as_scolarite.short_description = "Définir comme Responsable de scolarité"

    def set_as_compta(self, request, queryset):
        updated = queryset.update(role='COMPTA')
        self.message_user(request, f"{updated} utilisateur(s) mis à jour en tant que Comptabilité.")
    set_as_compta.short_description = "Définir comme Comptabilité"

    def set_as_admin(self, request, queryset):
        updated = queryset.update(role='ADMIN', is_staff=True, is_superuser=True)
        self.message_user(request, f"{updated} utilisateur(s) mis à jour en tant qu'Administrateur.")
    set_as_admin.short_description = "Définir comme Administrateur"
    def approve_users(self, request, queryset):
        queryset.update(is_approved=True)
    approve_users.short_description = "Approuver les utilisateurs sélectionnés"
admin.site.register(User, CustomUserAdmin)
