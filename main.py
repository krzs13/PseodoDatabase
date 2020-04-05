# create document somedoc (name, surname, age)
# add (Pa,,,co, Daniell, 11) to somedoc
# add (Ro   cky     , Daniell, 4) to somedoc
# add (Ro   cky     , zzzzzz) to somedoc
# SELECT (name, age) from somedoc
# SELECT (aaaaa) from somedoc
# COUNT DISTINCT (name) FROM somedoc
# DELETE FROM somedoc WHERE name=Koles
# JSON somedoc
# EXPORT FROM somedoc, somedoc2
# IMPORT FROM bbb, aaa

from logic.front_controller import FrontController


if __name__ == "__main__":
    front_controller = FrontController()
    front_controller.run()