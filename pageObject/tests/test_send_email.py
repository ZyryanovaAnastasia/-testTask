from pageObject.pages.main_page import MainPage
from pageObject.pages.email_page import EmailPage


def test_send_email(browser):
    email = 'testovaya.pochta.21'
    password = 'test124578'
    contact_email = 'test@mail.ru'
    body_email = ('Вышел тестер из тумана,\n'
                  'Вынул багу из кармана:\n'
                  '"Буду резать, буду бить,\n'
                  'Все равно вам не внедрить!"')

    main_page = MainPage(browser)
    email_page = EmailPage(browser)

    main_page.open_main_page()
    main_page.fill_login(email)
    main_page.click_btn_enter_password()
    main_page.fill_password(password)
    main_page.click_btn_login()

    email_page.click_btn_new_email()
    email_page.fill_contact(contact_email)
    email_page.fill_body_email(body_email)
    email_page.click_btn_send_email()