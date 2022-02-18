from app.persistence.models import Tags


def create_new_tag(tag):
    tag = Tags({'schema': 1, 'tag': tag})
    return tag.save().acknowledged


def get_tag(**kwargs):
    return Tags.find(**kwargs).first_or_none()


def iter_tags(start, stop):
    return Tags.iter(start, stop).full_or_none()


def delete_tag(tag):
    return Tags.delete(tag=tag)
