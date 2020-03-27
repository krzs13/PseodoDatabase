# create document somedoc (aaa, bbb, ccc)
# add (ddd, e,,,,   ee, fff) to somedoc
# SELECT (name, age) from somedoc
# COUNT DISTINCT (name) FROM somedoc
# DELETE FROM somedoc WHERE name=Koles
# JSON somedoc
# EXPORT somedoc
# IMPORT FROM database/somepac.zip

from logic.front_controller import FrontController

if __name__ == "__main__":
    front_controller = FrontController()
    front_controller.run()