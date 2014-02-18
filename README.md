[![Build Status](https://travis-ci.org/quasiben/doto.png?branch=master)](https://travis-ci.org/quasiben/doto)

doto
====

Doto is a Python interface to Digital Ocean with an emphasis on production usage.
doto supports the full Digital Ocean API:

**Full Documentation at: http://quasiben.github.io/doto/**

To get started with doto create a **.dotorc** file in a directory named, **~/.doto**, with your **api_key**
and **client_id** listed:

```
[Credentials]
client_id = XXXXXXXXXXXXX
api_key = 99999999999999999999999
```

You are now ready to use doto

```python
import doto
d0 = doto.connect_d0()

new_key = d0.create_key_pair('my_new_key_pair')
droplet = d0.create_droplet(name='Random',
                            size_id=66, #512MB
                            image_id=2158507, #Docker 0.8 Ubuntu 13.04 x64
                            region_id=1, #New York
                            ssh_key_ids=[new_key['id']]
                            )
while droplet.percentage_update() != '100':
    print droplet.percentage
```

Doto is designed to support both Python 2.7 and Python 3 and provides an interface with filtering options similar to
**boto**.

```python
In [1]: import doto
d0
In [2]: d0 = doto.connect_d0()

In [3]: filters = {'distribution':u'CentOS','name':'x64'}

In [4]: d0.get_all_images(filters=filters)
>>> Getting /images
Out[4]: [Image:1601, Image:562354, Image:1646467]

In [5]: images = d0.get_all_images(filters=filters)
>>> Getting /images

In [6]: for img in images:
    print img.distribution, img.name, img.id
   ...:
CentOS CentOS 5.8 x64 1601
CentOS CentOS 6.4 x64 562354
CentOS CentOS 6.5 x64 1646467
```

Using the **table=True** argument, for a number of **get** funcs prints a well formatted table for inline exploratory

sessions:

```python

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
```
