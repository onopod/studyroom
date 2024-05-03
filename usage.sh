d=http://localhost:8000/api/
j='Content-Type: application/json'
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
curl -X POST ${d}commands/ -d user=ONOPOD -d name=!in
curl -X POST ${d}commands/ -d user=ONOPOD -d name=!out
curl -X POST ${d}commands/ -d user=WASDFF -d name=!out
curl -X POST ${d}commands/ -d user=WASDFF -d name=!out
echo -e "\n更新"
curl -X PATCH ${d}commands/1/ -d executed_web=true
echo -e "\n削除"
curl -X DELETE ${d}commands/4/
echo -e "\nテキストから登録"
curl -X POST -H "${j}" ${d}commands/register/ -d '{"text": "ONOPOD !in"}'
echo -e "\n一覧"
curl ${d}commands/
echo -e "\n詳細"
curl ${d}commands/1/
echo -e "\n最新"
curl ${d}commands/latest/
echo -e "\nWebの処理が未実施で一番古い行"
curl ${d}commands/unexecute_web/
echo -e "\n未処理の行を処理"
curl ${d}commands/execute_unexecute_web/
echo -e "Web側の処理を実行"
curl ${d}commands/1/execute/
