-------
Domains
-------

Digital Ocean allows users to easily setup and control hostnames and subdomains for existing droplets.
Simply point the DNS of your host provider to:

- ns1.digitalocean.com
- ns2.digitalocean.com
- ns3.digitalocean.com

For full documentation on setup please read:
`How To Set Up a Host Name with DigitalOcean <https://www.digitalocean.com/community/articles/how-to-set-up-a-host-name-with-digitalocean>`_.


.. THIS IS A COMMENT automethod:: doto.connect_d0.create_droplet

Creating Domains
----------------

::

    domain = d0.create_domain(name='myurl.com',ip_addr='555.55.5.55')

    #or with a droplet
    droplet = d0.create_droplet(..)
    domain = d0.create_domain(name='myurl.com',ip_addr=droplet.ip_address)

Getting a specific domain
--------------------------

::

    droplet = d0.get_domain(domain_id=555555)

Getting all droplets
--------------------

::

    domains = d0.get_all_domains()


Droplet API
------------

.. autoclass:: doto.Domain
   :members:
   :undoc-members:
