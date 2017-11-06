```
curl -v 'http://localhost:5000/template/create' \
  --request POST \
  --header "Content-Type: application/json" \
  --data '{
      "user_id": "59f7e576b2c79a43548402e0",
      "kind": "train",
      "name": "名称",
      "regions": [
        {
          "name": "区域01",
          "pt1": {"x": 20, "y": 10}, 
          "pt2": {"x": 50, "y": 30},
          "correction": "ABC"
        }
      ],
      "storage_id": "59f6b2ebb2c79a6c3a969331",
      "filename": "测试.png"
    }'

curl -v -G 'http://localhost:5000/template/get' \
  --data-urlencode 'id=59f84711b2c79a6ed6b6d3c6'

curl -v -G 'http://localhost:5000/template/exist' \
  --data-urlencode 'field=name' \
  --data-urlencode 'value=名称'

curl -v -G 'http://localhost:5000/template/count'

curl -v -G 'http://localhost:5000/template/list' \
  --data-urlencode 'page=0' \
  --data-urlencode 'size=2' \
  --data-urlencode 'order=create_date' \
  --data-urlencode 'direction=asc'

curl -v 'http://localhost:5000/template/update' \
  --request POST \
  --header "Content-Type: application/json" \
  --data '{
      "id": "59f84711b2c79a6ed6b6d3c6",
      "name": "名称更新",
      "regions": [
        {
          "name": "区域01",
          "pt1": {"x": 20, "y": 10}, 
          "pt2": {"x": 50, "y": 30}
        },
        {
          "name": "区域02",
          "pt1": {"x": 60, "y": 10}, 
          "pt2": {"x": 90, "y": 30}
        }
      ]
    }'

curl -v 'http://localhost:5000/template/delete' \
  --request POST \
  --header "Content-Type: application/json" \
  --data '{
        "id": "59f84711b2c79a6ed6b6d3c6"
    }'
```
