from django.contrib import admin
from .models import Article

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'publish', 'status')
	list_filter = ('publish', 'status')
	search_fields = ('title', 'description')
	#slug o khodkar misaze
	prepopulated_fields = {'slug': ('title',)}
	#- nozoli order mikone
	ordering = ['status', '-publish']

admin.site.register(Article, ArticleAdmin)