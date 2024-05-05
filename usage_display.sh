d=http://localhost:8000/
#d=https://onopod-1.paiza-user-basic.cloud:8000/api/
echo -e "\n初期データを準備"
curl --get ${d}api/users/ONOPOD/changestatus/ --data-urlencode id=ONOPOD --data-urlencode name=小野 --data-urlencode emote=smile
curl --get ${d}api/users/ONOPOD/changestatus/ --data-urlencode id=ONOPOD --data-urlencode name=小野 --data-urlencode subject=簿記2級
curl --get ${d}api/users/ONOPOD/changestatus/ --data-urlencode id=ONOPOD --data-urlencode name=小野 --data-urlencode place=A12
curl --get ${d}api/users/ONOPOD/changestatus/ --data-urlencode id=ONOPOD --data-urlencode name=小野 --data-urlencode comment=がんばります
curl --get ${d}api/users/ONOPOD/changestatus/ --data-urlencode id=ONOPOD --data-urlencode name=小野 --data-urlencode chara=zunda
curl --get ${d}api/studies/in/ --data-urlencode id=ONOPOD --data-urlencode name=小野
curl --get ${d}api/studies/charge/ --data-urlencode id=ONOPOD --data-urlencode name=小野
curl --get ${d}api/studies/out/ --data-urlencode id=ONOPOD --data-urlencode name=小野

curl --get ${d}api/studies/in/ --data-urlencode id=ONOPOD2 --data-urlencode name=小野2
sqlite3 db.sqlite3 -echo "select * from api_study;"

echo -e "\n表示内容を取得"
curl ${d}display/