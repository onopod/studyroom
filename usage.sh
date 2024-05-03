d=http://localhost:8000/api/
echo -e "\nユーザーテーブル"
echo -e "\n新規登録"
curl -X POST ${d}users/ -d id=ONOPOD -d name=小野
curl -X POST ${d}users/ -d id=WASDFF -d name=テスト太郎
curl -X POST ${d}users/ -d id=DUMMY -d name=DUMMY
echo -e "\n更新"
curl -X PATCH ${d}users/WASDFF/ -d place=A12
echo -e "\n削除"
curl -X DELETE ${d}users/DUMMY/
echo -e "\n一覧"
curl ${d}users/
echo -e "\n詳細"
curl ${d}users/ONOPOD/
echo -e "\nコマンドテーブル"
echo -e "\n新規登録"
curl -X POST ${d}commands/ -d user=ONOPOD -d name=in
curl -X POST ${d}commands/ -d user=ONOPOD -d name=out
curl -X POST ${d}commands/ -d user=WASDFF -d name=out
curl -X POST ${d}commands/ -d user=WASDFF -d name=out
echo -e "\n更新"
curl -X PATCH ${d}commands/1/ -d executed_web=true
echo -e "\n削除"
curl -X DELETE ${d}commands/4/
echo -e "\n一覧"
curl ${d}commands/
echo -e "\n詳細"
curl ${d}commands/1/
echo -e "\n最新"
curl ${d}commands/latest/
