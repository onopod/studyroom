d=http://localhost:8000/api/
j='Content-Type: application/json'
echo -e "\nコマンドを登録→ユーザーを自動登録→Webコマンドを実行"
curl -X POST -H "${j}" ${d}commands/register/ -d '{"text": "ONOPOD !in"}'
sqlite3 db.sqlite3 -echo "select * from api_user;"
sqlite3 db.sqlite3 -echo "select * from api_command;"
