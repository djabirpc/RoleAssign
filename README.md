## Test  
### Sign Up
URL `http://127.0.0.1:8000/api/register/`  
Body  
```
{
    "username":"djabir",
    "password":"Papamama-123"
}
```
### Login
URL `http://127.0.0.1:8000/api/token/`  
Body  
```
{
    "username":"admin",
    "password":"admin"
}
```     

### Create Role
URL `http://127.0.0.1:8000/api/create-role/`  
Body  
```
{
    "name": "Finance"
}
```

### Assign Roles
URL `http://127.0.0.1:8000/api/assignrole/
`  
Body  
```
{
    "username": "djabir",
    "role_name": "Finance"
}
```  

### Test HR role
URL `http://127.0.0.1:8000/api/hr/`  
 
