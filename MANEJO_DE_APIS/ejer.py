import requests

url= "https://jsonplaceholder.typicode.com/posts"

def get_posts():
    response= requests.get(url)
    if response.status_code == 200:
        data= response.json()
        for post in data[:5]:
            print(f"ID: {post['id']}\nTitle: {post['title']}\nBody: {post['body']}\n")
    else:
        print("Error en la petición")

def get_post_by_id(id):
    response= requests.get(f"{url}/{id}")
    if response.status_code == 200:
        post= response.json()
        print(f"ID: {post['id']}\nTitle: {post['title']}\nBody: {post['body']}\n")
    else:
        print("Error en la petición")
        
def create_post(title, body, userId):
    data= {
        "title": title,
        "body": body,
        "userId": userId
    }
    response= requests.post(url, json= data)
    if response.status_code == 201:
        post= response.json()
        print(f"ID: {post['id']}\nTitle: {post['title']}\nBody: {post['body']}\n")
    else:
        print("Error en la petición")
        
def actualizar_post(post_id, title=None, body=None, userId=None):
    update_data= {"title": title, "body": body, "userId": userId}
    response= requests.put(f"{url}/{post_id}", json= update_data)
    if response.status_code == 200:
        post= response.json()
        print(f"ID: {post['id']}\nTitle: {post['title']}\nBody: {post['body']}\n")
    else:
        print("Error en la petición")

def delete_post(post_id):
    response= requests.delete(f"{url}/{post_id}")
    if response.status_code == 200:
        print("Post eliminado")
    else:
        print("Error en la petición")
    
if __name__== "__main__":
    
    while True:
        print("1. Ver los primeros 5 posts")
        print("2. Ver post por ID")
        print("3. Creación de ID")
        print("4. Actualizar post")
        print("5. Eliminar post")
        print("6. Salir")
        option= input("Opción: ")
        if option == "1":
            get_posts()
        elif option == "2":
            id= input("ID del post: ")
            get_post_by_id(id)
        elif option == "3":
            title= input("Título: ")
            body= input("Cuerpo: ")
            userId= input("ID del usuario: ")
            create_post(title, body, userId)
        elif option == "4":
            post_id= input("ID del post: ")
            title= input("Título: ")
            body= input("Cuerpo: ")
            userId= input("ID del usuario: ")
            actualizar_post(post_id, title, body, userId)
        elif option == "5":
            post_id= input("ID del post: ")
            delete_post(post_id)
        else:
            break
        print("\n\n")
'''
response= requests.get(url)


if response.status_code == 200:
    data= response.json()
    for post in data[:5]:
        print(post["title"])
else:
    print("Error en la petición")
'''