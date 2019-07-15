# [Django - Unit Testing - Part 4](https://www.youtube.com/watch?v=uk1ij07cKLA&t=11s)

Fixtures can be used to eliminate repeating elements in tests, for ex.\
Before
```
class TestAuth(TestCase):
    
    @classmethod
    def setUpClass(cls):
        super(TestViews, cls).setUpClass()
        mixer.blend('item')
        cls.factory = RequestFactory()

    def test1():
        request = cls.factory.get(path)
        assert statement

    def test2():
        request = cls.factory.get(path)
        assert statement
```

After
```
@pytest.fixture(scope='module')
def factory():
    return RequestFactory()

@pytest.fixture
def item(db):
    return mixer.blend('item')

def test1(factory, item):
    request = cls.factory.get(path)
    assert statement

def test2(factory, item):
    request = cls.factory.get(path)
    assert statement
```

- `scope=module` prevents a new factory reduces overhead by preventing a new factory to be instantied for each test
- passing `db` to the mixer gives access to the db instead of having to specify the `@pytest.mark.django_db` at the beginning of the class

Another example of Fixtures

Before
```
def test_product_is_in_stock(product):
    product = mixer.blend('products.Product', quantity=1)
    assert product.is_in_stock == True


def test_product_is_not_in_stock(product):
    product = mixer.blend('products.Product', quantity=1)
    assert product.is_in_stock == False
```
After
```
@pytest.fixture
def item(request, db):
    return mixer.blend('item', quant=request.param)

@pytest.mark.parametrize('item', [1], indirect=True)
def test_in_stock(item):
    assert item.in_stock == True


@pytest.mark.parametrize('item', [0], indirect=True)
def test_not_in_stock(item):
    assert item.in_stock == False
```

- parameters can be specified to the fixture for alternating cases
using the same mock object
- `indirect` if True means that access to parameters can be obtained from other fixtures. If it were set to False, could not query `in_stock` attribute of item