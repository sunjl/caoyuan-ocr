```
curl -v 'http://localhost:5000/user/sign_up' \
  --request POST \
  --header "Content-Type: application/json" \
  --data '{
        "display_name": "哈哈123",
        "email": "test@abc.com",
        "username": "test",
        "password": "12345"
    }'

curl -v http://localhost:5000/user/sign_in \
  --request POST \
  --header "Content-Type: application/json" \
  --data '{
        "username": "test",
        "password": "12345"
    }'

curl -v 'http://localhost:5000/user/create' \
  --request POST \
  --header "Content-Type: application/json" \
  --data '{
        "display_name": "哈哈123",
        "email": "test@abc.com",
        "username": "test",
        "password": "12345",
        "auth_roles": ["normal"]
    }'

curl -v -G 'http://localhost:5000/user/get' \
  --data-urlencode 'id=59f7e576b2c79a43548402e0'

curl -v -G 'http://localhost:5000/user/exist' \
  --data-urlencode 'field=username' \
  --data-urlencode 'value=test'

curl -v -G 'http://localhost:5000/user/count'

curl -v -G 'http://localhost:5000/user/list'

curl -v 'http://localhost:5000/user/update' \
  --request POST \
  --header "Content-Type: application/json" \
  --data '{
        "id": "59f7e576b2c79a43548402e0",
        "display_name": "呵呵456",
        "email": "test@def.com"
    }'

curl -v 'http://localhost:5000/user/update_password' \
  --request POST \
  --header "Content-Type: application/json" \
  --data '{
        "username": "test",
        "new_password": "67890"
    }'

curl -v 'http://localhost:5000/user/update_auth_roles' \
  --request POST \
  --header "Content-Type: application/json" \
  --data '{
        "id": "59f7e576b2c79a43548402e0",
        "auth_roles": ["admin","normal"]
    }'

curl -v 'http://localhost:5000/user/update_auth_token' \
  --request POST \
  --header "Content-Type: application/json" \
  --data '{
        "id": "59f7e576b2c79a43548402e0"
    }'

curl -v 'http://localhost:5000/user/delete' \
  --request POST \
  --data-urlencode 'id=59f7e576b2c79a43548402e0'
```