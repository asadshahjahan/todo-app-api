# todo-app-api
Backend services for todo app written in Python-Django
## Project Structure
```
app/
    app/
    core/
    user/
```
## APIs
### User
* **Sign Up**
    * (**POST**) `localhost:8000/api/user/signup/`
* **Sign In**
    * (**POST**) `localhost:8000/api/user/auth/`
    * This will return a token which should be added in header of future requests as `Authorization: Token c60ba83d8ef20f9339d0a4088`
* **User Detail**
    * (**GET**) `localhost:8000/api/user/me/`
* **User Update**
    * (**PUT**) `localhost:8000/api/user/me/`
