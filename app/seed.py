# seed.py
from app import create_app
from app.extensions import db
from app.models     import User, Profile

app = create_app()
with app.app_context():
    db.drop_all()
    db.create_all()

    u1 = User(username="alice",   name="Alice Doe",  email="alice@example.com", photo="https://i.pravatar.cc/200?img=1")
    u1.set_password("secret123")
    db.session.add(u1)
    db.session.add(Profile(
        user=u1, description="Reggae lover",
        parish="St. Andrew", biography="Born to dancehall…",
        sex="Female", race="African", birth_year=1990,
        height=5.5, photo="https://i.pravatar.cc/200?img=47",
        fav_cuisine="Jamaican", fav_colour="Green",
        fav_school_subject="Music",
        political=False, religious=True,
        family_oriented=True
    ))

    u2 = User(username="bob",     name="Bob Marley", email="bob@example.com",   photo="https://i.pravatar.cc/200?img=2")
    u2.set_password("oneLove")
    db.session.add(u2)
    db.session.add(Profile(
        user=u2, description="Legendary singer",
        parish="St. Ann", biography="Roots reggae…",
        sex="Male", race="African", birth_year=1945,
        height=5.6, photo="https://i.pravatar.cc/200?img=12",
        fav_cuisine="Italian", fav_colour="Red",
        fav_school_subject="History",
        political=True, religious=False,
        family_oriented=True
    ))
    db.session.commit()
    print("✅ Seeded Alice & Bob")
