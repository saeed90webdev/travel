from django.contrib.sitemaps import Sitemap
from django.utils import timezone

from blog.models import Post


class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Post.objects.filter(date_time_published__lte=timezone.now(), status=True)

    def lastmod(self, obj):
        return obj.date_time_published