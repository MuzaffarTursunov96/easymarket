from market.models import Categories

def categories_all(request):
    categories = Categories.objects.all()
    return {'categories':categories}