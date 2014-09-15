from django.contrib import admin
from masays.models import Wisdom
# Register your models here.

class WisdomAdmin(admin.ModelAdmin):
	fields = ['pub_date', 'wisdom_text']
	list_display = ('wisdom_text', 'pub_date')
	list_filter = ['pub_date']
	search_fields = ['wisdom_text']

admin.site.register(Wisdom, WisdomAdmin)