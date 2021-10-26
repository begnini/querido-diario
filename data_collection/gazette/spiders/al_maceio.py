from gazette.spiders.base.sigpub import SigpubGazetteSpider


class AlAssociacaoMunicipiosSpider(SigpubGazetteSpider):
    name = "al_maceio"
    TERRITORY_ID = "2704302"
    CALENDAR_URL = "http://www.diariomunicipal.com.br/maceio"
