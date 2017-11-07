```
curl -v 'http://localhost:5000/image/create' \
  --request POST \
  --header "Content-Type: application/json" \
  --data '{
      "user_id": "59f7e576b2c79a43548402e0",
      "kind": "evaluate",
      "name": "名称",
      "template_id": "59f84711b2c79a6ed6b6d3c6",
      "storage_id": "59f6b2ebb2c79a6c3a969331",
      "filename": "测试.png"
    }'

curl -v -G 'http://localhost:5000/image/get' \
  --data-urlencode 'id=59f935f6b2c79a6da6610f3c'

curl -v -G 'http://localhost:5000/image/exist' \
  --data-urlencode 'field=name' \
  --data-urlencode 'value=名称'

curl -v -G 'http://localhost:5000/image/count'

curl -v -G 'http://localhost:5000/image/list'

curl -v 'http://localhost:5000/image/update' \
  --request POST \
  --header "Content-Type: application/json" \
  --data '{
      "id": "59f935f6b2c79a6da6610f3c",
      "name": "名称更新",
      "regions": [
        {
          "name": "区域01",
          "pt1": {"x": 20, "y": 10}, 
          "pt2": {"x": 50, "y": 30},
          "regconition": "A80",
          "correction": "ABC"
        }
      ],
      "status": "validated"
    }'

curl -v 'http://localhost:5000/image/delete' \
  --request POST \
  --header "Content-Type: application/json" \
  --data '{
        "id": "59f935f6b2c79a6da6610f3c"
    }'

curl -v 'http://localhost:5000/image/update_regions' \
  --request POST \
  --header "Content-Type: application/json" \
  --data '{
        "id": "59f935f6b2c79a6da6610f3c"
    }'

curl -v 'http://localhost:5000/image/crop_regions' \
  --request POST \
  --header "Content-Type: application/json" \
  --data '{
        "id": "59f935f6b2c79a6da6610f3c"
    }'

curl -v 'http://localhost:5000/image/resize_regions' \
  --request POST \
  --header "Content-Type: application/json" \
  --data '{
        "id": "59f935f6b2c79a6da6610f3c"
    }'

curl -v 'http://localhost:5000/image/draw_regions' \
  --request POST \
  --header "Content-Type: application/json" \
  --data '{
        "id": "59f935f6b2c79a6da6610f3c"
    }'
```
