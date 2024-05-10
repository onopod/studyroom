d=http://localhost:8000/api/
#d=https://onopod-1.paiza-user-basic.cloud:8000/api/
echo -e "\nコマンド登録テスト"
curl --get ${d}studies/in/ --data-urlencode id=ONOPOD --data-urlencode name=小野
curl --get ${d}studies/charge/ --data-urlencode id=ONOPOD --data-urlencode name=小野
curl --get ${d}users/ONOPOD/changestatus/ --data-urlencode id=ONOPOD --data-urlencode name=小野 --data-urlencode emote=smile
curl --get ${d}users/ONOPOD/changestatus/ --data-urlencode id=ONOPOD --data-urlencode name=小野 --data-urlencode subject=簿記2級
curl --get ${d}users/ONOPOD/changestatus/ --data-urlencode id=ONOPOD --data-urlencode name=小野 --data-urlencode place=A12
curl --get ${d}users/ONOPOD/changestatus/ --data-urlencode id=ONOPOD --data-urlencode name=小野 --data-urlencode comment=がんばります
curl --get ${d}users/ONOPOD/changestatus/ --data-urlencode id=ONOPOD --data-urlencode name=小野 --data-urlencode chara=zunda
curl --get ${d}studies/out/ --data-urlencode id=ONOPOD --data-urlencode name=小野
sqlite3 db.sqlite3 -echo "select * from api_user;"
sqlite3 db.sqlite3 -echo "select * from api_study;"
sqlite3 db.sqlite3 -echo "select * from api_command;"
