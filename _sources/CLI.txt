----------------------
Command Line Interface
----------------------

Doto provides a CLI tool for creating/destroying/managing resources on Digital Ocean from the command line.
Many arguments can be prepended with an optional `--wait`, which instructs doto not to return control of the prompt
until an event has completed.  This is especially useful during creation and destruction of droplets.


Droplets
--------

Example::

    $ doto start --name Random --size_id 66 --image_id 2158507 --region_id 1 --ssh_key_ids 89221

List of arguments:

- start
- listdroplets
- power-on
- power-off
- rebuilt
- terminate
- info


SSH Keys
--------

Example::

    $ doto createkey -o file_name

List of arguments:

- createkey
- deletekey
- listkeys

Images
------

Example::

    $ doto image "image name" show/destroy

List of arguments:

- image
- listimages

Snapshot
--------

Example::

    $ doto snapshot "droplet name" "snapshot name"

List of arguments:

- snapshot