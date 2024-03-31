# Generated by Django 4.2.4 on 2024-03-30 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeClasse', models.CharField(max_length=9, unique=True, verbose_name='Code de la classe')),
                ('libelleClasse', models.CharField(max_length=50, unique=True, verbose_name='Nom de la classe')),
            ],
            options={
                'verbose_name': 'Classe',
                'verbose_name_plural': 'Classes',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Devoir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeDevoir', models.PositiveIntegerField(verbose_name='Devoir ')),
                ('typeDevoir', models.CharField(choices=[('INTERRO', 'INTERROGATION'), ('DEVOIR', 'DEVOIR')], default='INTERRO', max_length=7)),
                ('denominationDevoir', models.CharField(max_length=50, null=True, verbose_name='Denomination')),
            ],
            options={
                'verbose_name': 'Devoir',
                'verbose_name_plural': 'Devoirs',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Filiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeFiliere', models.CharField(max_length=4, unique=True, verbose_name='Code')),
                ('nomFiliere', models.CharField(max_length=50, unique=True, verbose_name='Nom ')),
            ],
            options={
                'verbose_name': 'Filiere',
                'verbose_name_plural': 'Filieres',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Trimestre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeTrimestre', models.PositiveIntegerField(unique=True, verbose_name='Trimestre ')),
            ],
            options={
                'verbose_name': 'Trimestre',
                'verbose_name_plural': 'Trimestres',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anneeDebut', models.IntegerField(choices=[(1900, '1900'), (1901, '1901'), (1902, '1902'), (1903, '1903'), (1904, '1904'), (1905, '1905'), (1906, '1906'), (1907, '1907'), (1908, '1908'), (1909, '1909'), (1910, '1910'), (1911, '1911'), (1912, '1912'), (1913, '1913'), (1914, '1914'), (1915, '1915'), (1916, '1916'), (1917, '1917'), (1918, '1918'), (1919, '1919'), (1920, '1920'), (1921, '1921'), (1922, '1922'), (1923, '1923'), (1924, '1924'), (1925, '1925'), (1926, '1926'), (1927, '1927'), (1928, '1928'), (1929, '1929'), (1930, '1930'), (1931, '1931'), (1932, '1932'), (1933, '1933'), (1934, '1934'), (1935, '1935'), (1936, '1936'), (1937, '1937'), (1938, '1938'), (1939, '1939'), (1940, '1940'), (1941, '1941'), (1942, '1942'), (1943, '1943'), (1944, '1944'), (1945, '1945'), (1946, '1946'), (1947, '1947'), (1948, '1948'), (1949, '1949'), (1950, '1950'), (1951, '1951'), (1952, '1952'), (1953, '1953'), (1954, '1954'), (1955, '1955'), (1956, '1956'), (1957, '1957'), (1958, '1958'), (1959, '1959'), (1960, '1960'), (1961, '1961'), (1962, '1962'), (1963, '1963'), (1964, '1964'), (1965, '1965'), (1966, '1966'), (1967, '1967'), (1968, '1968'), (1969, '1969'), (1970, '1970'), (1971, '1971'), (1972, '1972'), (1973, '1973'), (1974, '1974'), (1975, '1975'), (1976, '1976'), (1977, '1977'), (1978, '1978'), (1979, '1979'), (1980, '1980'), (1981, '1981'), (1982, '1982'), (1983, '1983'), (1984, '1984'), (1985, '1985'), (1986, '1986'), (1987, '1987'), (1988, '1988'), (1989, '1989'), (1990, '1990'), (1991, '1991'), (1992, '1992'), (1993, '1993'), (1994, '1994'), (1995, '1995'), (1996, '1996'), (1997, '1997'), (1998, '1998'), (1999, '1999'), (2000, '2000'), (2001, '2001'), (2002, '2002'), (2003, '2003'), (2004, '2004'), (2005, '2005'), (2006, '2006'), (2007, '2007'), (2008, '2008'), (2009, '2009'), (2010, '2010'), (2011, '2011'), (2012, '2012'), (2013, '2013'), (2014, '2014'), (2015, '2015'), (2016, '2016'), (2017, '2017'), (2018, '2018'), (2019, '2019'), (2020, '2020'), (2021, '2021'), (2022, '2022'), (2023, '2023'), (2024, '2024'), (2025, '2025'), (2026, '2026'), (2027, '2027'), (2028, '2028'), (2029, '2029'), (2030, '2030'), (2031, '2031'), (2032, '2032'), (2033, '2033'), (2034, '2034'), (2035, '2035'), (2036, '2036'), (2037, '2037'), (2038, '2038'), (2039, '2039'), (2040, '2040'), (2041, '2041'), (2042, '2042'), (2043, '2043'), (2044, '2044'), (2045, '2045'), (2046, '2046'), (2047, '2047'), (2048, '2048'), (2049, '2049'), (2050, '2050'), (2051, '2051'), (2052, '2052'), (2053, '2053'), (2054, '2054'), (2055, '2055'), (2056, '2056'), (2057, '2057'), (2058, '2058'), (2059, '2059'), (2060, '2060'), (2061, '2061'), (2062, '2062'), (2063, '2063'), (2064, '2064'), (2065, '2065'), (2066, '2066'), (2067, '2067'), (2068, '2068'), (2069, '2069'), (2070, '2070'), (2071, '2071'), (2072, '2072'), (2073, '2073'), (2074, '2074'), (2075, '2075'), (2076, '2076'), (2077, '2077'), (2078, '2078'), (2079, '2079'), (2080, '2080'), (2081, '2081'), (2082, '2082'), (2083, '2083'), (2084, '2084'), (2085, '2085'), (2086, '2086'), (2087, '2087'), (2088, '2088'), (2089, '2089'), (2090, '2090'), (2091, '2091'), (2092, '2092'), (2093, '2093'), (2094, '2094'), (2095, '2095'), (2096, '2096'), (2097, '2097'), (2098, '2098'), (2099, '2099'), (2100, '2100')], default=2024, verbose_name='Year start')),
                ('anneeFin', models.IntegerField(choices=[(1900, '1900'), (1901, '1901'), (1902, '1902'), (1903, '1903'), (1904, '1904'), (1905, '1905'), (1906, '1906'), (1907, '1907'), (1908, '1908'), (1909, '1909'), (1910, '1910'), (1911, '1911'), (1912, '1912'), (1913, '1913'), (1914, '1914'), (1915, '1915'), (1916, '1916'), (1917, '1917'), (1918, '1918'), (1919, '1919'), (1920, '1920'), (1921, '1921'), (1922, '1922'), (1923, '1923'), (1924, '1924'), (1925, '1925'), (1926, '1926'), (1927, '1927'), (1928, '1928'), (1929, '1929'), (1930, '1930'), (1931, '1931'), (1932, '1932'), (1933, '1933'), (1934, '1934'), (1935, '1935'), (1936, '1936'), (1937, '1937'), (1938, '1938'), (1939, '1939'), (1940, '1940'), (1941, '1941'), (1942, '1942'), (1943, '1943'), (1944, '1944'), (1945, '1945'), (1946, '1946'), (1947, '1947'), (1948, '1948'), (1949, '1949'), (1950, '1950'), (1951, '1951'), (1952, '1952'), (1953, '1953'), (1954, '1954'), (1955, '1955'), (1956, '1956'), (1957, '1957'), (1958, '1958'), (1959, '1959'), (1960, '1960'), (1961, '1961'), (1962, '1962'), (1963, '1963'), (1964, '1964'), (1965, '1965'), (1966, '1966'), (1967, '1967'), (1968, '1968'), (1969, '1969'), (1970, '1970'), (1971, '1971'), (1972, '1972'), (1973, '1973'), (1974, '1974'), (1975, '1975'), (1976, '1976'), (1977, '1977'), (1978, '1978'), (1979, '1979'), (1980, '1980'), (1981, '1981'), (1982, '1982'), (1983, '1983'), (1984, '1984'), (1985, '1985'), (1986, '1986'), (1987, '1987'), (1988, '1988'), (1989, '1989'), (1990, '1990'), (1991, '1991'), (1992, '1992'), (1993, '1993'), (1994, '1994'), (1995, '1995'), (1996, '1996'), (1997, '1997'), (1998, '1998'), (1999, '1999'), (2000, '2000'), (2001, '2001'), (2002, '2002'), (2003, '2003'), (2004, '2004'), (2005, '2005'), (2006, '2006'), (2007, '2007'), (2008, '2008'), (2009, '2009'), (2010, '2010'), (2011, '2011'), (2012, '2012'), (2013, '2013'), (2014, '2014'), (2015, '2015'), (2016, '2016'), (2017, '2017'), (2018, '2018'), (2019, '2019'), (2020, '2020'), (2021, '2021'), (2022, '2022'), (2023, '2023'), (2024, '2024'), (2025, '2025'), (2026, '2026'), (2027, '2027'), (2028, '2028'), (2029, '2029'), (2030, '2030'), (2031, '2031'), (2032, '2032'), (2033, '2033'), (2034, '2034'), (2035, '2035'), (2036, '2036'), (2037, '2037'), (2038, '2038'), (2039, '2039'), (2040, '2040'), (2041, '2041'), (2042, '2042'), (2043, '2043'), (2044, '2044'), (2045, '2045'), (2046, '2046'), (2047, '2047'), (2048, '2048'), (2049, '2049'), (2050, '2050'), (2051, '2051'), (2052, '2052'), (2053, '2053'), (2054, '2054'), (2055, '2055'), (2056, '2056'), (2057, '2057'), (2058, '2058'), (2059, '2059'), (2060, '2060'), (2061, '2061'), (2062, '2062'), (2063, '2063'), (2064, '2064'), (2065, '2065'), (2066, '2066'), (2067, '2067'), (2068, '2068'), (2069, '2069'), (2070, '2070'), (2071, '2071'), (2072, '2072'), (2073, '2073'), (2074, '2074'), (2075, '2075'), (2076, '2076'), (2077, '2077'), (2078, '2078'), (2079, '2079'), (2080, '2080'), (2081, '2081'), (2082, '2082'), (2083, '2083'), (2084, '2084'), (2085, '2085'), (2086, '2086'), (2087, '2087'), (2088, '2088'), (2089, '2089'), (2090, '2090'), (2091, '2091'), (2092, '2092'), (2093, '2093'), (2094, '2094'), (2095, '2095'), (2096, '2096'), (2097, '2097'), (2098, '2098'), (2099, '2099'), (2100, '2100')], default=2024, verbose_name='Year end')),
            ],
            options={
                'verbose_name': 'Promotion',
                'verbose_name_plural': 'Promotions',
                'db_table': '',
                'managed': True,
                'unique_together': {('anneeDebut', 'anneeFin')},
            },
        ),
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeMatiere', models.CharField(max_length=7, verbose_name='Code ')),
                ('denomination', models.CharField(max_length=50, verbose_name='Nom')),
                ('appreciation', models.CharField(blank=True, max_length=50, null=True, verbose_name='Appreciation')),
                ('classeMatiere', models.ManyToManyField(related_name='matieres_autorisees', to='classes.classe', verbose_name='Classe')),
                ('filiereMatiere', models.ManyToManyField(related_name='filieres_autorisees', to='classes.filiere', verbose_name='Filiere')),
            ],
            options={
                'verbose_name': 'Matiere',
                'verbose_name_plural': 'Matieres',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Coefficient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valeurCoefficient', models.PositiveIntegerField(verbose_name='Coefficient')),
                ('matiereCoefficient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='classes.matiere', verbose_name='Matiere')),
            ],
            options={
                'verbose_name': 'Coefficient',
                'verbose_name_plural': 'Coefficients',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
