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


