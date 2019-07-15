# [Django - Unit Testing - Part 2](https://www.youtube.com/watch?v=TzCWadHwdSs)


## **Running Tests**
create `pytest.ini` with configuration settings\
create /test/ along with individual tests for each app directory\
run `py.test`

```
[pytest]
DJANGO_SETTINGS_MODULE = testing.settings
```
---
create test files for models, urls, views

`test_models.py`
```
from mixer.backend.django import mixer

@pytest.mark.django_db 
class TestModels:
    def_product_is_in_stock(self):
        product = mixer.blend('products.Product', quantity=1)
        assert product.is_in_stock == True
```

- mixer allows to quickly mock objects without going through db create()
- decorator gives access to db from pytest

---
`test_urls.py`
- notice that product url created has a name of 'detail' and takes in a args\
`path('<int:pk>', views.product_detail, name='detail')`
- `reverse` grabs a url given a name, you could use `url('absolute\path)` but if a change if url is changed later on in the future, all references need to be updated. instead 
change it in the url file, and maintain the same `name` attribute.
- `resolve` retrieves a given path

```
class TestUrls:
    def test_detail_url(self):
        path = reverse('detail', kwargs={'pk': 1})
        assert resolve(path).view_name == 'detail'
```

(this test is kind of strange, feels pointless/redundant :confused:.
If `reverse` will grab the url where `name=detail`, then won't 
`resolve(...).view_name` obviously be equal to detail?)

---
`test_views.py`

- `RequestFactory` way to black box API and can be passed to a view for testing
- how to test 

```
class TestViews:
    def test_product_detail_authenticated(self):
        mixer.blend('products.Product');
        path = reverse('detail', kwargs={'pk': 1})
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)

        response = product_detail(request, pk=1)
        assert response.status_code == 200
```
how to test anonymous user?
1. use `request.user = AnonmousUser()`
2. the url of the response with a regex: `assert r'accounts/login' in response.url`









