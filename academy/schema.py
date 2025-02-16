import graphene
from graphene_django.types import DjangoObjectType
from .models import Academy, Chapter
from graphene_django_pagination import DjangoPaginationConnectionField


class AcademyType(DjangoObjectType):
    class Meta:
        model = Academy
        filter_fields = ['chapter']

class ChapterType(DjangoObjectType):
    class Meta:
        model = Chapter

class Query(graphene.ObjectType):
    academies = DjangoPaginationConnectionField(AcademyType)
    chapters = graphene.List(ChapterType)

    def resolve_academies(self, info, **kwargs):
        return Academy.objects.all()

    def resolve_chapters(self, info, **kwargs):
        return Chapter.objects.all()

schema = graphene.Schema(query=Query)