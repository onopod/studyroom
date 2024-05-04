d=http://localhost:8000/api/
#d=https://onopod-1.paiza-user-basic.cloud:8000/api/
echo -e "\nin out chargコマンドをテスト"
curl --get ${d}studies/in/ --data-urlencode id=ONOPOD --data-urlencode name=小野
curl --get ${d}studies/charge/ --data-urlencode id=ONOPOD --data-urlencode name=小野
curl --get ${d}studies/out/ --data-urlencode id=ONOPOD --data-urlencode name=小野
e