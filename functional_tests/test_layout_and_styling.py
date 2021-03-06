from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys

class LayoutAndSytlingTest(FunctionalTest):
    def test_layout_and_styling(self):
        # Edith goes to the home page
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(720, 1024)


        # She notices the input box is nicely centered
        inputbox = self.get_item_input_box()
        #print(inputbox.location)
        self.assertAlmostEqual(
             inputbox.location['x'] + inputbox.size['width'] / 2,
             360,
             delta=10
        )
        # She starts a new list and the input box is nicely
        # centered there too
        inputbox.send_keys('testing')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: testing')

        inputbox = self.get_item_input_box()
        self.assertAlmostEqual(
             inputbox.location['x'] + inputbox.size['width'] / 2,
             360,
             delta=6
        )


