import graphene
from graphene_django.types import DjangoObjectType
from .models import Post, Author, Category, Tag

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
    all_posts = graphene.List(PostType)
    post_by_id = graphene.Field(PostType, id=graphene.Int(required=True))
    post_by_slug = graphene.Field(PostType, slug=graphene.String(required=True))

    def resolve_all_posts(self, info, **kwargs):
        return Post.objects.all()

    def resolve_post_by_id(self, info, id):
        return Post.objects.get(pk=id)

    def resolve_post_by_slug(self, info, slug):
        return Post.objects.get(slug=slug)

schema = graphene.Schema(query=Query)
