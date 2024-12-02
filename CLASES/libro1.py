class Libro:
    def __init__(self, titulo, autor):
        self.titulo= titulo
        self.autor= autor
        
    def actualizar_titulo(self,nuevo_titulo):
        self.titulo= nuevo_titulo
        print(f"El nuevo título es: {nuevo_titulo}")
        
        
libro1= Libro("El principito", "Antoine de Saint-Exupéry")
libro1.actualizar_titulo("Tierra de hombres")