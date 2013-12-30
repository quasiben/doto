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
        # https://api.digitalocean.com/events/[event_id]/?
        # client_id=[your_client_id]&api_key=[your_api_key]

        data = self._request("/droplets/"+str(self.id))

        self.__dict__.update(**data['droplet'])

    def event_update(self):
        # https://api.digitalocean.com/events/[event_id]/?
        # client_id=[your_client_id]&api_key=[your_api_key]

        url = "/events/%s" % (str(self.event_id))
        data = self._request(url)
        log.debug("Updating Event")
        log.debug(data)

        data['event']['event_id'] = data['event']['id']
        data['event']['id'] = data['event']['droplet_id']

        self.__dict__.update(**data['event'])

    def percentage_update(self):
        """
        Convenience method to return the percentage of event completion
        """

        #needed to grab ip_address
        self.update()

        self.event_update()
        return self.percentage

    def rename(self,name=None):

        """
        This method renames the droplet to the specified name.

        :type name: str
        :param name: Name of the new droplet

        """

        # https://api.digitalocean.com/droplets/[droplet_id]/rename/?
        # client_id=[your_client_id]&api_key=[your_api_key]&name=[name]

        url = "/droplets/%s/rename" % (str(self.id))

        data = self._request(url,name=name)

        self.event_id = data['event_id']

        log.info("Renaming: %d To:%s Event: %d" % (self.id, name, self.event_id))

    def destroy(self, scrub_data=False):
        """
        This method destroys one of your droplets - this is irreversible.

        :type scrub_data: bool
        :param scrub_data: An optional bool which will strictly write 0s to your prior
        partition to ensure that all data is completely erased.

        """
        # https://api.digitalocean.com/droplets/[droplet_id]/destroy/?
        # client_id=[your_client_id]&api_key=[your_api_key]

        url = "/droplets/%s/destroy" % (str(self.id))

        data = self._request(url,scrub_data=scrub_data)

        self.event_id = data['event_id']

        log.info("Destroying: %d, Event: %d" % (self.id, self.event_id))

    def reboot(self):
        """
        This method allows you to reboot a droplet.
        This is the preferred method to use if a server is not responding.

        """
        # https://api.digitalocean.com/droplets/[droplet_id]/reboot/?
        # client_id=[your_client_id]&api_key=[your_api_key]

        url = "/droplets/%s/reboot" % (str(self.id))

        data = self._request(url)

        self.event_id = data['event_id']

        log.info("Rebooting: %d, Event: %d" % (self.id, self.event_id))

    def shutdown(self):
        """
        This method allows you to shutdown a droplet.
        The droplet will remain in your account.

        """
        # https://api.digitalocean.com/droplets/[droplet_id]/shutdown/
        # ?client_id=[your_client_id]&api_key=[your_api_key]

        url = "/droplets/%s/shutdown" % (str(self.id))

        data = self._request(url)

        self.event_id = data['event_id']

        log.info("Shutting Down: %d, Event: %d" % (self.id, self.event_id))
        log.info("Droplet remains active in your account")



    def power_cycle(self):
        """
        This method allows you to power cycle a droplet.
        This will turn off the droplet and then turn it back on.

        """

        # https://api.digitalocean.com/droplets/[droplet_id]/power_cycle/?
        # client_id=[your_client_id]&api_key=[your_api_key]

        url = "/droplets/%s/power_cycle" % (str(self.id))

        data = self._request(url)

        self.event_id = data['event_id']

        log.info("Power Cycle: %d, Event: %d" % (self.id, self.event_id))

    def power_off(self):
        """
        This method allows you to power off a droplet.
        This will turn off the droplet and then turn it back on.

        """

        # https://api.digitalocean.com/droplets/[droplet_id]/power_off/?
        # client_id=[your_client_id]&api_key=[your_api_key]

        url = "/droplets/%s/power_off" % (str(self.id))

        data = self._request(url)

        self.event_id = data['event_id']

        log.info("Powering Off: %d, Event: %d" % (self.id, self.event_id))



    def power_on(self):
        """
        This method allows you to power on a previously powered off droplet.

        """

        # https://api.digitalocean.com/droplets/[droplet_id]/power_on/?
        # client_id=[your_client_id]&api_key=[your_api_key]

        url = "/droplets/%s/power_on" % (str(self.id))

        data = self._request(url)

        self.event_id = data['event_id']

        log.info("Powering On: %d, Event: %d" % (self.id, self.event_id))


    def password_reset(self):
        """
        This method will reset the root password for a droplet.
        Please be aware that this will reboot the droplet to allow resetting the password.

        """

        # https://api.digitalocean.com/droplets/[droplet_id]/password_reset/?
        # client_id=[your_client_id]&api_key=[your_api_key]

        url = "/droplets/%s/password_reset" % (str(self.id))

        data = self._request(url)

        self.event_id = data['event_id']

        log.info("Resetting Password: %d, Event: %d" % (self.id, self.event_id))
        log.info("Rebooting Droplet")


    def resize(self,size=None):
        """
        This method allows you to resize a specific droplet to a different size.
        This will affect the number of processors and memory allocated to the droplet.

        :type size: int
        :param size: The new SIZE id of the droplet

        REQUIRES SNAPSHOT OF DROPLET

        """

        # https://api.digitalocean.com/droplets/[droplet_id]/resize/?size_id=[size_id]&
        # client_id=[your_client_id]&api_key=[your_api_key]

        url = "/droplets/%s/resize" % (str(self.id))

        data = self._request(url,size=size)

        self.event_id = data['event_id']

        log.info("Resizing Droplet: %d, Event: %d" % (self.id, self.event_id))
        log.info("Rebooting Droplet")

    def snapshot(self,name=None):
        """
        This method allows you to take a snapshot of the droplet once it has been powered off,
        which can later be restored or used to create a new droplet from the same image.
        Please be aware this may cause a reboot.

        :type name: string
        :param size: The NAME of the snapshot


        """

        # https://api.digitalocean.com/droplets/[droplet_id]/snapshot/?name=[snapshot_name]&
        # client_id=[your_client_id]&api_key=[your_api_key]

        url = "/droplets/%s/snapshot" % (str(self.id))

        data = self._request(url,name=name)

        self.event_id = data['event_id']

        log.info("Taking Snapshot: %d, Event: %d" % (self.id, self.event_id))

