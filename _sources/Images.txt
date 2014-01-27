------
Images
------

A droplet is created using a pre-defined **Image**.  Users can select from nearly 40
:doc:`Public Images </PublicImages>` or from snapshots and backups previously created.

.. THIS IS A COMMENT automethod:: doto.connect_d0.create_droplet

Creating Snapshots
------------------

::

    d0.create_snapshot(name='My New Snapshot')

Getting a specific image
------------------------

::

    image = d0.get_image(1860934)

Getting all images
------------------

::

        df_imgs = d0.get_all_images()

        df_imgs.sort('distribution',inplace=True)
        print df_imgs.head()


Image API
------------

.. autoclass:: doto.Image
   :members:
   :undoc-members:
