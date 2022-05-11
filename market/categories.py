from market.models import Categories

def categories_all(request):
    categories = Categories.objects.filter(parent=None)
    return {'categories':categories}