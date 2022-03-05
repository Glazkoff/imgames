import graphene
from .models import Organization
from .types import OrganizationType
from graphql_jwt.decorators import login_required


class CreateOrganization(graphene.Mutation):
    """ Мутация для создания организации """
    organization = graphene.Field(OrganizationType)
    success = graphene.Boolean()
    errors = graphene.List(graphene.String)

    class Arguments:
        name = graphene.String(required=True)
        subdomain = graphene.String(required=True)
        prefix = graphene.String(required=True)

    @login_required
    def mutate(self, info, name, subdomain, prefix):
        try:
            user = info.context.user
            check_organization = Organization.objects.filter(
                subdomain=subdomain).count()
            print(check_organization)
            if check_organization == 0:
                organization = Organization(
                    name=name, prefix=prefix, subdomain=subdomain, organization_owner=user)
                organization.save()
                return CreateOrganization(success=True, organization=organization)
            else:
                raise ValueError('Subdomain exists!')
        except Exception as e:
            return CreateOrganization(success=False, errors=[str(e)])
