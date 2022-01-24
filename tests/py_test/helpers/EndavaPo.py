from .PO import AbstractPage


class EndavaHomePage(AbstractPage):

    _implicit_element_wait = 5
    
    @property
    def menu_button(self):
        return self.find_by_xpath('//a[@id="menu-toggle"]')
    
    @property
    def about_btn(self):
        return self.find_by_xpath('//a[@href="/en/About"]')

    @property
    def contact_btn(self):
        return self.find_by_xpath('//a[@href="/en/Contact"]')

    @property
    def capabilities_btn(self):
        return self.find_by_xpath('//a[@href="/en/Capabilities"]')

    @property
    def careers_btn(self):
        return self.find_by_xpath('//a[@href="https://careers.endava.com/en"]')

    @property
    def cookie_accept_button(self):
        return self.wait_for_element('//button[@id="onetrust-accept-btn-handler"]')

    def handle_cooki_question(self):
        if self.cookie_accept_button:
            self.cookie_accept_button.click()
            self.static_wait(1)


class EndavaAboutPage(EndavaHomePage):
    pass


class EndavaContactPage(EndavaHomePage):
    pass


class EndavaCapabilitiestPage(EndavaHomePage):
    pass


class EndavaCareersPage(EndavaHomePage):

    @property
    def job_search_btn(self):
        return self.find_by_xpath('//a[@href="/en/Search-Job"]')


class EndavaJobSearchPage(EndavaHomePage):

    @property
    def job_input_filed(self):
        return self.find_by_xpath('//input[@name="search"]')

    @property
    def search_btn(self):
        return self.find_by_xpath('//button[@onclick="performJobsSearchFn();"]')

    @property
    def _location_filter_field(self):
        return self.find_by_xpath('//div[@class="form-group"][2]/span/span/span')

    @property
    def jobs_listed(self):
        job_elements = self.find_elements('//ul[@id="jobs"]/li')
        return [el.text for el in job_elements]

    def filter_by_location(self, text):
        self._location_filter_field.click()  # click on field in order to see the dropdown list of regions
        _el = self.find_by_xpath('//span/ul[@role="listbox"]/li[contains(text(), "{region}")]'.format(region=text))
        _el.click()

    def search_job_by_name(self, job_name):
        self.job_input_filed.send_keys(job_name)
        self.search_btn.click()
        self.static_wait(2)




