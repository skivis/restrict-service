import jwt

encoded = jwt.encode({
    "firstName": "John",
    "lastName": "Doe",
    "email": "john.doe@example.com",
    "timezone": "Europe/Paris",
    "country": "cn",
}, 'secret', algorithm='HS256')


print encoded

print jwt.decode(encoded, verify=False)
