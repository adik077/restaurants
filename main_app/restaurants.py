from django.conf import settings

class Cart(object):
    def __init__(self,request):
        self.session = request.session
        restaurants = self.session.get(settings.CART_SESSION_ID)
        if not restaurants:
            restaurants = self.session[settings.CART_SESSION_ID]={}
        self.restaurants = restaurants

    def get_values(self):
        return self.restaurants

    def add(self,id):
        self.restaurants[id]=id
        self.save()

    def clear(self):
        self.restaurants.clear()
        self.save()

    def save(self):
        self.session.modified = True


