# coding=utf-8
from haystack import indexes
from ec_goods.models import GoodsInfo


# 指定对于某个类的某些数据建立索引
class GoodsIndex(indexes.SearchIndex, indexes.Indexable):
    # text是索引字段
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return GoodsInfo

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
