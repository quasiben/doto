.. doto documentation master file, created by
   sphinx-quickstart on Sat Jan 11 16:24:07 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

doto: A Python interface to Digital Ocean
=========================================

DOTO is an open-source Python 2/3 interface to `Digital Ocean's API <http://developers.digitalocean.com/>`_.

Installing
----------

You can install ``doto`` with ``conda`` or ``pip``:

.. code-block:: console

    $ pip install doto
    $ conda install doto


Why yet another Python library for Digital Ocean?

* Logging
* boto like interface
* Optionally formatted tables for inline exploration

Getting Started
---------------

To get started with doto create a **.dotorc** file in a directory named, **~/.doto**, with your
**api_key** and **client_id** listed::

    [Credentials]
    client_id = XXXXXXXXXXXXX
    api_key = 99999999999999999999999

You are now ready to use doto::

    import doto
    d0 = doto.connect_d0()

    new_key = d0.create_key_pair('my_new_key_pair')
    droplet = d0.create_droplet(name='Random',
                                size_id=66, #512MB
                                image_id=1341147, #Docker 0.7 Ubuntu 13.04 x64
                                region_id=1, #New York
                                ssh_key_ids=[new_key['id']]
                                )


Doto is designed to support both Python 2.7 and Python 3.  A number of functions add a bit more than just returning
json converted dicts.  For example, **Images** and **Droplets** are objects within doto where data such as, event_id,
ip_address, status, etc. are stored as attributes with respect to the individual object::


    In [1]: import doto
    d0
    In [2]: d0 = doto.connect_d0()

    In [22]: images = d0.get_all_images()
    >>> Getting /images

    In [23]: images
    Out[23]:
    [Image:490208,
     Image:568111,
     Image:633923,
     Image:714697,
     Image:1420886,
     Image:1898676,
     Image:2003826,...]

Additionally, doto supports filtering on valid keys::

    In [3]: filters = {'distribution':u'CentOS','name':'x64'}

    In [4]: images = d0.get_all_images(filters=filters)
    >>> Getting /images

    In [5]: for img in images:
        print img.distribution, img.name, img.id
       ...:
    CentOS CentOS 5.8 x64 1601
    CentOS CentOS 6.4 x64 562354
    CentOS CentOS 6.5 x64 1646467


To view information inline, users can provide an optional **Table=True** argument for a well formatted table::

    In [3]: d0.get_all_images(table=True)
    >>> Getting /images
    | Ubuntu       | None | True   | 1505699 | Ubuntu 13.10 x64                                |
    | Ubuntu       | None | True   | 1608711 | Ruby on Rails on Ubuntu 12.10 (Nginx + Unicorn) |
    | CentOS       | None | True   | 1646467 | CentOS 6.5 x64                                  |
    | CentOS       | None | True   | 1646732 | CentOS 6.5 x32                                  |
    | Ubuntu       | None | True   | 1687372 | Redmine on Ubuntu 12.04                         |
    | Ubuntu       | None | True   | 1860934 | Ghost 0.4.0 on Ubuntu 12.04                     |
    | Ubuntu       | None | True   | 2105243 | GitLab 6.5.1 CE                                 |
    | Ubuntu       | None | True   | 2118237 | Dokku-v0.2.1 on Ubuntu 13.04                    |
    | Ubuntu       | None | True   | 2158507 | Docker 0.8 Ubuntu 13.04 x64                     |
    ...


Currently Supported Services
============================
.. toctree::
    :maxdepth: 1

    Droplets
    Images
    Domains
    Management
    config
    PublicImages

Requirements
------------

* requests (>=2.0.1)
* pycrypto (>=2.6.1)
* six (>=1.3.0)


Release Notes
-------------



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


.. _API: http://developers.digitalocean.com/

