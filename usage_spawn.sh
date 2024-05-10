d=http://localhost:8000/api/
#d=https://onopod-1.paiza-user-basic.cloud:8000/api/
echo -e "\nin out Spawnコマンドをテスト"
curl --get ${d}studies/in/ --data-urlencode id=ONO123 --data-urlencode name=ONO
curl --get ${d}studies/in/ --data-urlencode id=SATO123 --data-urlencode name=SATO
curl --get ${d}studies/in/ --data-urlencode id=TANAKA123 --data-urlencode name=TANAKA
curl --get ${d}users/ONO123/changestatus/ --data-urlencode id=ONO123 --data-urlencode name=ONO --data-urlencode place=A
curl --get ${d}users/SATO123/changestatus/ --data-urlencode id=SATO123 --data-urlencode name=SATO --data-urlencode place=A
curl --get ${d}users/TANAKA123/changestatus/ --data-urlencode id=TANAKA123 --data-urlencode name=TANAKA --data-urlencode place=A
curl --get ${d}users/ONO123/changestatus/ --data-urlencode id=ONO123 --data-urlencode name=ONO --data-urlencode place=B
curl --get ${d}users/SATO123/changestatus/ --data-urlencode id=SATO123 --data-urlencode name=SATO --data-urlencode place=B
curl --get ${d}users/TANAKA123/changestatus/ --data-urlencode id=TANAKA123 --data-urlencode name=TANAKA --data-urlencode place=B





sqlite3 db.sqlite3 -echo "select * from api_command order by created_at desc limit 10"
