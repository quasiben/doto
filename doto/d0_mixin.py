from __future__ import print_function, division, absolute_import
import requests

from doto.logger import log

class DOError(Exception):
    pass

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



            BASEURL = "https://api.digitalocean.com"
            response = requests.get(BASEURL+event,headers=headers,params=kwds)
            log.info('Getting '+event)
            log.debug(response.url)

            if response.status_code == 200:
                data = response.json()
                log.debug(data)

                if data['status'] == 'ERROR':
                    log.debug("Error with request: %s" % (data['message']))
                    error = "MSG: %s" % (data['message'])
                    raise DOError(error)

                if status_check:
                    return response.status_code

                return data
            else:
                #error
                error = "Status code: %d MSG: %s" % (response.status_code, data['message'])
                raise DOError(error)
