d=http://localhost:8000/api/
#d=https://onopod-1.paiza-user-basic.cloud:8000/api/
echo -e "\nnightbotから飛んでくるcommandをテスト"
curl --get ${d}users/ONOPOD/changestatus/ --data-urlencode id=ONOPOD --data-urlencode name=小野 --data-urlencode emote=smile
curl --get ${d}users/ONOPOD/changestatus/ --data-urlencode id=ONOPOD --data-urlencode name=小野 --data-urlencode subject=簿記2級
curl --get ${d}users/ONOPOD/changestatus/ --data-urlencode id=ONOPOD --data-urlencode name=小野 --data-urlencode place=A12
curl --get ${d}users/ONOPOD/changestatus/ --data-urlencode id=ONOPOD --data-urlencode name=小野 --data-urlencode comment=がんばります
