extension = input("Ingrese la extensión del archivo (jpg, mp3, pdf, docx): ").lower()

match extension:
    case "jpg":
        print("Categoría: Imagen")
    case "mp3":
        print("Categoría: Audio")
    case "pdf":
        print("Categoría: Documento")
    case "docx":
        print("Categoría: Documento de texto")
    case _:
        print("Categoría: Desconocido")