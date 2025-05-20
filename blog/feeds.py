from django.contrib.syndication.views import Feed
from django.urls import reverse
from django.utils import timezone
from blog.models import Post


class LatestEntriesFeed(Feed):
    title = "blog latest posts"
    link = "/rss/feed"
    description = "best blog ever."

    def items(self):
        return Post.objects.filter(
        date_time_published__lte=timezone.now(), status=True)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content