# webapp-testing-kit
Web Application Testing Kit


## Required

- Python 3.6 and up
- Python Selenium module
- chrome Gheko webdriver


## Config
Open up *TextConfig.py* and set up the testing kit as follows:

Set the base app location
```
app_location = 'https://MyWebAppUrl.com/'
```

Add the test to the import list in
```
from tests.MyWebAppTest import MyWebAppTest
```

Add the importet test to the test dictionary
```
self.tests = {
    'search_test': SearchTest,
    'my_web_app_test': MyWebAppTest,
}
```


## Methods

- assert_on_page(self, string)
- assert_not_on_page(string)
- input(self, element_id, input_data)
- input_file(element_id, input_data)
- input_select(element_id)
- press(element_id)
- wait_for_page_to_load()


## Sample test
```
from tests.Test import Test

class SearchTest(Test):

    search_data = {
        'q' : 'Today\'s weather',
    }


    def test(self):
        self.perform_login()


    def perform_login(self):
        url = self.app_location + '/'
        self.driver.get(url)
        self.input('search_form_input_homepage', self.search_data['q'])
        self.press('search_button_homepage')
        self.wait_for_page_to_load()
        self.assert_on_page('results')



```

Defining the method *test()* is mandatory.
