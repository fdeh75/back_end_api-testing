from aiohttp import web
from graphene import ObjectType, String
from aiohttp_graphql import GraphQLView
from graphene import Schema
import graphene


class InputPerson(graphene.InputObjectType):
    first_name = graphene.String()
    last_name = graphene.String()


class Person(ObjectType):
    first_name = String()
    last_name = String()
    full_name = String()


class Queries(graphene.ObjectType):

    person = graphene.Field(Person, input=InputPerson())
    # person = graphene.Field(Person, first_name=graphene.String(), last_name=graphene.NonNull(graphene.String))

    def resolve_person(self, *args, input: InputPerson, **kwargs):
        result = Person()
        result.first_name = input.first_name
        result.last_name = input.last_name
        result.full_name = f"{input.first_name} {input.last_name}"

        return result

    # def resolve_person(self, *args, first_name='', last_name='', **kwargs):
    #     result = Person()
    #     result.first_name = first_name
    #     result.last_name = last_name
    #     result.full_name = f"{first_name} {last_name}"
    #
    #     return result


Schema = Schema(query=Queries)
app = web.Application()

GraphQLView.attach(app, schema=Schema, graphiql=True)
web.run_app(app, port=5002)