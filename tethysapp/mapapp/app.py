from tethys_sdk.base import TethysAppBase, url_map_maker


class Mapapp(TethysAppBase):
    """
    Tethys app class for Map App.
    """

    name = 'Map App'
    index = 'mapapp:home'
    icon = 'mapapp/images/icon.gif'
    package = 'mapapp'
    root_url = 'mapapp'
    color = '#800000'
    description = 'The app for my map. '
    tags = '&quot;tag&quot;'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='mapapp',
                controller='mapapp.controllers.home'
            ),
            UrlMap(
                name='map',
                url='mapapp/map',
                controller='mapapp.controllers.map'
            ),
            UrlMap(
                name='data',
                url='mapapp/data',
                controller='mapapp.controllers.data'
            ),
            UrlMap(
                name='about',
                url='mapapp/about',
                controller='mapapp.controllers.about'
            ),
        )

        return url_maps
