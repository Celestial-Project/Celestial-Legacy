import json
import pytest

with open('./responses/responses_th.json', encoding = "utf-8") as f:
    res_th = json.load(f)


def test_typo_check():
    for response in res_th:
        assert [res for res in res_th[response]['response'] if 'นะค่ะ' in res] == []