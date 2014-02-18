--------
Droplets
--------

Droplets are the atomic unit of of compute instances on the Digital Ocean cloud service.  They are available in a
variety of RAM, HD, CPU configurations.

.. THIS IS A COMMENT automethod:: doto.connect_d0.create_droplet

Creating Droplets
-----------------

::

    droplet = d0.create_droplet(name='Random',
                                size_id=66, #512MB
                                image_id=1341147, #Docker 0.7 Ubuntu 13.04 x64
                                region_id=1, #New York
                                ssh_key_ids=[new_key['id']]
                                )

Getting a specific droplet
--------------------------

::

    droplet = d0.get_droplet(923125)

Getting all droplets
--------------------

::

    droplets = d0.get_all_droplets()


Droplet API
------------

.. autoclass:: doto.Droplet
   :members:
   :undoc-members:
