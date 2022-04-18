{\rtf1\ansi\ansicpg1252\cocoartf2580
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\froman\fcharset0 Times-Roman;\f1\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;\red255\green255\blue255;}
{\*\expandedcolortbl;;\cssrgb\c0\c1\c1;\cssrgb\c100000\c100000\c99985\c0;}
{\*\listtable{\list\listtemplateid1\listhybrid{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{none\}}{\leveltext\leveltemplateid1\'00;}{\levelnumbers;}\fi-360\li720\lin720 }{\listname ;}\listid1}}
{\*\listoverridetable{\listoverride\listid1\listoverridecount0\ls1}}
\paperw11900\paperh16840\margl1440\margr1440\vieww13940\viewh14560\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs29\fsmilli14667 \cf2 \cb3 \expnd0\expndtw0\kerning0
import time\
from geopy.geocoders import Nominatim\
\
geolocator = Nominatim( user_agent='geopyExercises' )\
\
def get_data( x ):\
      index, row = x\
      time.sleep(1)\
\
\
#chamada API\
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls1\ilvl0\cf2 \cb3 \kerning1\expnd0\expndtw0 		      \cf2 \cb3 \expnd0\expndtw0\kerning0
response = geolocator.reverse( row['query'] )\
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls1\ilvl0
\f1\fs24 \cf2 \cb3 \kerning1\expnd0\expndtw0 		\
		\
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls1\ilvl0
\f0\fs29\fsmilli14667 \cf2 \cb3 		\cf2 \cb3 \expnd0\expndtw0\kerning0
      place_id = response.raw['place_id'] if 'place_id' in response.raw else 'NA'\
\ls1\ilvl0\cf2 \cb3 \kerning1\expnd0\expndtw0 		\cf2 \cb3 \expnd0\expndtw0\kerning0
      osm_type = response.raw['osm_type'] if 'osm_type' in response.raw else 'NA'\
\ls1\ilvl0\cf2 \cb3 \kerning1\expnd0\expndtw0 		\cf2 \cb3 \expnd0\expndtw0\kerning0
      country = address['country'] if 'country' in address else 'NA'\
\pard\pardeftab720\sa240\partightenfactor0
\cf2 \cb3                 country_code = address['country_code'] if 'country_code' in address 'NA'
\fs24 \cf2 \cb3 \
\pard\pardeftab720\partightenfactor0

\fs29\fsmilli14667 \cf2 \cb3       return place_id, osm_type, country, country_code\
\pard\pardeftab720\sa240\partightenfactor0

\fs24 \cf2 \cb3 \
}