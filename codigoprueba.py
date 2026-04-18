class Actividades:
    def __init__(self, nombre_tarea, tiempo_estimado, prioridad, completada, responsable):
        self.__nombre_tarea = nombre_tarea
        self.__tiempo_estimado = tiempo_estimado  
        self.__prioridad = prioridad  
        self.__completada = completada 
        self.__responsable = responsable

    def info(self):
        print("Tarea:", self.__nombre_tarea)
        print("Tiempo estimado:", self.__tiempo_estimado, "minutos")
        print("Prioridad:", self.__prioridad) #1:alta, 2:media y 3:alta
        print("Completada:", self.__completada)
        print("Responsable:", self.__responsable)

    def get_nombre_tarea(self):
        return self.__nombre_tarea

    def get_tiempo_estimado(self):
        return self.__tiempo_estimado

    def get_prioridad(self):
        return self.__prioridad

    def get_completada(self):
        return self.__completada

    def get_responsable(self):
        return self.__responsable
    
    def set_nombre_tarea(self, nombre_tarea):
        self.__nombre_tarea = nombre_tarea

    def set_tiempo_estimado(self, tiempo_estimado):
        self.__tiempo_estimado = tiempo_estimado

    def set_prioridad(self, prioridad):
        self.__prioridad = prioridad

    def set_completada(self, completada):
        self.__completada = completada

    def set_responsable(self, responsable):
        self.__responsable = responsable    
    
    def completar_tarea(self):
        self.__completada = True
    def es_urgente(self):
        return self.__prioridad == 1 and not self.__completada
    
    tarea = Actividades("Barrer la casa", 20, 1, False, "Mayte")
    tarea.info()
    print("\nLa prioridad es:", tarea.get_prioridad())
    tarea.set_prioridad(3)
    print("Nueva prioridad:", tarea.get_prioridad())
    tarea.completar_tarea()
    print("¿Es urgente?:", tarea.es_urgente())
    tarea.info()