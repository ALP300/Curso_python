class Libro:
    def __init__(self, titulo, autor):
        self.titulo= titulo
        self.autor= autor
        
    def mostrar_info(self):
        print(f"Título: {self.titulo} y el Autor es: {self.autor}")
        
        
libro1= Libro("Cien años de soledad", "Gabriel García Marquez")
libro1.mostrar_info()