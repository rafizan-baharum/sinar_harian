import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sinar_harian.settings")
django.setup()

from articles.models import Article, Comment, db
from django.utils import timezone

a1 = Article(title="Sebar khabar angin kerja sia-sia",
             summary="pihak yang menyebarkan khabar angin bertujuan merobohkan permuafakatan",
             url="https://www.sinarharian.com.my/article/42434/EDISI/Selangor-KL/Sebar-khabar-angin-kerja-sia-sia",
             published_date=timezone.now())

a2 = Article(title="Krisis Anwar-Azmin tidak sampai pecah-belahkan parti",
             summary="Pengerusi PKR Sarawak, Baru Bian percaya kemelut yang berlaku dalam Parti Keadilan Rakyat (PKR)",
             url="https://www.sinarharian.com.my/article/42302/BERITA/Politik/Krisis-Anwar-Azmin-tidak-sampai-pecah-belahkan-parti",
             published_date=timezone.now())

a3 = Article(title="Lima industri dikenal pasti Selangor: Amirudin",
             summary="Kerajaan negeri dalam proses mengenal pasti lima industri utama di negeri ini yang memerlukan kerjasama",
             url="https://www.sinarharian.com.my/article/42373/EDISI/Selangor-KL/Lima-industri-dikenal-pasti-Selangor-Amirudin",
             published_date=timezone.now())


db.add(a1)
db.add(a2)
db.add(a3)
db.flush()
db.commit()