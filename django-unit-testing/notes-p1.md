# [Django - Unit Testing - Part 1](https://www.youtube.com/watch?v=B-qYGeLpUtE)


`@property` decorator is sugar syntax for wrapping property with getters and setters

```
@property
def is_in_stock(self):
    return self.quantity > 0
```
---
- html can be returned in views
- pk is private key

`urls.py`
```
url_patterns = [
    path('<int:pk>', views.product_detail, name='detail')
]
```

`views.py`
```
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {{Product: product}})
```

`/template/product_detail.html`
```
<h1>{{ product.name }}</h1>
```

1. when a request comes in at `localhost:8000/1`, pk = 1
2. request is fired off at the views, where the query will search for an object or return a 404
3. that product is `rendered` in the defined html
---
- another way to CRUD on api is using the shell
```
manage.py shell
> from persons.model import Person
> from datetime import datetime
> Person.objects.create(name="Bob", born=datetime.now()).save()
> Person.objects.get(pk=1)
```
---
- `@login_required` decorator can be applied to views 
- from docs:
> If the user isn’t logged in, redirect to settings.LOGIN_URL, passing the current absolute path in the query string. Example: /accounts/login/?next=/polls/3/.
> If the user is logged in, execute the view normally. The view code is free to assume the user is logged in.
---
`pytest` - testing package\
`pytest-django`  - testing plugin specifically for django\
`pytest-cov` - test coverage\
`mixer` - mock data

