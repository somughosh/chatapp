from chat import db


def test_get_user():
    assert db.get_user(email="") == db.DEFAULT_USER

def test_get_check_valid_password():
    db.set_user(email="a@b.com", password="12344")
    assert db.get_check_valid_password(email="a@b.com",password="12344")==True