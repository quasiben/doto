.. doto documentation master file, created by
   sphinx-quickstart on Sat Jan 11 16:24:07 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

doto: A Python interface to Digital Ocean
========================================

DOTO is an open-source Python 2/3 interface to `Digital Ocean's API <http://developers.digitalocean.com/>`_.

Installing
----------

You can install ``doto`` with ``conda`` or ``pip``:

.. code-block:: console

    $ pip install doto
    $ conda install doto


Why yet another Python library for Digital Ocean?

* a
* b
* c

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
json converted dicts.  For example::

    In [1]: import doto

    In [2]: d0 = doto.connect_d0()

    In [3]: df_imgs = d0.get_all_images()
    >>> Getting /images

    In [5]: df_imgs.tail()
    Out[5]:
       distribution       id                                             name  \
    38       Ubuntu  1608711  Ruby on Rails on Ubuntu 12.10 (Nginx + Unicorn)
    39       CentOS  1646467                                   CentOS 6.5 x64
    40       CentOS  1646732                                   CentOS 6.5 x32
    41       Ubuntu  1687372                          Redmine on Ubuntu 12.04
    42       Ubuntu  1720819                                  GitLab 6.4.3 CE

       public  slug
    38   True  None
    39   True  None
    40   True  None
    41   True  None
    42   True  None

Pandas Dataframes -- while a bit heavy -- provide a nice interface for searching and sorting over.::

    In [6]: df_imgs.sort('distribution',inplace=True)

    In [7]: df_imgs.head()
    Out[7]:
       distribution      id                    name public  slug
    20   Arch Linux  361740  Arch Linux 2013.05 x32   True  None
    19   Arch Linux  350424  Arch Linux 2013.05 x64   True  None
    5        CentOS    1601          CentOS 5.8 x64   True  None
    26       CentOS  562354          CentOS 6.4 x64   True  None
    6        CentOS    1602          CentOS 5.8 x32   True  None


Currently Supported Services
============================
.. toctree::
    :maxdepth: 1

    Droplets
    Images
    Management
    PublicImages

Requirements
------------

* python 2.7 and 3.x
* pandas (>= 0.12)
* requests (>=2.0.1)
* pycrypto (>=2.6.1)


Release Notes
-------------



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


.. _API: http://developers.digitalocean.com/

