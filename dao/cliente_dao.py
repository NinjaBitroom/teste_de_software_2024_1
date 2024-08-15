class MemoryDAO[T]:
    def __init__(self, model: type[T]) -> None:
        self.__model = model
        self.__data = []

    def add_one(self, obj: T) -> None:
        self.__data.append(obj)

    def delete_one(self, obj: T) -> None:
        self.__data.remove(obj)

    def get_all(self) -> list[T]:
        return self.__data

    def get_one(self, id) -> T | None:
        for obj in self.__data:
            if obj.id == id:
                return obj
        return None
