from django.db import models
from taggit.managers import TaggableManager
from django.conf import settings


class BaseModel(models.Model):
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        abstract = True


class Thread(BaseModel):
    title = models.CharField('Título', max_length=100)
    slug = models.SlugField('Slug', max_length=120, unique=True)
    body = models.TextField('Mensagem')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Autor', related_name='threads',
                               on_delete=models.CASCADE)
    views = models.IntegerField('Visualizações', blank=True, default=0)
    answers = models.IntegerField('Respostas', blank=True, default=0)
    tags = TaggableManager()

    def __str__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return 'forum:thread', (), {'slug': self.slug}

    class Meta:
        verbose_name = 'Tópico'
        ordering = ['-updated_at']


class Reply(BaseModel):
    thread = models.ForeignKey(Thread, verbose_name='Tópico', related_name='replies', on_delete=models.CASCADE)
    reply = models.TextField('Resposta')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Autor', related_name='replies',
                               on_delete=models.CASCADE)
    correct = models.BooleanField('Correta?', blank=True, default=False)

    def __str__(self):
        return self.reply[:100]

    class Meta:
        verbose_name = 'Resposta'
        ordering = ['-correct', 'created_at']


def post_save_reply(instance, **kwargs):
    instance.thread.answers = instance.thread.replies.count()
    instance.thread.save()
    if instance.correct:
        instance.thread.replies.exclude(pk=instance.pk).update(correct=False)


def post_delete_reply(instance, **kwargs) :
    instance.thread.answers = instance.thread.replies.count()
    instance.thread.save()


models.signals.post_save.connect(post_save_reply, sender=Reply, dispatch_uid='post_save_replay')
models.signals.post_delete.connect(post_delete_reply, sender=Reply, dispatch_uid='post_delete_replay')
