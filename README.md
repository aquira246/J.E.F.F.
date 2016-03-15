# J.E.F.F.
JAPE Extension For Fun

By Andrew Acosta, Andrew Wang, and Sam Wu

Based on:

Ritchie, Graeme, Ruli Manurung, Helen Pain, Annalu Waller, Rolf Black, and Dave O’Mara. "A practical application of computational humour." In Proceedings of the 4th International Joint Conference on Computational Creativity, pp. 91-98. 2007.

Ritchie, Graeme. "The JAPE riddle generator: technical specification." Institute for Communicating and Collaborative Systems (2003).

#Dependencies:
- Python 3
  - selenium (OPTIONAL: for web scrapping)
  - BeautifulSoup (OPTIONAL: for web scrapping)
  - requests (OPTIONAL: for web scrapping)
  - ujson
  - NLTK
    - wordnet
    - averaged_perceptron_tagger
  - bottle (OPTIONAL: for web server)
- Apache (OPTIONAL: for web server)

#Running via CLI:
`python3 get_random_joke.py`

#Installing for web server:
1. Make sure apache has wsgi enabled
2. Symlink the JEFF directory under `/var/www` or other relevant web directory
3. Create htdocs directory
4. Edit restapi.conf as necessary for correct directory paths and port
5. Symlink restapi.conf to sites-enabled for apache
6. Test the webserver via the root url (e.g. `localhost:8080`)
   . Webserver should return a random joke in text string format
   . Note that the first request will take a few minutes as the webserver initializes with jokes

