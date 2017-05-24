from graphene import Schema, relay, ObjectType, List
from graphene_sqlalchemy import SQLAlchemyObjectType

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
    employees = List(Employee)

    def resolve_employees(self, args, context, info):
        query = Employee.get_query(context)
        return query.all()


schema = Schema(query=Query, types=[Department, Employee])
