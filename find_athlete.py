# импортируем библиотеку sqlalchemy и некоторые функции из нее 
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# константа, указывающая способ соединения с базой данных
DB_PATH = "sqlite:///sochi_athletes.sqlite3"
# базовый класс моделей таблиц
Base = declarative_base()

class Athelete(Base):
    """
    Описывает структуру таблицы user для хранения регистрационных данных пользователей
    """
    __tablename__ = 'athelete'
    id = sa.Column(sa.Integer, primary_key=True)
    age = sa.Column(sa.Text)
    birthdate = sa.Column(sa.Text)
    gender = sa.Column(sa.Text)
    height = sa.Column(sa.Float)
    name = sa.Column(sa.Text)
    weight = sa.Column(sa.Float)
    gold_medals = sa.Column(sa.Float)
    silver_medals = sa.Column(sa.Float)
    bronze_medals = sa.Column(sa.Float)
    total_medals = sa.Column(sa.Float)
    sport = sa.Column(sa.Text)
    country = sa.Column(sa.Text)


def connect_db():
    """
    Устанавливает соединение к базе данных, создает таблицы, если их еще нет и возвращает объект сессии 
    """
    # создаем соединение к базе данных
    engine = sa.create_engine(DB_PATH)
    # создаем описанные таблицы
    Base.metadata.create_all(engine)
    # создаем фабрику сессию
    session = sessionmaker(engine)
    # возвращаем сессию
    return session()

def find(id, session):
    """
    Производит поиск пользователя в таблице user по заданному имени name
    """
    try:
        athelete_main = session.query(Athelete).filter(Athelete.id == id).first()
        # Выводим основного
        print(f"Основной! ID - {athelete_main.id}; Имя - {athelete_main.name}; Рост - {athelete_main.height}; ДР - {athelete_main.birthdate}") 

        # Ищем ближайшего по росту
        y_height = ''
        all_atheletes = session.query(Athelete).order_by(Athelete.height).all()
        for x in all_atheletes:
            if x.height == athelete_main.height:
                print(f"Ближайший по росту! ID - {y_height.id}; Имя - {y_height.name}; Рост - {y_height.height}; ДР - {y_height.birthdate}") 
                break
            y_height = x
        
        # Ищем ближайшего по ДР
        all_atheletes = session.query(Athelete).order_by(Athelete.birthdate).all()
        y_birthdate = ''
        for x in all_atheletes:
            if x.birthdate == athelete_main.birthdate:
                print(f"Ближайший по ДР! ID - {y_birthdate.id}; Имя - {y_birthdate.name}; Рост - {y_birthdate.height}; ДР - {y_birthdate.birthdate}")
                break
            y_birthdate = x
        return (True)
    except:
        return (False)


    # # находим все записи в таблице User, у которых поле User.first_name совпадает с параметром name
    # query = session.query(User).filter(User.id == id)
    # # составляем список идентификаторов всех найденных пользователей
    # user_ids = [user.id for user in query.all()]


def main():
    """
    Осуществляет взаимодействие с пользователем, обрабатывает пользовательский ввод
    """
    session = connect_db()

    # выбран режим поиска, запускаем его
    id = input("Введи id пользователя для поиска: ")
    # вызываем функцию поиска по имени

    # печать на экран результатов поиска
    if find(id, session):
        pass
    else:
        print("Такого пользователя нет")

if __name__ == "__main__":
    main()