import graphene
from graphene_django.types import DjangoObjectType
from .models import Academy, Article
from graphene_django_pagination import DjangoPaginationConnectionField


class ArticleType(DjangoObjectType):
    class Meta:
        model = Article
        filter_fields = ['academy__slug']

class AcademyType(DjangoObjectType):
    total_articles = graphene.Int()
    logo=graphene.String()

    class Meta:
        model = Academy
        fields = ('id', 'title', 'slug','logo', 'description', 'total_articles')

    def resolve_total_articles(self, info):
        return self.article_set.count()
    
    def resolve_logo(self, info):
        if self.logo:
            return self.logo.url
        return None

class Query(graphene.ObjectType):
    articles = DjangoPaginationConnectionField(ArticleType)
    academy = graphene.List(AcademyType)

    def resolve_articles(self, info, **kwargs):
        return Article.objects.all()

    def resolve_academy(self, info, **kwargs):
        return Academy.objects.all()

schema = graphene.Schema(query=Query)