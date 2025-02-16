'''

authenticathion and authorization

used to authenticate and authorize the user.
protect the routes from unauthorized access.

oauth2 is an standard that allows the user to access the resources in a secure way.

token is created starting with an password. password passed as a form data.

to use form data, we need to install python-multipart.

to get the token, we need to pass the password in the form data.

need to import OAuth2PasswordBearer, OAuth2PasswordRequestForm.

OAuth2PasswordRequestForm is a dependency that give us the form data with the user and password.

the token needs to be passed in the header of the request.

to generate the token hash we need python-jose.

'''