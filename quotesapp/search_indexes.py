from haystack import indexes
from quotesapp.models import Quote


class QuoteIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    author = indexes.CharField(model_attr='author', faceted=True)
    tag = indexes.CharField(model_attr='tag', faceted=True)

    def get_model(self):
        return Quote

    def index_queryset(self):
        return self.get_model().objects.all()
