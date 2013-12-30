from __future__ import print_function, division, absolute_import
import requests

from doto.logger import log

class d0mixin(object):

    def _request(self, event, status_check=None, **kwds):
            if 'client_id' not in kwds:
                kwds['client_id'] = self._client_id
            if 'api_key' not in kwds:
                kwds['api_key'] = self._api_key

            headers = {
                'User-Agent': 'doto/client'
            }

            for key, value in kwds.iteritems():
                log.debug("%s = %s" % (key, value))


            log.info('Getting '+event)

            BASEURL = "https://api.digitalocean.com"
            response = requests.get(BASEURL+event,headers=headers,params=kwds)
            log.debug(response.url)


            if response.status_code == 200:
                data = response.json()
                log.info("Successful return")
                log.debug(data)
                if status_check:
                    return response.status_code

                return data
            else:
                log.info("Error Getting Droplets")
                log.error(response.status_code)
                log.error("Error Getting Droplets")
                # error handling
                pass
