"""Build the whole SafeBAE site: python3 build/build.py [module ...]"""
import sys, importlib, time
sys.path.insert(0, '/home/claude/v2/build')
import lib

ORDER = ['pages_home', 'pages_library', 'films_red', 'films_bae', 'films_know', 'films_dating', 'films_oh', 'films_rc',
         'films_men', 'films_rrcr', 'pages_resources', 'pages_support', 'pages_students', 'pages_adults', 'pages_schools',
         'pages_about', 'pages_ai', 'pages_choking']
FILM_BUILDERS = {}


def run(name):
    mod = importlib.import_module(name)
    if hasattr(mod, 'build'):
        mod.build()
    elif hasattr(mod, 'home'):
        mod.home()
    else:
        raise SystemExit(f'{name} has no build()')


if __name__ == '__main__':
    t = time.time()
    mods = sys.argv[1:] or ORDER
    for m in mods:
        run(m)
        print('built', m)
    # credits last: it reads credits.jsonl and scans pages
    import pages_about
    if hasattr(pages_about, 'credits'):
        pages_about.credits()
    import search_index
    search_index.build()
    print(len(lib.PAGES), 'pages this run ·', round(time.time() - t, 1), 's')
