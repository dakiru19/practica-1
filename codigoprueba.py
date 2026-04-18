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
