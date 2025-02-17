import graphene
from graphene_django.types import DjangoObjectType
from .models import Author, Category, Tag, Post, Faq
from graphene_django_pagination import DjangoPaginationConnectionField

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
    thumbnailImage = graphene.String()

    class Meta:
        model = Post
        filter_fields = ['category', 'tags', 'slug']

    def resolve_thumbnailImage(self, info):
        if self.thumbnail_image:
            return self.thumbnail_image.url
        return None

class FaqType(DjangoObjectType):
    class Meta:
        model = Faq
        filter_fields = ['category','question']


class Query(graphene.ObjectType):
    all_authors = graphene.List(AuthorType)
    all_categories = graphene.List(CategoryType)
    all_tags = graphene.List(TagType)
    all_posts = DjangoPaginationConnectionField(PostType)
    all_faqs = graphene.List(FaqType)

    def resolve_all_authors(self, info, **kwargs):
        return Author.objects.all()

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_all_tags(self, info, **kwargs):
        return Tag.objects.all()

    def resolve_all_posts(self, info, **kwargs):
        return Post.objects.all()
    
    def resolve_all_faqs(self, info, **kwargs):
        return Faq.objects.all()

schema = graphene.Schema(query=Query)
