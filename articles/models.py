from django_sorcery.db import databases
from sqlalchemy import ForeignKey, Sequence, UniqueConstraint, Enum
import enum

db = databases.get("default")

# =========================================================================
# article
# =========================================================================

ArticleSequence = Sequence('sq_cng_atcl', start=1000)


class SocialMedia(enum.Enum):
    TWITTER = 1
    FACEBOOK = 2
    OTHERS = 3


class Article(db.Model):
    __tablename__ = 'cng_atcl'
    __table_args__ = (UniqueConstraint('url', name='uq_cng_atcl_url'),)
    id = db.Column(db.Integer(), ArticleSequence, primary_key=True, server_default=ArticleSequence.next_value())
    title = db.Column(db.String(length=200))
    summary = db.Column(db.String(length=200))
    url = db.Column(db.String(length=200))
    published_date = db.Column(db.DateTime())

    def __repr__(self):
        return "cng_atcl(id=%r, title=%r)" % (
            self.id,
            self.title
        )

CommentSequence = Sequence('sq_cng_cmnt', start=1000)


class Comment(db.Model):
    __tablename__ = 'cng_cmnt'
    id = db.Column(db.Integer(), CommentSequence, primary_key=True, server_default=CommentSequence.next_value())
    article_id = db.Column(db.Integer(), ForeignKey("cng_atcl.id"), nullable=False)
    message = db.Column(db.String(length=200))
    score = db.Column(db.Integer(), default=0)
    social_media = db.Column(db.Enum(SocialMedia, native_enum=False))
    # comment = db.ManyToOne(Article, backref=db.backref("comments", cascade="all, delete-orphan"))


