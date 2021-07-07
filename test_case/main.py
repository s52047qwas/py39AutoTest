import pytest

pytest.main(["-s", "-v", "test_login_02.py", "--html=report1.html", "--alluredir=allure_files","--clean-alluredir"])