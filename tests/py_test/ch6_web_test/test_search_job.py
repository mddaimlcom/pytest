from ..helpers import EndavaPo as EN

# module level variables
browser_args = {
    'executable_path': '~/WebDrivers/geckodriver',
    "cookies": '/tests/py_test/data_artifacts/endava_cookies.pkl',
    "domain_url": 'https://www.endava.com'
}


urls = dict(
    homepage='https://www.endava.com/',
    career='https://careers.endava.com/en',
    job_search='https://careers.endava.com/en/Search-Job',
)


# actual tests
def test_career_page_redirect(browser):
    browser_handler = EN.EndavaHomePage(browser)
    browser_handler.nav(urls.get('homepage'))
    browser_handler.menu_button.click()
    browser_handler.careers_btn.click()
    assert urls.get('career') in browser_handler.current_url, f'Redirect to {urls.get("career")} has not happened, ' \
                                                            f'current url {browser_handler.current_url}'


def test_career_search_redirect(browser):
    browser_handler = EN.EndavaCareersPage(browser)
    browser_handler.nav(urls.get('career'))
    browser_handler.job_search_btn.click()
    assert urls.get("job_search") in browser_handler.current_url, f'Redirect to {urls.get("job_search")} did not happen' \
                                                               f' current page {browser_handler.current_url}'


def test_job_search(browser):
    browser_handler = EN.EndavaJobSearchPage(browser)
    browser_handler.nav(urls.get("job_search"))
    browser_handler.search_job_by_name('Senior QA Engineer')
    num_listed_job_posts = len(browser_handler.jobs_listed) # actual job_posts_listed
    expected_job_posts = 11 # expected job posts
    assert num_listed_job_posts >= expected_job_posts, f'Expected at least 11 jobs posts, got instead {num_listed_job_posts}'
