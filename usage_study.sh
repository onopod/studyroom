d=http://localhost:8000/api/
#d=https://onopod-1.paiza-user-basic.cloud:8000/api/
echo -e "\nin out chargコマンドをテスト"
echo -e "\n基本"
curl --get ${d}studies/in/ --data-urlencode id=ONOPOD --data-urlencode name=小野
curl --get ${d}studies/charge/ --data-urlencode id=ONOPOD --data-urlencode name=小野
curl --get ${d}studies/out/ --data-urlencode id=ONOPOD --data-urlencode name=小野
sqlite3 db.sqlite3 -echo "select * from api_study;"
echo -e "\n開始していないのにチャージ、終了"
curl --get ${d}studies/charge/ --data-urlencode id=ONOPOD2 --data-urlencode name=小野
curl --get ${d}studies/out/ --data-urlencode id=ONOPOD2 --data-urlencode name=小野
echo -e "\n1度目のinを終了しないまま次に進んだ場合"
curl --get ${d}studies/in/ --data-urlencode id=ONOPOD3 --data-urlencode name=小野
curl --get ${d}studies/in/ --data-urlencode id=ONOPOD3 --data-urlencode name=小野
curl --get ${d}studies/out/ --data-urlencode id=ONOPOD3 --data-urlencode name=小野
sqlite3 db.sqlite3 -echo "select * from api_study;"
