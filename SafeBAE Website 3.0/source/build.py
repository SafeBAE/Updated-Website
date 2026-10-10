"""Build the whole SafeBAE site: python3 build/build.py [module ...]"""
import sys, importlib, time
sys.path.insert(0, '/home/claude/v3/build')
import lib

ORDER = ['pages_home', 'pages_library', 'films_red', 'films_bae', 'films_know', 'films_dating', 'films_oh', 'films_rc',
         'films_men', 'films_rrcr', 'pages_resources', 'pages_vibe', 'pages_skills', 'pages_support', 'pages_support2',
         'pages_students', 'pages_students2', 'pages_adults', 'pages_adults2', 'pages_programs', 'pages_schools', 'pages_schools2',
         'pages_about', 'pages_about2', 'pages_daisy', 'pages_ai', 'pages_choking']
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
        try:
            run(m)
            print('built', m)
        except ModuleNotFoundError as e:
            if e.name != m: raise
            print('skip (not written yet)', m)
    # credits last: it reads credits.jsonl and scans pages
    import pages_about
    if hasattr(pages_about, 'credits'):
        pages_about.credits()
    import search_index
    search_index.build()
    print(len(lib.PAGES), 'pages this run ·', round(time.time() - t, 1), 's')
