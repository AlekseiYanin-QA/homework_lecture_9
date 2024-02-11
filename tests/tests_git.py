from selene import browser, be, by
import allure
from allure_commons.types import Severity


# Чистый тест на Selene
def test_git_issue_clear_selene():
    browser.open('https://github.com/')
    browser.element('.header-search-button').click()
    browser.element("#query-builder-test").send_keys("AlekseiYanin-QA/homework_lecture_7")
    browser.element("#query-builder-test").submit()
    browser.element(by.link_text('AlekseiYanin-QA/homework_lecture_7')).click()
    browser.element('#issues-tab').click()
    browser.element(by.partial_text('Issues are used to track todos, bugs, feature requests, and more')) \
        .should(be.visible)
    allure.dynamic.severity(Severity.BLOCKER)


# Шаги с декоратором @allure.step
@allure.severity(Severity.CRITICAL)
@allure.tag("web")
@allure.feature("Git's Issue")
@allure.story("Пользователь видит Issue")
@allure.link("https://github.com", name="Testing")
def test_git_issue_allure_step():
    with allure.step("Открываем главую страницу GitHub"):
        browser.open('https://github.com/')

    with allure.step("Ищем репозиторий"):
        browser.element('.header-search-button').click()
        browser.element('#query-builder-test').type('AlekseiYanin-QA/homework_lecture_7').press_enter()
        browser.element(by.link_text('AlekseiYanin-QA/homework_lecture_7')).click()

    with allure.step("Ищем Issues"):
        browser.element('#issues-tab').click()

    with allure.step("Проверяем Issues"):
        browser.element(by.partial_text('Issues are used to track todos, bugs, feature requests, and more'))\
            .should(be.visible)


# Тест с Лямбда-шагами
def test_git_issue_lambda_allure_steps():
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.tag("web")
    allure.dynamic.feature("Git's Issue")
    allure.dynamic.story("Пользователь видит Issue")
    allure.dynamic.link("https://github.com", name="Testing")
    open_main_github_page()
    find_repository()
    find_issues_button()
    check_issues()


@allure.step("Открываем главную страницу Github")
def open_main_github_page():
    browser.open('https://github.com/')


@allure.step("Ищем репозиторий")
def find_repository():
    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').type('AlekseiYanin-QA/homework_lecture_7').press_enter()
    browser.element(by.link_text('AlekseiYanin-QA/homework_lecture_7')).click()


@allure.step("Ищем репозиторий")
def find_issues_button():
    browser.element('#issues-tab').click()


@allure.step("Ищем репозиторий")
def check_issues():
    browser.element(by.partial_text('Issues are used to track todos, bugs, feature requests, and more'))\
        .should(be.visible)