# [Django - Unit Testing - Part 3](https://www.youtube.com/watch?v=LH5U0cOmJgw)

`pytest --cov` will display the coverage in terminal

adding options in pytest.ini can generate an html page with coverages

to omit files, like the massive venv that's in there, create `.coveragerc`
```
[run]
omit = */tests/*
       */migrations/* 
       ../../venv/*
```

- one measurement of test coverage is if functions within models, views, url, etc. are called
    - for example if the authentication tests in `/tests/test_views.py` were removed, then the `product_detail`
    function inside `views.py` would not be run at all, resulting in lower test coverage percentage
    - this also means you won't really need to test the coverage of test files themselves, so they are omitted.


