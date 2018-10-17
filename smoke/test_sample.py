import pytest
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.common.by import By

url = os.getenv("TEST_URL") or "https://www.schireson.com"
skill_match = {
    "software": "Software Designers\n& Developers",
    "quant": "Quant & Qual\nResearchers",
    "data": "Data Scientists\n& Data Engineers",
    "strategy": "Strategists\n& Innovators"
}


def test_demo(driver):
    driver.get(url)
    verify_homepage_intro(driver)
    verify_open_nav(driver)
    verify_close_nav(driver)


@pytest.allure.step("Verify contents of skills display properly.")
@pytest.mark.parametrize("skill", ["software", "quant", "data", "strategy"])
def test_skills_of_team(driver, skill):
    driver.get(url)
    skill_item = Wait(driver, 10).until(
        EC.visibility_of_element_located((
            By.CLASS_NAME, "skills-item"))
    )
    driver.execute_script("arguments[0].scrollIntoView();", skill_item)
    Wait(driver, 10).until(
        lambda driver: driver.find_element_by_css_selector(
            ".skills-label.FI.animated.fadeIn").text is not None
    )
    skill_title = driver.find_element_by_css_selector(
        ".skills-item." + skill).text
    assert skill_title == skill_match[skill]


@pytest.allure.step("Verify intro works properly.")
def verify_homepage_intro(driver):
    homepage_intro = Wait(driver, 10).until(
        EC.visibility_of_element_located((
            By.CLASS_NAME, "intro"))
    )
    assert homepage_intro.is_displayed()


@pytest.allure.step("Verify open nav works properly.")
def verify_open_nav(driver):
    nav_open_button = Wait(driver, 10).until(
        EC.visibility_of_element_located((
            By.ID, "nav-open"))
    )
    assert nav_open_button.is_displayed()
    nav_open_button.click()
    nav_links = Wait(driver, 10).until(
        EC.visibility_of_element_located((
            By.CLASS_NAME, "nav-panel-links"))
    )
    assert nav_links.is_displayed()


@pytest.allure.step("Verify close nav works properly.")
def verify_close_nav(driver):
    nav_close_button = Wait(driver, 10).until(
        EC.visibility_of_element_located((
            By.ID, "nav-close"))
    )
    assert nav_close_button.is_displayed()
    nav_close_button.click()
    nav_links = Wait(driver, 10).until(
        EC.invisibility_of_element_located((
            By.CLASS_NAME, "nav-panel-links"))
    )
    assert not nav_links.is_displayed()
