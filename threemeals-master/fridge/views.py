from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from myblog.views import LoginRequiredMixin

from fridge.models import Ingredient
from rest_framework import viewsets
from fridge.serializers import IngredientSerializer

class FridgeHomeView(TemplateView):
    template_name = 'fridge/recom_list.html'

class IngredientHomeView(TemplateView):
    template_name = 'fridge/ingredient_list.html'

class ScrapHomeView(TemplateView):
    template_name = 'fridge/scrap_list.html'

class ShoppingHomeView(TemplateView):
    template_name = 'fridge/shopping_memo.html'

class AddIngredient(TemplateView):
	template_name = 'fridge/addingredient.html'
	
	def get_ingre(self):
		ingredient_type = int(self.request.GET.get('type') or '0')
		if ingredient_type == 0:
			ingredients = Ingredient.objects.all()
		else:
			ingredients = Ingredient.objects.filter(type=ingredient_type)
		context = {'ingredients': ingredients}
		return context

class IngredientViewSet(viewsets.ModelViewSet):
	queryset = Ingredient.objects.all()
	serializer_class = IngredientSerializer
	lookup_field = 'type'


	def get_queryset(self):
		ingredient_type = int(self.request.GET.get('type') or '0')
		if ingredient_type == 0:
			ingredients = Ingredient.objects.all()
		else:
			ingredients = Ingredient.objects.filter(type=ingredient_type)

		queryset = ingredients
		return queryset



# class MealCreateView(LoginRequiredMixin, CreateView):
#     model = MealPref
#     fields = ['morning', 'lunch', 'dinner']
#     success_url = reverse_lazy('mealpref:index')
#     def form_valid(self, form):
#         form.instance.pref_user = self.request.user
#         return super(MealCreateView, self).form_valid(form)
#
# class MealChangeLV(LoginRequiredMixin, ListView):
#     template_name = 'mealpref/mealpref_change_list.html'
#
#     def get_queryset(self):
#         return MealPref.objects.filter(pref_user=self.request.user)
#
# class MealUpdateView(LoginRequiredMixin, UpdateView):
#     model = MealPref
#     fields = ['morning', 'lunch', 'dinner']
#     success_url = reverse_lazy('mealpref:index')
#
# class MealDeleteView(LoginRequiredMixin, DeleteView):
#     model = MealPref
#     success_url = reverse_lazy('mealpref:index')

