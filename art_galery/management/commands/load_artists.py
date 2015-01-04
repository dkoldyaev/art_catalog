from lxml.doctestcompare import strip

__author__ = 'dkoldyaev'

from django.core.management import BaseCommand

import time
import random
import re

from urllib.request import pathname2url, urlopen
from grab import Grab

from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from optparse import make_option

from artist.models import Artist, School
from picture.models import Style
from country.models import Country, City, Nationality

from art_galery.settings import LANGUAGES, MODELTRANSLATION_DEFAULT_LANGUAGE

debug = False


class Command(BaseCommand) :

    option_list = BaseCommand.option_list + (

        make_option('--skip_load_artist_lists',
            action='store_true',
            default=False,
            help='Do not load artist lists'),
        ) + (

        make_option('--skip_load_artist_detail',
            action='store_true',
            default=False,
            help='Do not load artist detail'),
        ) + (

        make_option('--artist_slug',
            action='append',
            help='Store custom artist slug'),
        ) + (

        make_option('--artist_detail_start_id',
            action='store',
            type='int',
            default=0,
            help='Load artist detail for all artists with id__gte=--artist_detail_start_id'),
        )

    def handle(self, *args, **options):

        domain = 'http://www.wikiart.org'
        artist_slugs = args

        g = Grab(document_charset='UTF-8')
        g.setup(hammer_mode=True, hammer_timeouts=((2, 5), (10, 15), (20, 30)))

        if not options['skip_load_artist_lists'] :

            from string import ascii_uppercase

            artist_list = ['/{language}/alphabet/{letter}'.format(letter=letter, language='en') for letter in ascii_uppercase]

            if not options['artist_slug'] :

                for artist_list_page in artist_list :

                    continue

                    artist_list_url = domain + pathname2url(artist_list_page)

                    self.stdout.write('Разбор страницы %s' % (artist_list_url,))

                    try :   g.go(artist_list_url)
                    except:
                        self.stderr.write('Ошибка загрузки страницы %s' % (artist_list_url,))
                        raise

                    links_elements = g.css_list('.pozRel > a')

                    for link_element in links_elements :

                        link = link_element.get('href')
                        artist_slug = link.split('/')[-1]

                        artist, created = Artist.objects.get_or_create(
                            slug =  artist_slug
                        )
                        if created :
                            self.stdout.write('\tХудожник: "{slug}"'.format(slug=artist_slug))

            else :

                for artist_slug in options['artist_slug'] :

                    artist, created = Artist.objects.get_or_create(
                        slug =  artist_slug
                    )
                    if created :
                        self.stdout.write('Художник: "{slug}"'.format(slug=artist_slug))

        if options['skip_load_artist_detail'] :

            return

        artist_url_template = '/{language}/{artist_slug}'

        self.stdout.write('\nЗагружаем подробнсти')

        artists_list = Artist.objects.all().order_by('id')\
            .filter(id__gte=options['artist_detail_start_id']).exclude(slug=None)

        for artist_num, artist in enumerate(artists_list) :

            self.stdout.write('\n%d\nХудожник "%s"' % (artist.id, artist.slug))

            for lang, _ in LANGUAGES :

                self.stdout.write('\tLANG: %s' % lang)

                page_url = domain + pathname2url(artist_url_template.format(language=lang, artist_slug=artist.slug))
                try:
                    g.go(page_url)
                    self.stdout.write('\t\tЗагрузка данных по URL "%s"' % page_url)
                except:
                    self.stdout.write('\t\tОшибка загрузки данных по URL "%s"' % page_url)
                    raise

                if g.response.code != 200 :
                    self.stdout.write('\t\tОшибка загрузки данных 404 по URL "%s"' % page_url)
                    artist.public = False
                    continue

                try:
                    artist.origin_name = g.css('.tt30 h2').text.strip()
                    self.stdout.write('\t\tПолное имя "%s"' % artist.origin_name)
                except:
                    artist.origin_name = None
                    self.stderr.write('\t\tПолное имя не найдено ')

                for prop in g.css_list('.DataProfileBox .b0') :

                    try:
                        prop_name = re.sub(r'[^\w\d\s\-]', '', prop.find('b').text.lower())
                    except:
                        continue

                    if prop.find('a/span') is not None:

                        self.stdout.write('\t\tРасширенное свойство "%s"' % prop.find('a/span').get('itemprop'))

                        if prop.find('a/span').get('itemprop') == 'nation' :

                            self.stdout.write('\t\t\tНашли поле "национальность" %s' % prop.find('a/span').get('itemprop'))

                            nationality_url = prop.find('a').get('href').split('/')[-1]
                            nationality, nationality_created = Nationality.objects.get_or_create(
                                slug = nationality_url
                            )
                            if nationality_created :
                                self.stdout.write('\t\t\t\tДобавлена национальность %s' % nationality_url)
                            name_lang_field = 'name_{language}'.format(language=lang)
                            setattr(nationality, name_lang_field, prop.find('a/span').text)
                            nationality.save()
                            self.stdout.write('\t\t\t\tНациональность %s -- обновлено название: %s' % (nationality_url, getattr(nationality, name_lang_field)))
                            artist.nationality.add(nationality)

                        if prop.find('a/span').get('itemprop') == 'art movement' :

                            self.stdout.write('\t\t\tНашли поле "направление" %s' % prop.find('a/span').get('itemprop'))

                            for style_block in prop.findall('a') :

                                style_url = style_block.get('href').split('/')[-1]
                                style, style_created = Style.objects.get_or_create(
                                    slug = style_url
                                )
                                if style_created :
                                    self.stdout.write('\t\t\t\tДобавлено направление %s' % style_url)
                                style_name_field = 'name_{language}'.format(language=lang)
                                setattr(style, style_name_field, style_block.find('span').text)
                                style.save()
                                self.stdout.write('\t\t\t\tНаправление %s -- обновлено название: %s' % (style_url, getattr(style, style_name_field)))

                                artist.style.add(style)

                        if prop.find('a/span').get('itemprop') == 'painting school' :

                            self.stdout.write('\t\t\tНашли поле "школа" %s' % prop.find('a/span').get('itemprop'))

                            for school_block in prop.findall('a') :

                                school_url = school_block.get('href').split('/')[-1]
                                school, school_created = School.objects.get_or_create(
                                    slug = school_url
                                )
                                if school_created :
                                    self.stdout.write('\t\t\t\tДобавлена школа %s' % school_url)
                                school_name_field = 'name_{language}'.format(language=lang)
                                setattr(school, school_name_field, school_block.find('span').text)
                                school.save()
                                self.stdout.write('\t\t\t\tШкола %s -- обновлено название: %s' % (school_url, getattr(school, school_name_field)))

                                artist.school.add(school)

                    elif prop.find('span') is not None :

                        self.stdout.write('\t\t\tСвойство "%s"' % prop.find('span').get('itemprop'))

                        if prop.find('span').get('itemprop') == 'birthDate' :

                            try:
                                artist.years_from = int(re.search(r'[\d]{4}', prop.find('span').text).group(0))
                                self.stdout.write('\t\t\t\tРаспознан год рождения <%d>' % artist.years_from)
                            except:
                                self.stderr.write('\t\t\t\tОшибка парсинга года рождения <%s>' % prop.find('span').text)

                        elif prop.find('span').get('itemprop') == 'dearthDate' :

                            try:
                                artist.years_to = int(re.search(r'[\d]{4}', prop.find('span').text).group(0))
                                self.stdout.write('\t\t\t\tРаспознан год смерти <%d>' % artist.years_to)
                            except:
                                self.stderr.write('\t\t\t\tОшибка парсинга года смерти <%s>' % prop.find('span').text)

                    elif prop.find('b').tail.strip() :

                        self.stdout.write('\t\t\tДоп. инфа "%s: %s"' % (prop_name, prop.find('b').tail.strip()))

                        try:    artist._comment +=  '%s\t\t\t\t%s: %s\n' % (lang, prop_name, prop.find('b').tail.strip())
                        except: artist._comment =   '%s\t\t\t\t%s: %s\n' % (lang, prop_name, prop.find('b').tail.strip())

                name_raw = g.css('.tt30 h1').text.split()
                name = []
                surname = []

                self.stdout.write('\t\tРазбор имени %s (%s)' % (g.css('.tt30 h1').text, str(name_raw)))

                try:
                    while name_raw :
                        name_part = name_raw.pop(0)
                        name.append(name_part)
                        if name_part != name_part.lower() :
                            break
                    setattr(artist, 'name_{language}'.format(language=lang), ' '.join(name))
                    self.stdout.write('\t\tИмя {%s}: %s' % (lang, getattr(artist, 'name_{language}'.format(language=lang))))
                except:
                    self.stderr.write('\t\tОшибка парсинга имени {%s}: %s' % (lang, g.css('.tt30 h1').text))
                    artist.name = None

                try:
                    surname.append(name_raw.pop())
                    while name_raw :
                        if name_raw[-1].lower() != name_raw[-1] :
                            break
                        else :
                            surname = [name_raw.pop()] + surname
                    setattr(artist, 'surname_{language}'.format(language=lang), ' '.join(surname))
                    self.stdout.write('\t\tФамилия {%s}: %s' % (lang, getattr(artist, 'surname_{language}'.format(language=lang))))
                except:
                    self.stderr.write('\t\tОшибка парсинга фамилии {%s}: %s' % (lang, g.css('.tt30 h1').text))
                    artist.surname = None

                try:
                    setattr(artist, 'addition_name_{language}'.format(language=lang), ' '.join(name_raw))
                    self.stdout.write('\t\tДоп. имя {%s}: %s' % (lang, getattr(artist, 'addition_name_{language}'.format(language=lang))))
                except:
                    if name_raw :
                        self.stderr.write('\t\tОшибка парсинга доп. имени {%s}: %s' % (lang, g.css('.tt30 h1').text))
                    artist.addition_name = None

                setattr(artist, '_data_source_{language}'.format(language=lang), page_url)

                try :
                    wiki_link = g.doc.select('//table[@class="mt10"]/tr[2]/td/a').node()
                    if wiki_link is not None and 'wikipedia' in wiki_link.get('href') :
                        setattr(artist, 'link_wiki_{language}'.format(language=lang), wiki_link.get('href'))
                        self.stdout.write('\t\tСсылка на вики {%s}: %s' % (lang, getattr(artist, 'link_wiki_{language}'.format(language=lang))))
                except:
                    self.stderr.write('\t\tОшибка парсинга ссылки на wiki')

            try :
                image_link = g.css('.pozRel img').get('src').split('!')[0]
                self.stdout.write('\tЗагружаем картинку: %s' % (image_link))
                if image_link.find('http') == 0 :
                    pass
                elif image_link[0] == '/' :
                    image_link = domain + image_link
                else :
                    self.stderr.write('\tНепонятный URL картинки')
                    image_link = None

                if image_link is not None :

                    try:
                        url_content=urlopen(image_link).read()
                        self.stdout.write('\tЗагружено изображение по URL %s' % (image_link))
                    except :
                        self.stderr.write('\tОшибка при загрузке изображения по URL %s' % (image_link))
                        raise

                    temp_image =    NamedTemporaryFile(delete=True)
                    temp_image.write(url_content)
                    temp_image.flush()

                    file_ext =  image_link.split('.')[-1]
                    filename = '.'.join([artist.slug, file_ext])

                    try :
                        artist.portrait.save(filename, File(temp_image))
                        self.stdout.write('\tИзображение сохранено %s -> %s' % (filename, artist.portrait))
                    except :
                        self.stderr.write('\tОшибка сохранения изображения %s' % (filename))
                        raise

            except :
                self.stderr.write('\tНе могу найти картинку на странице')

            try:
                artist.save()
            except:
                self.stderr.write('\tОшибка сохранение %s (%s)' % (artist.__str__(), artist.slug))

            time.sleep(random.randint(0, 5)*random.random())