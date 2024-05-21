import os
from pytest_django.live_server_helper import LiveServer
from playwright.sync_api import expect, Browser

os.environ.setdefault("DJANGO_ALLOW_ASYNC_UNSAFE", "true")


def test_smoke(live_server: LiveServer, browser: Browser):
    page = browser.new_page(base_url=str(live_server))
    page.goto("/")
    expect(page).to_have_title("Demo App")
