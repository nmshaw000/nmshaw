PY?=python
PELICAN?=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
THEMEDIR=$(BASEDIR)/theme
CSSDIR=$(THEMEDIR)/static/css
JSDIR=$(THEMEDIR)/static/js
SCSSDIR=$(THEMEDIR)/styling
INPUTDIR=$(BASEDIR)/content
CACHEDIR=$(BASEDIR)/cache
OUTPUTDIR=$(BASEDIR)/output
PLUGINSDIR=$(BASEDIR)/plugins
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

# pelican plugins
I18N_SUBSITES_DIR=$(PLUGINSDIR)/i18n_subsites

GITHUB_PROJECT_PAGES_BRANCH=gh-pages
GITHUB_USER_NAME=YOUR_USERNAME


default: html serve

download:
	@echo "download pelican i18n_subsites plugin ..."
	[ ! -d $(I18N_SUBSITES_DIR) ] || rm -rf $(I18N_SUBSITES_DIR)
	mkdir -p $(I18N_SUBSITES_DIR)
	wget -P $(I18N_SUBSITES_DIR) https://raw.githubusercontent.com/getpelican/pelican-plugins/master/i18n_subsites/__init__.py
	wget -P $(I18N_SUBSITES_DIR) https://raw.githubusercontent.com/getpelican/pelican-plugins/master/i18n_subsites/i18n_subsites.py

scss:
	[ -d $(CSSDIR) ] || mkdir -p $(CSSDIR)
	$(PY) -mscss < $(SCSSDIR)/style.scss -I $(SCSSDIR) -o $(CSSDIR)/style.css

js:
	[ -d $(JSDIR) ] || mkdir -p $(JSDIR)
	cp theme/javascript/app.js $(JSDIR)/app.js

html: scss js
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)
	[ ! -d $(CACHEDIR) ]  || rm -rf $(CACHEDIR)

serve:
ifdef PORT
	cd $(OUTPUTDIR) && $(PY) -m pelican.server $(PORT)
else
	cd $(OUTPUTDIR) && $(PY) -m pelican.server
endif

publish: scss js clean
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

github_project_page:
	# http://docs.getpelican.com/en/latest/tips.html#publishing-to-github
	ghp-import $(OUTPUTDIR)
	@echo "upload to Project Pages ..."
	git push origin $(GITHUB_PROJECT_PAGES_BRANCH)


.PHONY: download scss html clean serve publish github_project_page
