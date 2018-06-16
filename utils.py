import glob
import markdown
import os
import requests

from django.conf import settings
from django.templatetags.static import static

BLOG_DIR = 'blog_posts'

class BlogPostManager(object):

    def __init__(self, src=None):
        self.posts = {}
        self.src = src if src else BLOG_DIR
        self.build_all()

    def build_all(self):
        """
        Build html pages from all markdown blog posts
        in source directory.
        """
        for index, filepath in enumerate(
            glob.glob('%s/*.md' % static(self.src))
        ):
            # builds post and adds it to posts
            self.build(filepath, index)

    def build(self, filepath, index):
        """
        Build html page from given markdown blog post filepath
        """
        md = markdown.Markdown(extensions=['markdown.extensions.meta'])
        filename = os.path.basename(filepath)
        filename = '%s.html' % filename.split('.')[0]
        content = md.convert(get_content(filepath))

        if content:
            post = {}
            post['id'] = index
            post['content'] = content
            post['filename'] = filename
            post['title'] = md.Meta['title'][0]
            post['author'] = md.Meta['author'][0]
            post['subtitle'] = md.Meta['subtitle'][0]
            post['date'] = md.Meta['date'][0]
            self.posts[index] = post

    def get_post(self, index):
        """
        Return post by index if it exists.
        """
        return self.posts.get(index)

    def get_feed(self):
        """
        Return list of blogs post without content.
        """
        feed = []
        for index, post in self.posts.items():
            item = post.copy()
            del item['content']
            feed.append(item)
        return feed


def get_content(filepath):
    """
    Return conteents of filepath
    """
    return open(filepath, 'r').read()
