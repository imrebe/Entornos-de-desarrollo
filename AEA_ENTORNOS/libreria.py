import json

class Libreria:
    def __init__(self):
        self.libros = []

    def anadir_libro(self, titulo, autor, genero, anio):
        self.libros.append({'titulo': titulo, 'autor': autor, 'genero': genero, 'anio': anio})
        return "Libro añadido"

    def buscar_libro(self, titulo):
        return [libro for libro in self.libros if libro['titulo'].lower() == titulo.lower()]

    def buscar_por_autor(self, autor):
        return [libro for libro in self.libros if autor.lower() in libro['autor'].lower()]

    def eliminar_libro(self, titulo):
        original_count = len(self.libros)
        self.libros = [libro for libro in self.libros if libro['titulo'].lower() != titulo.lower()]
        return "Libro eliminado" if len(self.libros) < original_count else "Libro no encontrado"

    def guardar_libros(self, archivo):
        with open(archivo, 'w') as f:
            json.dump(self.libros, f)
        return "Libros guardados"

    def cargar_libros(self, archivo):
        try:
            with open(archivo, 'r') as f:
                self.libros = json.load(f)
            return "Libros cargados"
        except FileNotFoundError:
            return "Archivo no encontrado"


mi_libreria = Libreria()
mi_libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)
mi_libreria.guardar_libros('libreria.json')
print(mi_libreria.cargar_libros('libreria.json'))
print(mi_libreria.buscar_por_autor("Gabriel García Márquez"))

'''
import unittest
import json

class TestLibreria(unittest.TestCase):

    def setUp(self):
        self.libreria = Libreria()

    def test_anadir_libro(self):
        titulo = "El Señor de los Anillos"
        autor = "J.R.R. Tolkien"
        genero = "Fantasía"
        anio = 1954

        resultado = self.libreria.anadir_libro(titulo, autor, genero, anio)
        self.assertEqual(resultado, "Libro añadido")

        libro_añadido = self.libreria.libros[0]
        self.assertEqual(libro_añadido["titulo"], titulo)
        self.assertEqual(libro_añadido["autor"], autor)
        self.assertEqual(libro_añadido["genero"], genero)
        self.assertEqual(libro_añadido["anio"], anio)

    def test_buscar_libro(self):
        titulo_buscado = "Cien años de soledad"

        libros_encontrados = self.libreria.buscar_libro(titulo_buscado)
        self.assertEqual(len(libros_encontrados), 1)

        libro_encontrado = libros_encontrados[0]
        self.assertEqual(libro_encontrado["titulo"], titulo_buscado)

    def test_buscar_por_autor(self):
        autor_buscado = "Gabriel García Márquez"

        libros_encontrados = self.libreria.buscar_por_autor(autor_buscado)
        self.assertEqual(len(libros_encontrados), 1)

        libro_encontrado = libros_encontrados[0]
        self.assertEqual(libro_encontrado["autor"], autor_buscado)

    def test_eliminar_libro(self):
        titulo_eliminar = "Cien años de soledad"

        resultado = self.libreria.eliminar_libro(titulo_eliminar)
        self.assertEqual(resultado, "Libro eliminado")

        libros_restantes = self.libreria.libros
        self.assertEqual(len(libros_restantes), 0)

    def test_guardar_libros(self):
        archivo = "libreria.json"

        resultado = self.libreria.guardar_libros(archivo)
        self.assertEqual(resultado, "Libros guardados")

        with open(archivo, "r") as f:
            datos_guardados = json.load(f)

        self.assertEqual(datos_guardados, self.libreria.libros)

    def test_cargar_libros(self):
        archivo = "libreria.json"

        # Se guarda la librería en un archivo JSON
        self.libreria.guardar_libros(archivo)

        # Se crea una nueva instancia de la clase Libreria
        nueva_libreria = Libreria()

        # Se carga la librería desde el archivo JSON
        resultado = nueva_libreria.cargar_libros(archivo)
        self.assertEqual(resultado, "Libros cargados")

        # Se verifica que los libros de la nueva librería son iguales a los de la librería original
        self.assertEqual(nueva_libreria.libros, self.libreria.libros)

if __name__ == "__main__":
    unittest.main()
'''