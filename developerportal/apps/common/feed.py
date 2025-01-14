from django.contrib.syndication.views import Feed

from developerportal.apps.articles.models import Article


class RssFeeds(Feed):
    title = "Mozilla Developer articles feed"
    link = "/article-feed/"
    description = "Articles published"

    def items(self):
        return Article.published_objects.all().order_by("-date")[:20]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description
