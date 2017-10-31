```
curl -v -X POST 'http://localhost:5000/storage/upload' \
  -F "file=@/home/ubuntu/download/测试.png"

curl -v -G 'http://localhost:5000/storage/59f6b2ebb2c79a6c3a969331/测试.png' \
  > ~/download/测试下载.png

curl -v 'http://localhost:5000/storage/delete' \
  --request POST \
  --header "Content-Type: application/json" \
  --data '{
        "id": "59f6b2ebb2c79a6c3a969331"
    }'
```