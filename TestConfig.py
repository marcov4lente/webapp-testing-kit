
class TestConfig:

    app_location = 'https://duckduckgo.com/'


    def import_tests(self):
        from tests.SearchTest import SearchTest

        self.tests = {
            'search_test': SearchTest,
        }
