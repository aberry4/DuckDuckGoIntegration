import requests
import pytest


url_ddg = "https://api.duckduckgo.com/?q="
q = "presidents+of+the+united+states"
format_json = "&format=json"


@pytest.mark.parametrize("president", ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Jackson", "Van Buren", "Harrison", "Tyler", "Polk", "Taylor", "Fillmore", "Pierce", "Buchanan", "Lincoln", "Johnson", "Grant", "Hayes", "Garfield", "Arthur", "Cleveland", "McKinley", "Roosevelt", "Taft", "Wilson", "Harding", "Coolidge", "Hoover", "Truman", "Eisenhower", "Kennedy", "Nixon", "Ford", "Carter", "Reagan", "Bush", "Clinton", "Obama", "Trump"])
def test_ddg_presidents(president):
    resp = requests.get(url_ddg + q + format_json)

    rsp_data = resp.json()
    
    relTopic = rsp_data["RelatedTopics"]
    
    text = [sub['Text'] for sub in relTopic]

    assert any(president in item for item in text)
    