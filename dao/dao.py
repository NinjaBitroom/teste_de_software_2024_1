from services.database import db


class Dao[T]:

    def __init__(self, model: type[T]):
        self.__model = model

    def get_all(self) -> list[T]:
        """Retorna todos os objetos."""
        return db.session.query(self.__model).all()

    def get_one(self, id_) -> T | None:
        """Retorna um cliente específico pelo ID."""
        return db.session.query(self.__model).get(id_)

    def add_one(self, obj: T) -> None:
        """Método para salvar um objeto no banco de dados."""
        db.session.add(obj)
        self.update()

    def update(self) -> None:
        """Método para atualizar o banco de dados."""
        db.session.commit()  # Salvando as alterações no banco de dados

    def delete_one(self, obj: T) -> None:
        """Método para deletar um objeto no banco de dados."""
        db.session.delete(obj)
        self.update()
