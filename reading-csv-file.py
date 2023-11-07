import csv
file_contents=open("Life Expectancy at Birth.csv")
csv_file_contents=csv.reader(file_contents)
for csv_file_content in csv_file_contents:
    ISO3, Country, Continent, Hemisphere, Human_Development_Groups, UNDP_Developing_Regions, HDI_Rank_2021, Life_Expect_1990, Life_Expect_1991, Life_Expect_1992, Life_Expect_1993, Life_Expect_1994, Life_Expect_1995, Life_Expect_1996, Life_Expect_1997, Life_Expect_1998, Life_Expect_1999,  Life_Expect_2000, Life_Expect_2001, Life_Expect_2002, Life_Expect_2003, Life_Expect_2004, Life_Expect_2005, Life_Expect_2006, Life_Expect_2007, Life_Expect_2008, Life_Expect_2009, Life_Expect_2010, Life_Expect_2011, Life_Expect_2012, Life_Expect_2013, Life_Expect_2014, Life_Expect_2015, Life_Expect_2016, Life_Expect_2017, Life_Expect_2018, Life_Expect_2019, Life_Expect_2020, Life_Expect_2021=csv_file_content
    print(
        "ISO3: {}, Country: {}, Continent: {}, Hemisphere: {}, Human_Development_Groups: {}, UNDP_Developing_Regions: {}, HDI_Rank_2021: {}, Life_Expect_1990: {}, Life_Expect_1991: {}, Life_Expect_1992: {}, Life_Expect_1993: {}, Life_Expect_1994: {}, Life_Expect_1995: {}, Life_Expect_1996: {}, Life_Expect_1997: {}, Life_Expect_1998: {}, Life_Expect_1999: {},  Life_Expect_2000: {}, Life_Expect_2001: {}, Life_Expect_2002: {}, Life_Expect_2003: {}, Life_Expect_2004: {}, Life_Expect_2005: {}, Life_Expect_2006: {}, Life_Expect_2007: {}, Life_Expect_2008: {}, Life_Expect_2009: {}, Life_Expect_2010: {}, Life_Expect_2011: {}, Life_Expect_2012: {}, Life_Expect_2013: {}, Life_Expect_2014: {}, Life_Expect_2015: {}, Life_Expect_2016: {}, Life_Expect_2017: {}, Life_Expect_2018: {}, Life_Expect_2019: {}, Life_Expect_2020: {}, Life_Expect_2021: {}".format(
            ISO3, Country, Continent, Hemisphere, Human_Development_Groups, UNDP_Developing_Regions, HDI_Rank_2021,
            Life_Expect_1990, Life_Expect_1991, Life_Expect_1992, Life_Expect_1993, Life_Expect_1994, Life_Expect_1995,
            Life_Expect_1996, Life_Expect_1997, Life_Expect_1998, Life_Expect_1999, Life_Expect_2000, Life_Expect_2001,
            Life_Expect_2002, Life_Expect_2003, Life_Expect_2004, Life_Expect_2005, Life_Expect_2006, Life_Expect_2007,
            Life_Expect_2008, Life_Expect_2009, Life_Expect_2010, Life_Expect_2011, Life_Expect_2012, Life_Expect_2013,
            Life_Expect_2014, Life_Expect_2015, Life_Expect_2016, Life_Expect_2017, Life_Expect_2018, Life_Expect_2019,
            Life_Expect_2020, Life_Expect_2021))
file_contents.close()