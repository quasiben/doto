import doto

d0 = doto.connect_d0()
new_key = d0.create_key_pair(ssh_key_name='a_new_key_test')
d0.get_all_ssh_keys(table=True)

droplet = d0.create_droplet(name='Random',
                            size_id=66, #512MB
                            image_id=2158507, #Docker 0.8 Ubuntu 13.04 x64
                            region_id=1, #New York
                            ssh_key_ids=[new_key['id']]
                            )



while droplet.percentage_update() != '100':
    print droplet.percentage

droplet.reboot()

while droplet.percentage_update() != '100':
    print droplet.percentage

droplet.rebuild(use_current=True)

while droplet.percentage_update() != '100':
    print droplet.percentage

droplet.destroy()
d0.delete_key_pair(ssh_key_id=new_key['id'])
