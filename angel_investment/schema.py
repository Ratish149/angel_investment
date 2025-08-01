import graphene
from graphene_django.types import DjangoObjectType
from team.models import OurTeam, OurPartner
from events.models import Event, EventAttendee
from blog.models import Author, Category, Tag, Post, Faq
from academy.models import Academy, Article
from authentication.models import CustomUser, Company, CompanyTag, CompanyTeam, Users
from graphene_django_pagination import DjangoPaginationConnectionField

# Define a GraphQL type for the OurTeam model


class OurTeamType(DjangoObjectType):
    profilePicture = graphene.String()

    class Meta:
        model = OurTeam
        filter_fields = ['id']

    def resolve_profilePicture(self, info):
        if self.profile_picture:
            return self.profile_picture.url
        return None


class OurPartnerType(DjangoObjectType):
    logo = graphene.String()

    class Meta:
        model = OurPartner
        filter_fields = ['id']

    def resolve_logo(self, info):
        if self.logo:
            return self.logo.url
        return None


class EventType(DjangoObjectType):
    class Meta:
        model = Event
        filter_fields = ['id', 'title']


class EventAttendeeType(DjangoObjectType):
    class Meta:
        model = EventAttendee
        filter_fields = ['id', 'event', 'email', 'created_at']


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
        filter_fields = ['category', 'question']


class ArticleType(DjangoObjectType):
    class Meta:
        model = Article
        filter_fields = ['academy__slug', 'slug']


class AcademyType(DjangoObjectType):
    total_articles = graphene.Int()
    logo = graphene.String()

    class Meta:
        model = Academy
        fields = ('id', 'title', 'slug', 'logo',
                  'description', 'total_articles')

    def resolve_total_articles(self, info):
        return self.article_set.count()

    def resolve_logo(self, info):
        if self.logo:
            return self.logo.url
        return None


class CustomUserType(DjangoObjectType):
    class Meta:
        model = CustomUser


class CompanyType(DjangoObjectType):
    organization_logo = graphene.String()

    class Meta:
        model = Users
        filter_fields = {
            'id': ['exact'],          # Allow filtering by company ID
            'is_activated': ['exact'],
            'role': ['exact'],
            'organization_role': ['exact'],
        }

    def resolve_organization_logo(self, info):
        if self.organization_logo:
            return self.organization_logo.url
        return None


class CompanyTagType(DjangoObjectType):
    class Meta:
        model = CompanyTag


class CompanyTeamType(DjangoObjectType):
    class Meta:
        model = CompanyTeam

# Define a query to list all team members


class Query(graphene.ObjectType):
    all_team_members = DjangoPaginationConnectionField(OurTeamType)
    all_our_partners = graphene.List(OurPartnerType)
    all_events = DjangoPaginationConnectionField(EventType)

    all_authors = graphene.List(AuthorType)
    all_categories = graphene.List(CategoryType)
    all_tags = graphene.List(TagType)
    all_posts = DjangoPaginationConnectionField(PostType)
    all_faqs = DjangoPaginationConnectionField(FaqType)

    articles = DjangoPaginationConnectionField(ArticleType)
    academy = graphene.List(AcademyType)

    custom_users = graphene.List(CustomUserType)
    companies = DjangoPaginationConnectionField(CompanyType)
    company_tags = graphene.List(CompanyTagType)
    company_teams = graphene.List(CompanyTeamType)

    def resolve_custom_users(self, info, **kwargs):
        return CustomUser.objects.all()

    def resolve_companies(self, info, **kwargs):
        return Users.objects.all()

    def resolve_company_tags(self, info, **kwargs):
        return CompanyTag.objects.all()

    def resolve_company_teams(self, info, **kwargs):
        return CompanyTeam.objects.all()

    def resolve_academy(self, info, **kwargs):
        return Academy.objects.all()

    def resolve_articles(self, info, **kwargs):
        return Article.objects.all()

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

    def resolve_all_events(self, info, **kwargs):
        return Event.objects.all()

    def resolve_all_team_members(self, info, **kwargs):
        return OurTeam.objects.filter(**kwargs)

    def resolve_all_our_partners(self, info, **kwargs):
        return OurPartner.objects.all()


class CreateEventAttendee(graphene.Mutation):
    class Arguments:
        event_id = graphene.ID(required=True)
        email = graphene.String(required=True)

    event_attendee = graphene.Field(EventAttendeeType)

    def mutate(self, info, event_id, email):
        event = Event.objects.get(pk=event_id)
        attendee = EventAttendee.objects.create(event=event, email=email)
        return CreateEventAttendee(event_attendee=attendee)


class Mutation(graphene.ObjectType):
    create_event_attendee = CreateEventAttendee.Field()


# Create the schema
schema = graphene.Schema(query=Query, mutation=Mutation)
