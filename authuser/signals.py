from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

# from matrixpro.submodel.m_client import ClientClass


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def post_save_create_staff(sender, instance, created, *args, **kwargs):
    if created:
        pass
        # if instance.roles_name =='consultant':
        #     ConsultantClass.objects.all().get_or_create(consultant_id=instance.id)

        # elif instance.roles_name =='client':
        #     ClientClass.objects.all().get_or_create(client_id=instance.id)