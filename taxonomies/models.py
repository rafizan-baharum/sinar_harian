from django_sorcery.db import databases
from sqlalchemy import ForeignKey, Sequence, UniqueConstraint, Enum
import enum

db = databases.get("default")

# =========================================================================
# taxonomy
# =========================================================================

TaxonomySequence = Sequence('sq_cng_txmy', start=1000)


class Taxonomy(db.Model):
    __tablename__ = 'cng_txmy'

    id = db.Column(db.Integer(), TaxonomySequence, primary_key=True, server_default=TaxonomySequence.next_value())
    parent_id = db.Column(db.Integer(), ForeignKey('cng_txmy.id'))
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return "cng_txmy(id=%r, name=%r, parent_id=%r)" % (
            self.id,
            self.name,
            self.parent_id
        )
