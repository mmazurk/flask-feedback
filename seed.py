from models import User, Feedback, db
from app import app

# to run this, just $ python seed.py

db.drop_all()
db.create_all()

u1 = User(username = "sadman22", password = "$2b$12$OBKeXt8Ca.Ups9AtJyEbj.eHuK9gSUtjr4a4bQ8Ltm1CYWIHpaPTm", email = "manny@whatever.com", first_name = "Fappy", last_name = "McBabbit")
u2 = User(username = "thereisnospoon22", password = "$2b$12$aZkL1s06pmf9T.GqksRQ6Ohv7XRIfwvT3xsn8sLSImG8wBdQOhf5K", email = "donald32@thisplace.com", first_name = "Donny", last_name = "Bobbokin")
u3 = User(username = "flappergirl", password = "$2b$12$IAUCcyv2eMR4nI8esjt0XeonK/1svqtUsxsjL1fX2MAknJU5LHjsC", email = "sandra@joylife.com", first_name = "Sandra", last_name = "Gladring")

# "wuppers"
# "gollygee"
# "pandasyay"

users = [u1, u2, u3]
db.session.add_all(users)
db.session.commit()

f1 = Feedback(title = "And So It Must Go", content = "Unpleasant astonished an diminution up partiality. Noisy an their of meant. Death means up civil do an offer wound of. Called square an in afraid direct. Resolution diminution conviction so mr at unpleasing simplicity no. No it as breakfast up conveying earnestly immediate principle. Him son disposed produced humoured overcame she bachelor improved. Studied however out wishing but inhabit fortune windows.", username = "sadman22")

f2 = Feedback(title = "There is Yet Time?", content = "Debating me breeding be answered an he. Spoil event was words her off cause any. Tears woman which no is world miles woody. Wished be do mutual except in effect answer. Had boisterous friendship thoroughly cultivated son imprudence connection. Windows because concern sex its. Law allow saved views hills day ten. Examine waiting his evening day passage proceed.", username = "thereisnospoon22")

f3 = Feedback(title = "Man Up!", content = "Manor we shall merit by chief wound no or would. Oh towards between subject passage sending mention or it. Sight happy do burst fruit to woody begin at. Assurance perpetual he in oh determine as. The year paid met him does eyes same. Own marianne improved sociable not out. Thing do sight blush mr an. Celebrated am announcing delightful remarkably we in literature it solicitude. Design use say piqued any gay supply. Front sex match vexed her those great..", username = "flappergirl")

feedback = [f1, f2, f3]
db.session.add_all(feedback)
db.session.commit()