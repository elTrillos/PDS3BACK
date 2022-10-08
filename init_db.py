from app import db, User, Monster, Battle

user1=User(username="elQlo", password="123123", email="abc@gmail.com")
user2=User(username="soyYo", password="123123", email="abcd@gmail.com")
user3=User(username="MiPana", password="123123", email="abce@gmail.com")
user4=User(username="sacsac9", password="123123", email="abcdd@gmail.com")

monster1=Monster(id=1, pokenum=1,name="Leafala",imageName="1", maxHp=25,type=1,attack=5,defense=13,speed=5,user_id=1)
monster2=Monster(id=2,pokenum=2,name="Marsupine",imageName="2", maxHp=40,type=1,attack=10,defense=20,speed=6,user_id=3)
monster3=Monster(id=3,pokenum=3,name="Koaliptus",imageName="3", maxHp=50,type=1,attack=12,defense=30,speed=9,user_id=2)
monster4=Monster(id=4,pokenum=4,name="Pyropup",imageName="4", maxHp=20,type=2,attack=10,defense=8,speed=15,user_id=4)

battle1=Battle(fid1=1,fid2=2,fid3=4,pid1=1,pid2=3,pid3=4,php1=25,php2=50,php3=20,turn=0)

db.session.add_all([user1, user2, user3,user4])
db.session.add_all([monster1, monster2, monster3, monster4])
db.session.add_all([battle1])

db.session.commit()