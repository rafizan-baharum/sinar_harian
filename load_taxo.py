import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sinar_harian.settings")
django.setup()

from articles.models import Article, db
from taxonomies.models import Taxonomy

t1 = Taxonomy(name="Politic")
db.add(t1)
db.flush()
db.commit()
t2 = Taxonomy(name="Political Figures", parent_id=t1.id)
db.add(t2)
db.flush()
db.commit()

t3 = Taxonomy(name="Azmin Ali", parent_id=t2.id)
t4 = Taxonomy(name="Mahathir Mohamad", parent_id=t2.id)
t5 = Taxonomy(name="Anwar Ibrahim", parent_id=t2.id)
t6 = Taxonomy(name="Najib Razak", parent_id=t2.id)
db.add(t3)
db.add(t4)
db.add(t5)
db.add(t6)
db.flush()
db.commit()
