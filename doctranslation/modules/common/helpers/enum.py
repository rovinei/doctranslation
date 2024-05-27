class EnumHelperMixin:
    @classmethod
    def get_choices(cls):
        return tuple((obj.value, obj.name) for obj in cls)

    @classmethod
    def values(cls):
        return [obj.value for obj in cls]

    @classmethod
    def names(cls):
        return [obj.name for obj in cls]
