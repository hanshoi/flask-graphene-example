from graphene import Schema, relay, ObjectType
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from . import models


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
    all_employees = SQLAlchemyConnectionField(Employee)

schema = Schema(query=Query, types=[Department, Employee])
