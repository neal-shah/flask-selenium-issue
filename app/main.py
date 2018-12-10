from flask import Flask
from app.utils import get_driver, connect_to_base
from time import sleep
app = Flask(__name__)


def run_process(browser, page_number=1):
    if connect_to_base(browser, page_number):
        print(f'Scraping page {page_number}...')
        sleep(0.1)
        html = browser.page_source
        return html
    else:
        return False


@app.route("/")
def hello():
    browser = get_driver()
    data = run_process(browser, 1)
    browser.quit()
    if data:
        return data
    else:
        return "Nope"


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=False, port=80)
