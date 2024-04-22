def get_authenticated_user_details(request_headers):
    user_object = {}

    ## check the headers for the Principal-Id (the guid of the signed in user)
    if "X-Ms-Client-Principal-Id" not in request_headers.keys():
        ## if it's not, assume we're in development mode and return a default user
        from . import sample_user
        raw_user_object = sample_user.sample_user
    else:
        ## if it is, get the user details from the EasyAuth headers
        raw_user_object = {k:v for k,v in request_headers.items()}

    user_object['user_principal_id'] = raw_user_object.get('X-Ms-Client-Principal-Id')
    user_object['user_name'] = raw_user_object.get('X-Ms-Client-Principal-Name')
    user_object['auth_provider'] = raw_user_object.get('X-Ms-Client-Principal-Idp')
    user_object['auth_token'] = raw_user_object.get('X-Ms-Token-Aad-Id-Token')
    user_object['client_principal_b64'] = raw_user_object.get('X-Ms-Client-Principal')
    user_object['aad_id_token'] = raw_user_object.get('X-Ms-Token-Aad-Id-Token')

    return user_object


## JWT Authentification service ##
import jwt

def decode_jwt(token):
    """Decodifica un token JWT y extrae la información del usuario."""
    with open('secret_key.txt', 'r') as f:
        SECRET_KEY = f.read().strip() 
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return {"status": "success", "payload": payload}
    except jwt.ExpiredSignatureError:
        return {"status": "error", "message": "Token expired"}
    except jwt.InvalidTokenError:
        return {"status": "error", "message": "Invalid token"}

def get_authenticated_user_details_jwt(request_headers):
    if "Authorization" not in request_headers:
        return {"status": "error", "message": "Authorization header is missing"}
    else:

        token = request_headers["Authorization"].split(" ")[1]  # Formato esperado "Bearer {token}"
        jwt_result = decode_jwt(token)  # Asegúrate de que esta función está correctamente implementada
        
        if jwt_result["status"] != "success":
            return jwt_result  # Devuelve el error si la decodificación del JWT falló
        
        # Mapear la carga útil del JWT al objeto del usuario según tu esquema
        user_object = {
            "user_id": jwt_result["payload"].get("sub", "default_user"),
            "user_name": jwt_result["payload"].get("name", "Unknown"),
        }
        return user_object