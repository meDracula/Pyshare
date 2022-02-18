import app
from app.persistence.models import User
from app.persistence.models import Post
from time import sleep

def update_user_schema():
    user_full = User.find(schema=1).full_or_none()
    for user in user_full:
        user_data = user.__dict__
        user_data['schema'] = 2
        User(user_data).save()
        print(f"User updated {user_data['username']}")
        sleep(0.05)

def update_post_schema():
    post_full = Post.find(schema=1).full_or_none()
    for post in post_full:
        post_data = post.__dict__
        post_data['schema'] = 2
        Post(post_data).save()
        print(f"Post updated {post_data['title']}")
        sleep(0.05)


if __name__ == '__main__':
    print("="*10, "Upgrading Schema", "="*10)
    print("Upgrading users ...")
    update_user_schema()
    print("Upgrading posts ...")
    update_post_schema()
    print("="*10, "Done", "="*10)

