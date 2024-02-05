Project: 'l_topo2_project' created on 2019-11-29
Author: Marc Dacier ( dacier@eurecom.fr)

This is a simple topology based on an ad hoc container available on docker hub (marcdacier/topo2) that mimics a simplistic network topology with three networks, an extranet, a dmz and an intranet.

All machines running, including the routers are using this same alpine based container

Do not try to modify the configuration of the node with the GNS3 interface as they are preconfigured with a bunch of ad hoc scripts that are launched at boot time (docker run)