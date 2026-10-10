"""Turn work/slx/cap-*.png into site/assets/img/sl-*.webp."""
from PIL import Image
SRC = '/home/claude/v4/work/slx/cap-'
DST = '/home/claude/v4/site/assets/img/sl-'
def save(im, slug, q=82):
    im.save(DST + slug + '.webp', 'WEBP', quality=q, method=6); print(slug, im.size)
# 16:10 thumbnails: same slugs and shape (16:10) as the ones resources.html / ai-literacy.html already use
for n in ['boundary-flags', 'nutrition-label', 'supporting-a-survivor', 'reset-kit', 'jeopardy', 'home']:
    im = Image.open(SRC + n + '.png').convert('RGB')
    assert abs(im.width / im.height - 1.6) < .01, (n, im.size)
    save(im.resize((1600, 1000), Image.LANCZOS), n)
# Listen Closer: frame the wheel panel (the tool's own header stays out of the picture)
im = Image.open(SRC + 'listen-closer.png').convert('RGB')      # 2560x1600
x0, y0, w = 200, 140, 2160; h = int(w / 1.6)
save(im.crop((x0, y0, x0 + w, y0 + h)).resize((1600, 1000), Image.LANCZOS), 'listen-closer')
# phone captures, 390x780 @2x
for n in ['boundary-flags', 'nutrition-label', 'supporting-a-survivor', 'reset-kit', 'listen-closer', 'jeopardy']:
    save(Image.open(SRC + n + '-m.png').convert('RGB'), n + '-m')
# the finished Partner Nutrition Label bookmark
save(Image.open(SRC + 'label.png').convert('RGB'), 'label', 86)
# the Lab's FAQ tool
im = Image.open(SRC + 'faq.png').convert('RGB')
save(im.resize((1600, 1000), Image.LANCZOS), 'faq')
