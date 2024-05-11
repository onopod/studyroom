d=http://localhost:8000/api/
#d=https://onopod-1.paiza-user-basic.cloud:8000/api/
curl --get ${d}studies/in/ --data-urlencode id=ONO123 --data-urlencode name=ONO
curl --get ${d}users/ONO123/changestatus/ --data-urlencode id=ONO123 --data-urlencode name=ONO --data-urlencode place=A
curl --get ${d}users/ONO123/changestatus/ --data-urlencode id=ONO123 --data-urlencode name=ONO --data-urlencode comment=がんばります！
curl --get ${d}users/ONO123/changestatus/ --data-urlencode id=ONO123 --data-urlencode name=ONO --data-urlencode subject=簿記2級
curl --get ${d}users/ONO123/changestatus/ --data-urlencode id=ONO123 --data-urlencode name=ONO --data-urlencode chara=Colobus
curl --get ${d}studies/charge/ --data-urlencode id=ONO123 --data-urlencode name=ONO
curl --get ${d}studies/out/ --data-urlencode id=ONO123 --data-urlencode name=ONO
sqlite3 db.sqlite3 -echo "select * from api_user order by created_at desc limit 10"
sqlite3 db.sqlite3 -echo "select * from api_command order by created_at desc limit 10"
