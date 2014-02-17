-------
Domains
-------

Droplets are the atomic unit of of compute instances on the Digital Ocean cloud service.  They are available in a
variety of RAM, HD, CPU configurations.

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
