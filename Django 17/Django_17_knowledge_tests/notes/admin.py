from django.contrib import admin

from notes.models import Note, Category, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'created_at', 'updated_at')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'content', 'author__username')
    autocomplete_fields = ('author', 'category')
    filter_horizontal = ('tags',)
    readonly_fields = ('created_at', 'updated_at')



# ============================================================
# Django Admin - Основные настройки ModelAdmin
# ============================================================

# list_display
# Определяет столбцы, которые будут отображаться в списке объектов
# в административной панели.
# list_display = ("id", "title", "author", "created_at")


# list_display_links
# Определяет, какие столбцы в списке будут ссылками
# на страницу редактирования объекта.
# list_display_links = ("id", "title")


# list_filter
# Добавляет панель фильтрации в правой части административной панели.
# list_filter = ("category", "created_at")


# search_fields
# Добавляет возможность поиска в административной панели.
# search_fields = ("title", "content", "author__username")


# ordering
# Определяет порядок отображения объектов.
# "-" означает сортировку по убыванию.
# ordering = ("-created_at",)


# readonly_fields
# Определяет поля, которые отображаются,
# но не могут быть изменены.
# readonly_fields = ("created_at", "updated_at")


# fields
# Определяет, какие поля и в каком порядке будут отображаться
# на странице создания/редактирования объекта.
# fields = ("title", "content", "category", "tags")


# exclude
# Определяет поля, которые не будут отображаться
# на странице создания/редактирования объекта.
# exclude = ("author",)


# fieldsets
# Позволяет группировать поля и разделять их на секции.


# filter_horizontal
# Создаёт удобный горизонтальный интерфейс выбора
# для ManyToManyField.
# filter_horizontal = ("tags",)


# filter_vertical
# Создаёт вертикальный интерфейс выбора
# для ManyToManyField.
# filter_vertical = ("tags",)


# prepopulated_fields
# Автоматически создаёт значение одного поля
# на основе значения другого поля.
# В основном используется для создания slug.
# prepopulated_fields = {"slug": ("name",)}


# autocomplete_fields
# Добавляет поиск с автодополнением
# для ForeignKey и ManyToManyField.
# autocomplete_fields = ("author", "tags")


# raw_id_fields
# Отображает выбор ForeignKey / ManyToManyField
# через ID объектов.
# Полезно при большом количестве данных.
# raw_id_fields = ("author",)


# date_hierarchy
# Добавляет в верхней части страницы навигацию по датам
# на основе указанного поля с датой.
# date_hierarchy = "created_at"


# list_per_page
# Определяет, сколько объектов будет отображаться
# на одной странице списка.
# list_per_page = 20


# list_editable
# Позволяет изменять значения полей прямо в списке объектов,
# не открывая отдельную страницу редактирования.
# list_editable = ("is_published",)


# empty_value_display
# Определяет, как будут отображаться пустые значения (None)
# в административной панели.
# empty_value_display = "—"


# save_on_top
# Дополнительно отображает кнопки Save
# в верхней части страницы редактирования.
# save_on_top = True

