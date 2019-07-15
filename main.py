from aiohttp import web
from graphene import ObjectType, String
from aiohttp_graphql import GraphQLView
from graphene import Schema
import graphene


class Person(ObjectType):
    first_name = String()
    last_name = String()
    full_name = String()

    # def resolve_first_name(parent, info):
    #     return "Иван"
    #
    # def resolve_full_name(parent, info):
    #     return 'Иванов Иван'


class Queries(graphene.ObjectType):

    person = graphene.Field(Person, first_name=graphene.String(), last_name=graphene.String())

    def resolve_person(self, *args, **kwargs):
        result = Person()
        result.first_name = kwargs['first_name']
        result.last_name = kwargs['last_name']
        result.full_name = f"{kwargs['last_name']} {kwargs['first_name']}"

        return result


Schema = Schema(query=Queries)
app = web.Application()

GraphQLView.attach(app, schema=Schema, graphiql=True)
web.run_app(app, port=5002)