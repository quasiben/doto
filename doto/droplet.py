from __future__ import print_function, division, absolute_import

from doto.logger import log
from doto.d0_mixin import d0mixin

import requests


class Droplet(d0mixin, object):

    def __str__(self):
        return ("Droplet:%s") % (self.id)

    def __repr__(self):
        return ("Droplet:%s") % (self.id)

    def __init__(self, **kwds):
        self.__dict__.update(kwds)

    def update(self):
        # https://api.digitalocean.com/events/[event_id]/?client_id=[your_client_id]&api_key=[your_api_key]

        data = self._request("/droplets/"+str(self.id))

        self.__dict__.update(**data['droplet'])


    def event_update(self):
        # https://api.digitalocean.com/events/[event_id]/?client_id=[your_client_id]&api_key=[your_api_key]

        url = "/events/%s" % (str(self.event_id))
        data = self._request(url)
        log.debug("Updating Event")
        log.debug(data)

        data['event']['event_id'] = data['event']['id']
        data['event']['id'] = data['event']['droplet_id']

        self.__dict__.update(**data['event'])


    def percentage_update(self):
        self.event_update()
        return self.percentage

    def destroy(self):
        # https://api.digitalocean.com/droplets/[droplet_id]/destroy/?client_id=[your_client_id]&api_key=[your_api_key]

        url = "/droplets/%s/destroy" % (str(self.id))

        data = self._request(url)

        self.event_id = data['event_id']

        log.info("Destroying: %d, Event: %d" % (self.id, self.event_id))


