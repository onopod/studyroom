d=http://localhost:8000/api/
echo -e "\nnightbotから飛んでくるulをテスト"
curl --get ${d}users/ONOPOD/nightbot/ --data-urlencode command=in --data-urlencode user_name=小野
