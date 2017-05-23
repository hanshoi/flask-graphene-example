from graphene import Schema, relay, ObjectType
from graphene_sqlalhemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from . import models

schema = Schema()


class Department(SQLAlchemyObjectType):
    class Meta:
        model = models.Department
        interfaces = (relay.Node, )


class Employee(SQLAlchemyObjectType):
    class Meta:
        model = models.Employee
        interfaces = (relay.Node, )


class Query(ObjectType):
    node = relay.Node.Field()
    all_employees = SQLAlchemyConnectionField(models.Employee)

schema.query = Query()
