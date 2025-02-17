import graphene
from graphene_django.types import DjangoObjectType
from .models import Academy, Article
from graphene_django_pagination import DjangoPaginationConnectionField


class ArticleType(DjangoObjectType):
    class Meta:
        model = Article
        filter_fields = ['academy__id']

class AcademyType(DjangoObjectType):
    class Meta:
        model = Academy

class Query(graphene.ObjectType):
    articles = DjangoPaginationConnectionField(ArticleType)
    academy = graphene.List(AcademyType)

    def resolve_articles(self, info, **kwargs):
        return Article.objects.all()

    def resolve_academy(self, info, **kwargs):
        return Academy.objects.all()

schema = graphene.Schema(query=Query)