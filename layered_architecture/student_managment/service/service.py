from dao.dao import Operations
class Service:
    def add(self,student):
        dao=Operations()
        dao.add(student)

    def view(self,student):
        dao=Operations()
        dao.view(student)

    def update(self,student):
        dao=Operations()
        dao.update(student)

    def delete(self,student):
        dao=Operations()
        dao.delete(student)


    