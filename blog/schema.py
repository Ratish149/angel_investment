import graphene
from graphene_django.types import DjangoObjectType
from .models import Author, Category, Tag, Post

class AuthorType(DjangoObjectType):
    class Meta:
        model = Author

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category

class TagType(DjangoObjectType):
    class Meta:
        model = Tag

class PostType(DjangoObjectType):
    class Meta:
        model = Post

class Query(graphene.ObjectType):
    all_authors = graphene.List(AuthorType)
    all_categories = graphene.List(CategoryType)
    all_tags = graphene.List(TagType)
    all_posts = graphene.List(PostType)

    def resolve_all_authors(self, info, **kwargs):
        return Author.objects.all()

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_all_tags(self, info, **kwargs):
        return Tag.objects.all()

    def resolve_all_posts(self, info, **kwargs):
        return Post.objects.all()

schema = graphene.Schema(query=Query)
