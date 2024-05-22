import unittest
import json


#Se dejan dos lineas despues de las importaciones.
class Testlibreria(unittest.TestCase):
    '''una linea en blanco entre los metodos de una clase.'''
    def setUp(self):
        self.libreria = Testlibreria()
        
    def test_añadir_libro(self):
        '''este metodo añade un libro a nuestra libreria.'''
        titulo="El señor de los anillos"
        autor="J.R.R Tolkien"
        genero= "Fantasia"
        anio= 1954
        self.libreria.anadir_libro(titulo, autor, genero, anio)
        libro_añadido = self.libreria.libros[-1]
        self.assertEqual(libro_añadido, {"titulo": titulo, "autor": autor, "genero": genero, "anio": anio})

    def test_de_buscar_libro(self):
        '''se busca un libro por su titulo.'''
        titulo_buscado="Cien años de soledad"
        libros_encontrados=self.libreria.buscar_libro(titulo_buscado)
        self.assertEqual(len(libros_encontrados), 1)
        libro_encontrado = libros_encontrados[0]
        self.assertEqual(libro_encontrado["titulo"], titulo_buscado)

    def test_buscar_por_autor(self):
        '''se busca un libro por el autor'''
        autor_buscado = "Gabriel García Márquez"
        libros_encontrados = self.libreria.buscar_por_autor(autor_buscado)
        self.assertTrue(libros_encontrados)
        for libro in libros_encontrados:
            self.assertIn(autor_buscado.lower(), libro["autor"].lower()) 
        if not libros_encontrados:
            mensaje_retorno = self.libreria.buscar_por_autor(autor_buscado)
            self.assertEqual(mensaje_retorno, "No se encontraron libros del autor")

    def test_eliminar_libro(self):
        '''se busca el libro a eliminar.''' 
        titulo_eliminar = "Cien años de soledad"
        resultado = self.libreria.eliminar_libro(titulo_eliminar)
        self.assertEqual(resultado, "Libro eliminado")
        libros_restantes = self.libreria.libros
        self.assertFalse(any(libro["titulo"] == titulo_eliminar for libro in libros_restantes))
        if not libros_restantes:
            mensaje_retorno = self.libreria.buscar_por_autor(titulo_eliminar)
            self.assertEqual(mensaje_retorno, "No se encontraron libros del autor")

    def test_guardar_libros(self):
        archivo = "libreria.json"
        resultado = self.libreria.guardar_libros(archivo)
        self.assertEqual(resultado, "Libros guardados")
        with open(archivo, "r") as f:
            datos_guardados = json.load(f)
        self.assertEqual(datos_guardados, self.libreria.libros)

    def test_cargar_libros(self):
        '''Se guarda la librería en un archivo JSON.'''
        archivo = "libreria.json"
        self.libreria.guardar_libros(archivo)
        nueva_libreria = Testlibreria()
        resultado = nueva_libreria.cargar_libros(archivo)
        self.assertEqual(resultado, "Libros cargados")
        self.assertEqual(nueva_libreria.libros, self.libreria.libros)


if __name__ == "__main__":
    unittest.main()
