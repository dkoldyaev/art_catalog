from lxml.doctestcompare import strip

__author__ = 'dkoldyaev'

from django.core.management import BaseCommand

class Command(BaseCommand) :

    def handle(self, *args, **options):

        import time
        import random
        import urllib
        import re

        from grab import Grab
        from string import ascii_uppercase

        from artist.models import Artist
        from country.models import Country

        for domain in args :

            if domain == 'http://classic-online.ru' :

                stop = False

                artists_lists = map(
                    lambda path:domain+path,
                    ['/ru/painters/%C0',
                     '/ru/painters/%C1',
                     '/ru/painters/%C2',
                     '/ru/painters/%C3',
                     '/ru/painters/%C4',
                     '/ru/painters/%C5',
                     '/ru/painters/%C6',
                     '/ru/painters/%C7',
                     '/ru/painters/%C8',
                     '/ru/painters/%C9',
                     '/ru/painters/%CA',
                     '/ru/painters/%CB',
                     '/ru/painters/%CC',
                     '/ru/painters/%CD',
                     '/ru/painters/%CE',
                     '/ru/painters/%CF',
                     '/ru/painters/%D0',
                     '/ru/painters/%D1',
                     '/ru/painters/%D2',
                     '/ru/painters/%D3',
                     '/ru/painters/%D4',
                     '/ru/painters/%D5',
                     '/ru/painters/%D6',
                     '/ru/painters/%D7',
                     '/ru/painters/%D8',
                     '/ru/painters/%D9',
                     '/ru/painters/%DD',
                     '/ru/painters/%DE',
                     '/ru/painters/%DF'])

                debug = True

                for artist_url in artists_lists :

                    self.stdout.write('')
                    self.stdout.write('--- %s ---' % artist_url)

                    g = Grab(document_charset='cp1251')
                    g.setup(hammer_mode=True, hammer_timeouts=((2, 5), (10, 15), (20, 30)))
                    g.go(artist_url)

                    artists_rows = g.css_list('div.al tr.even')

                    parsing_rule = re.compile(r'\s*(\w[\w\s\-\(\)]*)\s*,\s*(\w[\w\s\-]*)?\s*(\((род\.\s*)?(\d{,4})-?(\d{,4})\))*', flags=re.UNICODE)
                    country_rule = re.compile(r'\s*(\w[\w\d\s\-]*\w)\s*', flags=re.UNICODE)

                    for artists_row in artists_rows :

                        artist_teh_name =   artists_row.get('id')
                        artist_link =       artists_row.getchildren()[2].find('a')
                        country_span =      artists_row.getchildren()[2].find('span')

                        try :

                            if debug:
                                import pdb
                                pdb.set_trace()

                            surname, name, _1,  _2, year_start, year_finish = parsing_rule.search(artist_link.text).groups()
                        except:
                            self.stderr.write('Ошибка при разборе строки "%s"' % artist_link.text)
                            raise

                        try :
                            country_name = country_rule.search(country_span.text).groups()[0]
                        except:
                            self.stderr.write('Ошибка при разборе строки "%s"' % country_span.text)
                            raise

                        artist, created = Artist.objects.get_or_create(
                            name =          strip(name),
                            surname =       strip(surname),
                            years_from =    int(year_start) if year_start else None,
                            years_to =      int(year_finish) if year_finish else None,
                            _data_source =  domain + artist_link.get('href'),
                        )

                        country, country_created = Country.objects.get_or_create(
                            name =          country_name
                        )

                        artist.country.add(country)

                        if created :

                            self.stdout.write(artist_link.text)
                            self.stdout.write('\t\t %s, %s %d-%d (%s)' % (
                                artist.name,
                                artist.surname,
                                artist.years_from if artist.years_from is not None else 0,
                                artist.years_to if artist.years_to is not None else 0,
                                artist._data_source)
                            )

                        artist.save()

                    time.sleep(random.randint(0, 10)*random.random())