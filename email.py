import time
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    page = browser.new_page()
    page.goto("https://i.ua")
    page.set_default_timeout(5000)
    inputs = page.locator(
        selector="input[name='login']"
    )
    inputs.fill('xxx')
    # page.wait_for_timeout(1000)
    time.sleep(1)
    inputs = page.locator(
        selector="input[name='pass']"
    )
    inputs.fill('xxx')
    time.sleep(1)

    enter = page.locator(selector="input[value='Увійти']")
    enter.click()
    time.sleep(1)

    letter = page.locator('//a[text()="Создать письмо"]')
    letter.nth(1).click()
    time.sleep(1)

    address = page.locator(selector='textarea[id="to"]')
    address.fill('swarovsky@i.ua')
    time.sleep(1)

    address = page.locator(selector='input[name="subject"]')
    address.fill('hello!')
    time.sleep(1)

    address = page.locator(selector='textarea[id="text"]')
    address.fill('lucky')
    time.sleep(1)

    checkbox = page.locator(selector='input[name="req"]')
    checkbox.nth(1).click()

    time.sleep(1)

    send = page.locator('//p[@class="send_container clear"]/input[@name="send"]')
    send.click()
    time.sleep(1)



    new_page = browser.new_page()
    new_page.goto("https://i.ua")
    new_page.set_default_timeout(5000)

    inputs = new_page.locator('input[name="login"]')
    inputs.fill('yyy')
    time.sleep(1)
    inputs = new_page.locator('input[name="pass"]')
    inputs.fill('yyy')
    time.sleep(1)

    enter_me = new_page.locator('input[value="Увійти"]')
    enter_me.click()

    receive = new_page.locator('//div[@class="row new"]//a').nth(0)
    receive.wait_for(state="visible")

    time.sleep(1)

    with new_page.expect_event("dialog") as dialog_info:
        receive.click(timeout=15000)

    dialog = dialog_info.value
    dialog.accept()
    time.sleep(2)

    answer = new_page.locator(
        '//div[@class="Right"]//div[@class="block_gamma_bg toolbar"]//a[@class="button tl_bl reply"]')
    answer.nth(0).click()
    time.sleep(2)

    letter_back = new_page.locator('//div[@class="text_editor_browser"]//textarea')
    letter_back.fill('lucky too!')

    send_button = new_page.locator('//p[@class="send_container"]//input[@value="Отправить"]')
    send_button.click()
    time.sleep(2)

    third_page = browser.new_page()
    third_page.goto("https://i.ua")
    third_page.set_default_timeout(5000)
    inputs = third_page.locator(
        selector="input[name='login']"
    )
    inputs.fill('xxx')
    time.sleep(1)
    inputs = third_page.locator(
        selector="input[name='pass']"
    )
    inputs.fill('xxx')
    time.sleep(1)

    enter = third_page.locator(selector="input[value='Увійти']")
    enter.click()
    time.sleep(2)

    receive_2 = third_page.locator('//div[@class="row new"]//a').nth(0)
    receive_2.wait_for(state="visible")
    receive_2.nth(0).click()
    time.sleep(3)
