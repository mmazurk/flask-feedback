from models import User, db
from app import app

# to run this, just $ python seed.py

db.drop_all()
db.create_all()

u1 = User(username = "sadman22", password = "$2b$12$OBKeXt8Ca.Ups9AtJyEbj.eHuK9gSUtjr4a4bQ8Ltm1CYWIHpaPTm", email = "manny@whatever.com", first_name = "Fappy", last_name = "McCrapperson")
u2 = User(username = "thereisnospoon22", password = "$2b$12$aZkL1s06pmf9T.GqksRQ6Ohv7XRIfwvT3xsn8sLSImG8wBdQOhf5K", email = "donald32@thisplace.com", first_name = "Donny", last_name = "Bobbokin")
u3 = User(username = "flappergirl", password = "$2b$12$IAUCcyv2eMR4nI8esjt0XeonK/1svqtUsxsjL1fX2MAknJU5LHjsC", email = "sandra@joylife.com", first_name = "Sandra", last_name = "Gladring")

# "wuppers"
# "gollygee"
# "pandasyay"

users = [u1, u2, u3]
db.session.add_all(users)
db.session.commit()