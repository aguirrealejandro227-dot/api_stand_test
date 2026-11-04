import sender_stand_request
import data
def get_user_body(first_name):
    # el diccionario que contiene el cuerpo de solicitud se copia del archivo "data" (datos) para conservar los datos del diccionario de origen
    current_body = data.user_body.copy()
    # Se cambia el valor del parámetro firstName
    current_body["firstName"] = first_name
    # Se devuelve un nuevo diccionario con el valor firstName requerido
    return current_body
def negative_assert_symbol(first_name):
        # el diccionario que contiene el cuerpo de solicitud se copia del archivo "data" (datos) para conservar los datos del diccionario de origen
        user_body= get_user_body(first_name)
        # Se cambia el valor del parámetro firstName
        response = sender_stand_request.post_new_user(user_body)
    # El resultado de la solicitud relevante se guarda en la variable "user_response"
        assert response.status_code == 400
        assert response.json()["code"] == 400
        assert response.json()["message"] == "Has introducido un nombre de usuario no válido. " \
                                             "El nombre solo puede contener letras del alfabeto latino, " \
                                            "la longitud deber ser de 2 a 15 caracteres."
