__author__ = 'dkoldyaev'

from django.core.management import BaseCommand

class Command(BaseCommand) :

    def handle(self, *args, **options):

        import time, random, re, pycurl, os
        import transliterate

        from django.core.files import File
        from django.core.files.temp import NamedTemporaryFile

        from urllib.parse import urlparse
        from urllib.request import urlopen
        from grab import Grab

        from picture.models import Picture, Canvas, Genre, Technique, Style
        from museum.models import Museum
        from country.models import Country, City
        from artist.models import Artist

        debug = False
        stop = False

        start_artist = 0
        start_picture = 0
        if len(args) > 0 :
            start_artist = int(args[0])
        if len(args) > 1 :
            start_picture = int(args[1])


        for artist_num, artist in enumerate(Artist.objects.all()) :

            if artist_num < start_artist :
                continue

            if stop :
                break

            parsed_uri= urlparse(artist._data_source)
            domain =    '{uri.scheme}://{uri.netloc}'.format(uri=parsed_uri)

            g = Grab(document_charset='cp1251')
            g.setup(hammer_mode=True, hammer_timeouts=((2, 5), (10, 15), (20, 30)))
            g.go(artist._data_source)

            if domain == 'http://classic-online.ru' :

                pictures_links = g.css_list('.pic_item')

                for picture_num, pic_item in enumerate(pictures_links) :

                    if picture_num < start_picture :
                        continue

                    self.stdout.write('\n%d-%d' % (artist_num, picture_num))

                    if stop :
                        break

                    pic_link = pic_item.find('a').get('href')

                    picture, picture_created = Picture.objects.get_or_create(
                        artist =        artist,
                        _data_source =  pic_link
                    )

                    if picture_created :

                        self.stdout.write('Создан новый Picture из "%s"' % (pic_link))

                    else:

                        pass

                    g.go(domain + pic_link)
                    picture_name_block =    g.doc.select('//h1')[1].node

                    for original_link in g.doc.select('//div[@class="al"]/table/tr[2]/td[2]/div/a') :
                        if original_link.node.text == 'Открыть в полный размер':
                            origin_picture_link = original_link.node.get('href')
                            break

                    # Проверяем, что в названии нет скобок
                    parenthesis_in_name = re.search(r'([^\(]+\([^\)]+\)[^\(]+)\(([^\)]+)\)', picture_name_block.text)
                    if parenthesis_in_name :
                        name_block, years_block =   parenthesis_in_name.groups()
                        picture_name =              name_block.strip()
                        _, year_from, year_to =     re.search(r'((\d{,4})\s*-)?\s*(\d{,4})', years_block).groups()
                    else :
                        picture_name_rule =         re.compile(r'([\w\s\d\-]*\w)\s*(\(((\d{,4})-)?(\d{,4})\))?')
                        picture_name, _1, _2, year_from, year_to = \
                                                    picture_name_rule.search(picture_name_block.text).groups()

                    picture.year_from =     re.sub(r'[^\d]', '', year_from) if year_from else None
                    picture.year_to =       re.sub(r'[^\d]', '', year_to) if year_to else None
                    picture.name =          picture_name

                    picture.save()

                    file_ex =   origin_picture_link.split('.')[-1]
                    transliterate.get_available_language_codes
                    try:
                        filename =  '.'.join([transliterate.slugify(picture_name), file_ex])
                    except:
                        filename =  '.'.join([transliterate.slugify(picture_name, language_code='uk'), file_ex])
                    try:
                        url_content=urlopen(domain+origin_picture_link).read()
                        self.stdout.write('\tЗагружено изображение по URL %s' % (origin_picture_link))
                    except :
                        self.stderr.write('\tОшибка при загрузке изображения по URL %s' % (origin_picture_link))
                        raise

                    temp_image =    NamedTemporaryFile(delete=True)
                    temp_image.write(url_content)
                    temp_image.flush()
                    try :
                        picture.image.save(filename, File(temp_image))
                        self.stdout.write('\tИзображение сохранено %s -> %s' % (filename, picture.image))
                    except :
                        self.stderr.write('\tОшибка сохранения изображения %s -> %s' % (filename, picture.get_content_file_name(filename)))
                        raise

                    for picture_info_selector in g.doc.select('//span[@class="pic_info"]') :

                        picture_info = picture_info_selector.node

                        if 'дата' in picture_info.text.lower() :

                            if re.sub(r'[^\w\d\s]', '', picture_info.text.lower().strip()) == 'дата завершения' :

                                try :
                                    year_to = int(re.sub(r'[^\d]', '', picture_info.tail.strip()))
                                    if picture.year_to is None and year_to :
                                        picture.year_to = year_to
                                except:
                                    pass

                            elif re.sub(r'[^\w\d\s]', '', picture_info.text.lower().strip()) == 'дата начала' :

                                try :
                                    year_from = int(re.sub(r'[^\d]', '', picture_info.tail.strip()))
                                    if picture.year_from is None and year_from:
                                        picture.year_from = year_from
                                except:
                                    pass


                            else :

                                self.stderr.write('\tОщибка при попытке разбора атрибута с датой: "%s"' % picture_info.tail)

                        if 'стиль' in picture_info.text.lower() :

                            style, style_created = Style.objects.get_or_create(
                                name =  picture_info.getnext().text.strip()
                            )
                            picture.style.add(style)

                            if style_created :
                                self.stdout.write('\tСоздан новый стиль: \t%s' % (style.name))

                        if 'жанр' in picture_info.text.lower() :

                            genre, genre_created = Genre.objects.get_or_create(
                                name =  picture_info.getnext().text.strip()
                            )
                            picture.genre.add(genre)

                            if genre_created :
                                self.stdout.write('\tСоздан новый жанр: \t%s' % (genre.name))

                        if 'место' in picture_info.text.lower()  :

                            museum_block = picture_info.getnext()

                            place_rule = re.compile(r'((\w[\w\d\s\-]+)[\w\d]\s*.\s*)?([\w\s\d\-]+[\w\d])\s*(\((\w[\w\d\s\-]*)\))?')
                            _1, museum_city_name, museum_name, _2, museum_country_name = place_rule.search(museum_block.text).groups()

                            country = None
                            city = None
                            if museum_country_name :
                                country, country_created = Country.objects.get_or_create(name=museum_country_name)
                                if country_created :
                                    self.stdout.write('\tСоздана страна: %s' % (country.name))
                                if museum_city_name :
                                    city, city_created = City.objects.get_or_create(
                                        country =   country,
                                        name =      museum_city_name
                                    )
                                    if city_created :
                                        self.stdout.write('\tСоздан город: %s' % (city))

                            picture.museum, museum_created = Museum.objects.get_or_create(
                                name =  museum_name,
                                city =  city,
                                country=country
                            )
                            if museum_created :
                                self.stdout.write('\tСоздан музей: %s' % (picture.museum))

                        if 'техника' in picture_info.text.lower() :

                            technique, technique_created = Technique.objects.get_or_create(
                                name =  picture_info.getnext().text.strip()
                            )
                            picture.technique.add(technique)
                            if technique_created :
                                self.stdout.write('\tСоздана техника: %s' % (technique))

                        if 'материал' in picture_info.text.lower() :

                            canvas, canvas_created = Canvas.objects.get_or_create(
                                name =  picture_info.tail
                            )
                            picture.canvas.add(canvas)
                            if canvas_created :
                                self.stdout.write('\tСоздан материал: %s' % (canvas))

                    picture.save()


