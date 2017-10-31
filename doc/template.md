```
curl -v 'http://localhost:5000/template/create' \
  --request POST \
  --header "Content-Type: application/json" \
  --data '{
      "user_id": "59f7e576b2c79a43548402e0",
      "category": "train",
      "name": "名称",
      "regions": [
        {"pt1": {"x": 100, "y": 50}, "pt2": {"x": 200, "y": 100}}
      ],
      "storage_id": "59f6b2ebb2c79a6c3a969331",
      "filename": "测试.png"
    }'

curl -v -G 'http://localhost:5000/template/get' \
  --data-urlencode 'id=59f6b2ebb2c79a6c3a969331'

curl -v -G 'http://localhost:5000/template/exist' \
  --data-urlencode 'field=name' \
  --data-urlencode 'value=名称'

curl -v -G 'http://localhost:5000/template/count'

curl -v -G 'http://localhost:5000/template/list'

curl -v 'http://localhost:5000/template/update' \
  --request POST \
  --header "Content-Type: application/json" \
  --data '{
      "id": "59f6b2ebb2c79a6c3a969331",
      "name": "名称更新",
      "regions": [
        {"pt1": {"x": 100, "y": 50}, "pt2": {"x": 200, "y": 100}},
        {"pt1": {"x": 200, "y": 100}, "pt2": {"x": 300, "y": 150}}
      ],
    }'

curl -v 'http://localhost:5000/template/delete' \
  --request POST \
  --data-urlencode 'id=59f6b2ebb2c79a6c3a969331'
```
