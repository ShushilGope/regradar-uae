CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

.flag-stripe {
  height: 6px;
  background: linear-gradient(90deg, #00732F 0%, #00732F 33%, #FFFFFF 33%, #FFFFFF 66%, #000000 66%, #000000 100%);
  border-radius: 3px; margin-bottom: 24px;
}

.hero {
  text-align: center; padding: 60px 20px 40px 20px;
}
.hero h1 {
  font-size: 3rem; font-weight: 800; color: #00754A; margin-bottom: 8px;
}
.hero p { font-size: 1.15rem; color: #4A4A4A; max-width: 600px; margin: 0 auto; }

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
  border-radius: 10px; border: 1px solid #D8CFC0;
}
</style>
"""

HERO_IMAGE_CSS = """
<style>
.hero-img {
  width: 100%; max-height: 320px; object-fit: cover;
  border-radius: 16px; margin: 20px 0 30px 0;
  box-shadow: 0 8px 24px rgba(0,0,0,0.12);
}
.footer {
  margin-top: 60px; padding: 40px 20px; background: #F0EAE0;
  border-radius: 16px; text-align: center; color: #4A4A4A;
}
.footer h3 { color: #00754A; margin-bottom: 12px; }
.footer p { max-width: 700px; margin: 0 auto 8px auto; line-height: 1.6; }
.feature-grid {
  display: flex; justify-content: center; gap: 24px; margin: 30px 0; flex-wrap: wrap;
}
.feature-card {
  background: white; border: 1px solid #E8DDD0; border-radius: 12px;
  padding: 20px; width: 220px; text-align: center;
}
.feature-card h4 { color: #00754A; margin-bottom: 6px; font-size: 1rem; }
.feature-card p { font-size: 0.85rem; color: #666; }
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

/* Modern dev-style input */
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
</style>
"""