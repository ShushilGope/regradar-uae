CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

.flag-stripe {
  height: 6px;
  background: linear-gradient(90deg, #00732F 0%, #00732F 33%, #FFFFFF 33%, #FFFFFF 66%, #000000 66%, #000000 100%);
  border-radius: 3px; margin-bottom: 24px;
}

.badge-row { display: flex; justify-content: center; gap: 10px; margin-top: 20px; flex-wrap: wrap; }
.badge {
  background: #E0F2ED; color: #00754A; padding: 6px 14px; border-radius: 20px;
  font-size: 0.85rem; font-weight: 600; border: 1px solid #00754A33;
}

div.stButton > button {
  background-color: #00754A; color: white; border-radius: 10px;
  font-weight: 600; padding: 10px 24px; border: none;
}
div.stButton > button:hover { background-color: #005c3a; }

.stTextArea textarea {
  border-radius: 12px !important; border: 1.5px solid #D8CFC0 !important;
  background: #FFFFFF !important; font-family: 'Inter', monospace !important;
  font-size: 0.95rem !important; padding: 16px !important;
  box-shadow: 0 1px 3px rgba(0,0,0,0.05) !important;
  transition: border-color 0.2s, box-shadow 0.2s !important;
}
.stTextArea textarea:focus {
  border-color: #00754A !important;
  box-shadow: 0 0 0 3px rgba(0,117,74,0.15) !important;
}
.block-container {
  padding-top: 1.5rem !important;
}
</style>
"""

HERO_IMAGE_CSS = """
<style>
.hero-bg {
  background: linear-gradient(rgba(10,40,30,0.75), rgba(10,40,30,0.85)),
              url('https://images.unsplash.com/photo-1512453979798-5ea266f8880c?w=1600&q=80');
  background-size: cover;
  background-position: center;
  border-radius: 20px;
  padding: 60px 30px;
  margin-bottom: 30px;
  text-align: center;
}
.hero-bg h1 { color: #FFFFFF; font-size: 3rem; font-weight: 800; margin-bottom: 8px; }
.hero-bg p { color: #E8F0EC; font-size: 1.15rem; max-width: 620px; margin: 0 auto; }

.example-card {
  background: #FFFFFF; border-radius: 14px; padding: 24px 28px;
  max-width: 720px; margin: 30px auto 0 auto; text-align: left;
  box-shadow: 0 8px 24px rgba(0,0,0,0.15);
  position: relative;
}
.example-card .tag {
  display: inline-block; background: #FFF3CD; color: #8A6D00;
  font-size: 0.7rem; font-weight: 700; letter-spacing: 0.5px;
  padding: 3px 10px; border-radius: 20px; margin-bottom: 12px;
  text-transform: uppercase;
}
.example-card .q { font-weight: 700; color: #00754A; margin-bottom: 8px; }
.example-card .a { color: #333; font-size: 0.92rem; line-height: 1.6; }
.example-card .cite { color: #888; font-size: 0.8rem; margin-top: 10px; }
</style>
"""

FLIP_CARDS_CSS = """
<style>
.flip-grid { display: flex; justify-content: center; gap: 24px; margin: 40px 0; flex-wrap: wrap; perspective: 1000px; }
.flip-card { background: transparent; width: 260px; height: 280px; }
.flip-card-inner {
  position: relative; width: 100%; height: 100%; text-align: center;
  transition: transform 0.6s; transform-style: preserve-3d;
  box-shadow: 0 4px 16px rgba(0,0,0,0.08); border-radius: 14px;
}
.flip-card:hover .flip-card-inner { transform: rotateY(180deg); }
.flip-card-front, .flip-card-back {
  position: absolute; width: 100%; height: 100%; backface-visibility: hidden;
  border-radius: 14px; display: flex; flex-direction: column;
  align-items: center; justify-content: center; padding: 20px;
}
.flip-card-front { background: white; border: 1px solid #E8DDD0; }
.flip-card-front img { width: 70px; height: 70px; border-radius: 50%; object-fit: cover; margin-bottom: 14px; }
.flip-card-front h4 { color: #00754A; font-size: 1.05rem; margin: 0; }
.flip-card-back {
  background: linear-gradient(135deg, #00754A, #00543a); color: white;
  transform: rotateY(180deg); font-size: 0.85rem; line-height: 1.5;
}
.flip-card-back strong { display: block; margin-bottom: 8px; font-size: 0.95rem; }
</style>
"""

SECTION_BG_CSS = """
<style>
.section-features {
  background: linear-gradient(rgba(250,246,240,0.93), rgba(250,246,240,0.93)),
              url('https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=1600&q=80');
  background-size: cover; background-position: center;
  border-radius: 20px; padding: 40px 20px; margin: 30px 0;
}
.footer {
  background: linear-gradient(rgba(240,234,224,0.92), rgba(240,234,224,0.92)),
              url('https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=1600&q=80');
  background-size: cover; background-position: center;
  margin-top: 60px; padding: 40px 20px; border-radius: 16px; text-align: center; color: #333;
}
.footer h3 { color: #00754A; margin-bottom: 12px; }
.footer p { max-width: 750px; margin: 0 auto 8px auto; line-height: 1.6; }
</style>
"""