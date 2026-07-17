from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from config import URL
from course import Course


def fetch_courses():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True)

        page = browser.new_page()

        page.goto(URL, wait_until="networkidle")

        soup = BeautifulSoup(page.content(), "html.parser")

        browser.close()

    courses = []

    for card in soup.find_all("article", class_="st"):

        def text(selector):
            tag = card.select_one(selector)
            return tag.get_text(" ", strip=True) if tag else ""

        counts = card.select(".st--section-count")

        section = counts[0].text.strip() if len(counts) > 0 else ""
        seminar = counts[1].text.strip() if len(counts) > 1 else ""

        courses.append(
            Course(
                class_number=text(".st--section-info-wrapper .st--section-number"),
                course=text(".st--section-name"),
                section=section,
                seminar=seminar,
                title=text(".st--title h2"),
                instructor=text(".st--instructors"),
                days=text(".st--meeting-days"),
                time=text(".st--meeting-time"),
                location=text(".st--location"),
                seats=text(".st--seats"),
            )
        )

    return courses