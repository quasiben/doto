------
Images
------

A droplet is created using a pre-defined **Image**.  Users can select from nearly 40
:doc:`Public Images </PublicImages>` or from snapshots and backups previously created.

.. THIS IS A COMMENT automethod:: doto.connect_d0.create_droplet

Creating Snapshots
------------------

::

    >>>d0.create_snapshot(name='My New Snapshot')

Getting a specific image
------------------------

::

    >>>images = d0.get_image(1860934)

Getting all images
------------------

::

    >>>images = d0.get_all_images()

    >>>images
    [Image:490208,
     Image:568111,
     Image:633923,
     Image:714697,
     Image:1420886,
     Image:1898676,
     Image:2003826,...]

    >>>d0.get_all_images(table=True)
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



Image API
------------

.. autoclass:: doto.Image
   :members:
   :undoc-members:
