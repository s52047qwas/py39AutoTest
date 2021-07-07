import pytest


pytest.main(["-s","-v","test_case2.py","--html=report1.html", "--alluredir=allure1_files", "--clean-alluredir"])